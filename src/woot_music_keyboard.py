import ctypes
import os

from single_woot_midi_key import SingleWootMidiKey
from helpers.midi_note_helper import getMidiNoteByScanCode, getKeyNameByScanCode
from helpers.row_col_helper import getMatIdByNoteNum, isLeft, isRight
from midi_map_manager import MidiMapManager
from led_manager import LedManager

class WootMusicKeyboard():

    def __init__(self):
        self.woot_midi_keys = {}
        self._observers = {}

        # managers
        self.midiMapManager = MidiMapManager()
        self.ledManager = LedManager(self.midiMapManager)
        self.ledManager.init_leds()

        # load sdk
        base_path = os.path.dirname(os.path.abspath(__file__))
        analog_sdk_path = os.path.join(base_path, '..\\wooting-analog-sdk.dll')
        self.analog_sdk = ctypes.cdll.LoadLibrary(analog_sdk_path)

        rgb_sdk_path = os.path.join(base_path, '..\\wooting-rgb-sdk.dll')
        self.rgb_sdk = ctypes.cdll.LoadLibrary(rgb_sdk_path)

        # init ctypes array
        self.buffer_size = ctypes.c_uint(32)
        analogBuffer = ctypes.c_uint8 * 32
        self.buffer_arr = analogBuffer()

        if self.analog_sdk.wooting_kbd_connected():
            print('wooting has connected')
        else:
            print('wooting has not connected')

    def on(self, name, callback):
        self._observers[name] = callback

    def emit(self, name, note, vel):
        if name in self._observers:
            if note < 127:
                self._observers[name](note, vel)

    def rgb_direct_set_key_by_note(self,note, red, green, blue):
        self.ledManager.light_up_key_by_note(note)

    def rgb_direct_reset_key_by_note(self, note):
        self.ledManager.light_off_key_by_note(note)

    def reset_rgb(self):
        self.rgb_sdk.wooting_rgb_reset()

    def set_key(self, new_key_value):
        self.ledManager.key_shift(new_key_value)

    def update(self):
        # get active_keys_count and update buffer
        active_keys_count = self.analog_sdk.wooting_read_full_buffer(ctypes.byref(self.buffer_arr), self.buffer_size)
        active_key_numbers = []
        # create single key instance, and regist events
        for i in range(active_keys_count):

            # the values to process
            scan_code = self.buffer_arr[i*2]
            pressure = self.buffer_arr[i*2 + 1]
            active_key_numbers.append(scan_code)

            # update already created key
            if str(scan_code) in self.woot_midi_keys:
                self.woot_midi_keys[str(scan_code)].update_value(pressure)

            # handle as new
            else:

                # get midi note value from scan code
                note_num = getMidiNoteByScanCode(scan_code)
                key_name = getKeyNameByScanCode(scan_code)
                dynamic_note = note_num
                if note_num <= 108:
                    dynamic_note = self.midiMapManager.get_maped_notenum_by_key_name(key_name, note_num)

                self.woot_midi_keys[str(scan_code)] = SingleWootMidiKey(dynamic_note, pressure, 200)

                def note_on_handler(n_num, vel):

                    if n_num == 200:  # right shift
                        self.midiMapManager.set_octave('right',  -1)
                    elif n_num == 201:  # right ctrl
                        self.midiMapManager.set_octave('right',  1)
                    if n_num == 202:  # left shift
                        self.midiMapManager.set_octave('left',  -1)
                    elif n_num == 203:  # left ctrl
                        self.midiMapManager.set_octave('left',  1)
                    if n_num == 204:  # shift master octave +1
                        self.midiMapManager.shift_octave('master', 1)
                    elif n_num == 205:  # shift master octave -1
                        self.midiMapManager.shift_octave('master', -1)

                    self.emit('noteOn', n_num, vel)

                self.woot_midi_keys[str(scan_code)].on('noteOn', callback=note_on_handler)

                def note_off_handler(n_num, vel):
                    if n_num == 200 or n_num == 201:  # right shift
                        self.midiMapManager.set_octave('right',  0)
                    if n_num == 202 or n_num == 203:  # left ctrl
                        self.midiMapManager.set_octave('left',  0)
                    self.emit('noteOff', n_num, vel)

                self.woot_midi_keys[str(scan_code)].on('noteOff', callback=note_off_handler)

        # check note off and remove instance if released key
        for key in list(self.woot_midi_keys):
            if int(key) not in active_key_numbers:
                self.woot_midi_keys[key].update_value(0)
                self.woot_midi_keys.pop(key)
