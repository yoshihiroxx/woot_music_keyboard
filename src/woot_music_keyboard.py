import ctypes
import os

from single_woot_midi_key import SingleWootMidiKey
from helpers.midi_note_helper import getMidiNoteByScanCode



class WootMusicKeyboard():

    def __init__(self):
        self.woot_midi_keys = {}
        self._observers = {}

        #load sdk
        base_path = os.path.dirname(os.path.abspath(__file__))
        sdk_path = os.path.join(base_path, '..\\wooting-analog-sdk.dll')
        self.sdk = ctypes.cdll.LoadLibrary(sdk_path)

        #init ctypes array
        self.buffer_size = ctypes.c_uint(32)
        analogBuffer = ctypes.c_uint8 * 32
        self.buffer_arr = analogBuffer()

        if self.sdk.wooting_kbd_connected() :
            print('wooting has connected')
        else:
            print('wooting has not connected')

    def on(self, name, callback):
        self._observers[name] = callback

    def emit(self, name, note, vel):
        if name in self._observers:
            if note < 127:
                self._observers[name](note, vel)

    def update(self):

        #get active_keys_count and update buffer
        active_keys_count = self.sdk.wooting_read_full_buffer(ctypes.byref(self.buffer_arr), self.buffer_size)
        active_key_numbers = []

        #create single key instance, and regist event
        for i in range(active_keys_count):

            num = self.buffer_arr[i*2]
            pressure = self.buffer_arr[i*2 + 1]

            active_key_numbers.append( num )

            if str(num) in self.woot_midi_keys:
                self.woot_midi_keys[str(num)].updateValue(pressure)

            else:
                self.woot_midi_keys[str(num)] = SingleWootMidiKey(num, pressure, 200)

                def noteOnHandler(n, vel):
                    note_num = getMidiNoteByScanCode( n )
                    self.emit('noteOn', note_num, vel)

                self.woot_midi_keys[str(num)].on( 'noteOn', callback = noteOnHandler)

                def noteOffHandler(n, vel):
                    note_num = getMidiNoteByScanCode( n )
                    print(note_num, vel)
                    self.emit('noteOff', note_num, vel)

                self.woot_midi_keys[str(num)].on('noteOff', callback = noteOffHandler)

        # check note off and remove instance if released key
        for key in list(self.woot_midi_keys):
            if int(key) not in active_key_numbers:
                self.woot_midi_keys[key].updateValue(0)
                self.woot_midi_keys.pop(key)
