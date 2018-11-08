import unittest
from src.helpers.midi_note_helper import getMidiNoteByScanCode


class TestMidiNoteHelper(unittest.TestCase):
    """test class of midi_note_helper
    """

    def test_get_midi_by_scan_code(self):
        note_num = getMidiNoteByScanCode(24)# midldle c4(60)
        self.assertEqual(note_num, 60)

if __name__ == "__main__":
    unittest.main()
