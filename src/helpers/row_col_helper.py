from enum import IntEnum
import numpy as np
from .midi_map import MIDI_MAP


def getMatIdByNoteNum(note):
    try:
      key_name = MIDI_MAP(note).name
      return getMatIdByName(key_name)
    except:
      return

def getMatIdByName(name):
    np_array = np.array(key_mat)
    index = np.where(np_array == name)
    return index

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
