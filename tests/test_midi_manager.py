import unittest
from src.midi_map_manager import MidiMapManager
import numpy as np

class TestMidiMapManager(unittest.TestCase):
    """test class of led_manager.py
    """

    def setUp(self):
        self.manager = MidiMapManager()

    def test_getMatIdByNoteNum(self):
        self.assertEqual( self.manager.getMatIdByNoteNum(60).tolist(), [[5, 2],[1, 8]])
        self.manager.octaves["left"] = 1
        self.assertEqual( self.manager.getMatIdByNoteNum(60).tolist(), [[3, 0],[1, 8]])

        self.manager.octaves["left"] = 0
        self.assertEqual( self.manager.getMatIdByNoteNum(60).tolist(), [[5,2],[1,8]])

        self.manager.octaves["right"] = -1
        self.assertEqual( self.manager.getMatIdByNoteNum(60).tolist(), [[5,2], [2,12]])
        self.manager.octaves["right"] = 1
        self.assertEqual( self.manager.getMatIdByNoteNum(72).tolist(), [[1,8]])

if __name__ == "__main__":
    unittest.main()
