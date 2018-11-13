from helpers.row_col_helper import getMatIdByNoteNum as _getMatIdByNoteNum
from helpers.row_col_helper import getMatIdByName
from helpers.row_col_helper import isLeft, isRight
import numpy as np

class MidiMapManager():
    def __init__(self):
        self.octaves = {
            "master": 0,
            "left" : 0,
            "right" : 0
        }

    def set_octave(self, name, value):
        self.octaves[name] = value

    def shift_octave(self, name, value):
        self.ocataves[name] += value

    def get_maped_notenum_by_key_name(self, key_name, note):
        row_and_col = getMatIdByName(key_name)
        note_num = note
        if isRight(row_and_col[0], row_and_col[1]):
            note_num = note_num + (self.octaves['right'] * 12)
        if isLeft(row_and_col[0], row_and_col[1]):
            note_num = note_num + (self.octaves['left'] * 12)

        note_num = note_num + (self.octaves['master'] * 12)
        return note_num if note_num <= 108 else 0

    def getMatIdByNoteNum(self, note):
        marged_ids = np.empty((0,2), int)

        left_decoded_note = note - self.octaves["left"]*12 - self.octaves["master"]*12
        left_indices = _getMatIdByNoteNum(left_decoded_note)
        if left_indices is not None:
            for left_id in left_indices:
                if left_id is not None and isLeft(left_id[0], left_id[1]):
                    marged_ids = np.append( marged_ids, left_id.reshape(1,2), axis=0 )

        right_decoded_note = note - self.octaves["right"]*12 - self.octaves["master"]*12
        right_indices = _getMatIdByNoteNum(right_decoded_note)
        if right_indices is None:
            for right_id in right_indices :
                if right_id is not None and isRight(right_id[0], right_id[1]):
                    marged_ids = np.append( marged_ids, right_id.reshape(1,2), axis=0)

        return marged_ids