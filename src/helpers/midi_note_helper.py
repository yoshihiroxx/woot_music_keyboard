from .midi_map import MIDI_MAP
from .scan_code import SCAN_CODE


def getMidiNoteByScanCode(scan_code):
    return MIDI_MAP[SCAN_CODE(scan_code).name].value

def getKeyNameByScanCode(scan_code):
    return SCAN_CODE(scan_code).name