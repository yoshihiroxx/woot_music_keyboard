import ctypes
import os

from single_woot_midi_key import SingleWootMidiKey
from helpers.midi_note_helper import getMidiNoteByScanCode
from helpers.row_col_helper import getMatIdByNoteNum, isLeft, isRight



class WootMusicKeyboard():

    def __init__(self):
        self.woot_midi_keys = {}
        self._observers = {}
        self.octaves = {
            "master": 0,
            "left" : 0,
            "right" : 0
        }

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
        row_and_col = getMatIdByNoteNum(note)
        if row_and_col:
            self.rgb_sdk.wooting_rgb_direct_set_key(int(row_and_col[0][0]), int(row_and_col[1][0]), red, green, blue)

    def rgb_direct_reset_key_by_note(self, note):
        row_and_col = getMatIdByNoteNum(note)
        if row_and_col:
            self.rgb_sdk.wooting_rgb_direct_reset_key(int(row_and_col[0][0]), int(row_and_col[1][0]))

    def reset_rgb(self):
        self.rgb_sdk.wooting_rgb_reset()

    def _apply_current_octave(self, note_num):
        row_and_col = getMatIdByNoteNum(note_num)
        if isRight(int(row_and_col[0][0]), int(row_and_col[1][0])):
            note_num = note_num + (self.octaves['right'] * 12)

        if isLeft(int(row_and_col[0][0]), int(row_and_col[1][0])):
            note_num = note_num + (self.octaves['left'] * 12)

        note_num = note_num + (self.octaves['master'] * 12)
        return note_num if note_num <= 108 else 0

    def update(self):
        # get active_keys_count and update buffer
        active_keys_count = self.analog_sdk.wooting_read_full_buffer(ctypes.byref(self.buffer_arr), self.buffer_size)
        active_key_numbers = []
        # create single key instance, and regist events
        for i in range(active_keys_count):
            scan_code = self.buffer_arr[i*2]
            pressure = self.buffer_arr[i*2 + 1]
            active_key_numbers.append(scan_code)

            if str(scan_code) in self.woot_midi_keys:
                self.woot_midi_keys[str(scan_code)].update_value(pressure)

            else:
                note_num = getMidiNoteByScanCode(scan_code)
                dynamic_note = note_num
                if note_num <= 108:
                    dynamic_note = self._apply_current_octave(note_num)

                self.woot_midi_keys[str(scan_code)] = SingleWootMidiKey(dynamic_note, pressure, 200)

                def note_on_handler(n_num, vel):

                    if n_num == 200:  # right shift
                        self.octaves['right'] = -1
                    elif n_num == 201:  # right ctrl
                        self.octaves['right'] = 1
                    if n_num == 202:  # left shift
                        self.octaves['left'] = -1
                    elif n_num == 203:  # left ctrl
                        self.octaves['left'] = 1
                    if n_num == 204:  # shift master octave +1
                        self.octaves['master'] += 1
                    elif n_num == 205:  # shift master octave -1
                        self.octaves['master'] -= 1

                    self.emit('noteOn', n_num, vel)

                self.woot_midi_keys[str(scan_code)].on('noteOn', callback=note_on_handler)

                def note_off_handler(n_num, vel):
                    if n_num == 200 or n_num == 201:  # right shift
                        self.octaves['right'] = 0
                    if n_num == 202 or n_num == 203:  # left ctrl
                        self.octaves['left'] = 0
                    self.emit('noteOff', n_num, vel)

                self.woot_midi_keys[str(scan_code)].on('noteOff', callback=note_off_handler)

        # check note off and remove instance if released key
        for key in list(self.woot_midi_keys):
            if int(key) not in active_key_numbers:
                self.woot_midi_keys[key].update_value(0)
                self.woot_midi_keys.pop(key)
