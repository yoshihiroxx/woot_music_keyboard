from enum import IntEnum
import numpy as np
from .midi_map import MIDI_MAP


def getMatIdByNoteNum(note):
    row_and_col_array = None
    try:
      key_name = MIDI_MAP(note).name
      for name, member in MIDI_MAP.__members__.items():
        if member.name is key_name and member.name is not name:
            if row_and_col_array is None:
                row_and_col_array = getMatIdByNameAs2d(name)
            else:
                row_and_col_array = np.append(row_and_col_array, getMatIdByNameAs2d(name), axis=0)
      if row_and_col_array is not None:
        return np.append( row_and_col_array, getMatIdByNameAs2d(key_name),axis=0)
      else:
        return getMatIdByNameAs2d(key_name)
    except:
      print('getMatIdByNoteNum got error')
      return None

def getMatIdByNameAs2d(name):
    return getMatIdByName(name).reshape(1,2)

def getMatIdByName(name):
    np_array = np.array(key_mat)
    index_array = np.array(np.where(np_array == name))
    if np.array(index_array).size is not 0:
        return np.array(index_array).reshape(2)
    else:
        print('given error value')
        return index_array

def isLeft(row, col):
    if row == 1 and col <= 6 :
        return True
    elif row == 2 and col <= 5 :
        return True
    elif row == 3 and col <= 5 :
        return True
    elif row == 4 and col <= 6 :
        return True
    elif row == 5 and col <= 6 :
        return True
    elif row == 0 and col <= 6 :
        return True
    else :
        return False

def isRight(row, col):
    if row == 1 and col > 6 :
        return True
    elif row == 2 and col > 5 :
        return True
    elif row == 3 and col > 5 :
        return True
    elif row == 4 and col > 6 :
        return True
    elif row == 5 and col > 6 :
        return True
    elif row == 0 and col > 6 :
        return True
    else :
        return False


key_mat = [
    [
        "SCAN_Escape",
        0,
        "SCAN_F1",
        "SCAN_F2",
        "SCAN_F3",
        "SCAN_F4",
        "SCAN_F5",
        "SCAN_F6",
        "SCAN_F7",
        "SCAN_F8",
        "SCAN_F9",
        "SCAN_F10",
        "SCAN_F11",
        "SCAN_F12",
        "SCAN_Printscreen",
        "SCAN_Pause",
        "SCAN_Mode",
        "SCAN_A1",
        "SCAN_A2",
        "SCAN_A3",
        "SCAN_FullsizeMode"
    ],
    [
        "SCAN_Tilde",
        "SCAN_Number1",
        "SCAN_Number2",
        "SCAN_Number3",
        "SCAN_Number4",
        "SCAN_Number5",
        "SCAN_Number6",
        "SCAN_Number7",
        "SCAN_Number8",
        "SCAN_Number9",
        "SCAN_Number0",
        "SCAN_Underscore",
        "SCAN_Plus",
        "SCAN_Backspace",
        "SCAN_Insert",
        "SCAN_Home",
        "SCAN_PageUp",
        "SCAN_NumLock",
        "SCAN_NumpadDivide",
        "SCAN_NumpadMultiply",
        "SCAN_NumpadMinus",
    ],
    [
        "SCAN_Tab",
        "SCAN_Q",
        "SCAN_W",
        "SCAN_E",
        "SCAN_R",
        "SCAN_T",
        "SCAN_Y",
        "SCAN_U",
        "SCAN_I",
        "SCAN_O",
        "SCAN_P",
        "SCAN_OpenBracket",
        "SCAN_CloseBracket",
        "SCAN_Backslash",
        "SCAN_Delete",
        "SCAN_End",
        "SCAN_PageDown",
        "SCAN_Numpad7",
        "SCAN_Numpad8",
        "SCAN_Numpad9",
        "SCAN_NumpadPlus",
    ],
    [
        "SCAN_CapsLock",
        "SCAN_A",
        "SCAN_S",
        "SCAN_D",
        "SCAN_F",
        "SCAN_G",
        "SCAN_H",
        "SCAN_J",
        "SCAN_K",
        "SCAN_L",
        "SCAN_Colon",
        "SCAN_Quote",
        "SCAN_ExtraIso",
        "SCAN_Enter",
        0,
        0,
        0,
        "SCAN_Numpad4",
        "SCAN_Numpad5",
        "SCAN_Numpad6",
        0
    ],
    [
        "SCAN_ModifierLeftShift",
        "SCAN_ExtraIso",
        "SCAN_Z",
        "SCAN_X",
        "SCAN_C",
        "SCAN_V",
        "SCAN_B",
        "SCAN_N",
        "SCAN_M",
        "SCAN_Comma",
        "SCAN_Dot",
        "SCAN_Slash",
        0,
        "SCAN_ModifierRightShift",
        0,
        "SCAN_Up",
        0,
        "SCAN_Numpad1",
        "SCAN_Numpad2",
        "SCAN_Numpad3",
        "SCAN_NumpadEnter",

    ],
    [
        "SCAN_ModifierLeftCtrl",
        "SCAN_ModifierLeftUi",
        "SCAN_ModifierLeftAlt",
        0,
        0,
        0,
        "SCAN_Spacebar",
        0,
        0,
        0,
        "SCAN_ModifierRightAlt",
        "SCAN_ModifierRightUi",
        "SCAN_FnKey",
        "SCAN_ModifierRightCtrl",
        "SCAN_Left",
        "SCAN_Down",
        "SCAN_Right",
        0,
        "SCAN_Numpad0",
        "SCAN_NumpadDot",
        0
    ]
]
