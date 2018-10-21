import unittest
from woot_music_keyboard import WootMusicKeyboard

class TestSingleWootMidiKey(unittest.TestCase):
    """test class of woot_music_keyboard.py
    """
    def setUp(self):
        self.w = WootMusicKeyboard()

    def test_update(self):
        self.w.update()




if __name__ == "__main__":
    unittest.main()
