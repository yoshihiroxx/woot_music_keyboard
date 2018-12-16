import os, sys, ctypes
from helpers.row_col_helper import getMatIdByNoteNum, isLeft, isRight
import time

class LedManager():

    def __init__(self, midi_note_manager):
        self.sdk = self._get_sdk()
        self.key_shift_num = 0
        self.root_color = [0, 0 , 255]
        self.note_color = [140, 255, 230]
        self.octave_control_key_color = [0, 255, 0]
        self.note_recieve_color = [255, 255, 0]
        self.midi_note_manager = midi_note_manager
        self.left_note_on_keys_buffer = []
        self.right_note_on_keys_buffer = []

    def _get_sdk(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        rgb_sdk_path = os.path.join(base_path, '..\\wooting-rgb-sdk.dll')
        rgb_sdk = ctypes.cdll.LoadLibrary(rgb_sdk_path)
        return rgb_sdk

    def init_leds(self, octave = 0):
        for i in range(6):
            indices = getMatIdByNoteNum(200 + i)
            if indices is not None:
                for row_and_col in indices:
                    color = self.octave_control_key_color
                    self.sdk.wooting_rgb_direct_set_key( int(row_and_col[0]), int(row_and_col[1]), color[0], color[1], color[2])
                    time.sleep(0.001)

        for i in range(108):
            indices = self.midi_note_manager.getMatIdByNoteNum(i + octave*12)
            # if i >= 200 and i <= 205:
                # color = self.octave_control_key_color
            color = self._get_color_by_note(i)
            if indices is not None:
                for row_and_col in indices:
                    self.sdk.wooting_rgb_direct_set_key( int(row_and_col[0]), int(row_and_col[1]), color[0], color[1], color[2])
                    time.sleep(0.001)

    def key_shift(self, key_shift):
        self.key_shift_num = key_shift
        self.init_leds()

    def light_up_key_by_note(self, note):
        to_light_up_keys_indices = self.midi_note_manager.getMatIdByNoteNum(note)
        if to_light_up_keys_indices is not None:
            for row_and_col in to_light_up_keys_indices:
                self._add_key_buffer_object(note, row_and_col)
                color = self.note_recieve_color
                self.sdk.wooting_rgb_direct_set_key(int(row_and_col[0]), int(row_and_col[1]), color[0], color[1], color[2])

    def light_off_key_by_note(self, note):
        to_light_up_keys_indices = self.midi_note_manager.getMatIdByNoteNum(note)
        if to_light_up_keys_indices is not None:
            color = [0,0,0]
            if (note -self.key_shift_num) % 12 is 0:
                color = self.root_color
            elif (note - self.key_shift_num ) % 12 in [2, 4, 5, 7, 9 ,11]:
                color = self.note_color
            for row_and_col in to_light_up_keys_indices:
                self.sdk.wooting_rgb_direct_set_key(int(row_and_col[0]), int(row_and_col[1]), color[0], color[1], color[2])

    def init_left(self):
        for key in self.left_note_on_keys_buffer:
            self.sdk.wooting_rgb_direct_set_key(int(key['row_and_col'][0]), int(key['row_and_col'][1]), key['color'][0], key['color'][1], key['color'][2])
        self.left_note_on_keys_buffer = []

    def init_right(self):
        for key in self.right_note_on_keys_buffer:
            self.sdk.wooting_rgb_direct_set_key(int(key['row_and_col'][0]), int(key['row_and_col'][1]), key['color'][0], key['color'][1], key['color'][2])
        self.right_note_on_keys_buffer = []

    def _get_color_by_note(self, note):
        if (note - self.key_shift_num) % 12 is 0:
            return self.root_color
        elif (note - self.key_shift_num) % 12 in [2, 4, 5, 7, 9 ,11]:
            return self.note_color
        else:
            return [0, 0, 0]

    def _add_key_buffer_object(self, note, row_and_col):
        key = {
            'row_and_col': row_and_col,
            'color': self._get_color_by_note(note)
        }

        if isLeft(int(row_and_col[0]), int(row_and_col[1])):
            self.left_note_on_keys_buffer.append(key)
        if isRight(int(row_and_col[0]), int(row_and_col[1])):
            self.right_note_on_keys_buffer.append(key)