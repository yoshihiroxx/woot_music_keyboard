import unittest
from src.woot_music_keyboard import WootMusicKeyboard
import time

class TestSingleWootMidiKey(unittest.TestCase):
    """test class of woot_music_keyboard.py
    """
    def setUp(self):
        self.w = WootMusicKeyboard()

    def tearDown(self):
        self.w.reset_rgb()


    def test_update(self):
        self.w.update()

    def test_set_color(self):
        self.w.rgb_direct_set_key_by_note(60, 255, 0, 0)
        time.sleep(1)
        self.w.rgb_direct_reset_key_by_note(60)
        time.sleep(0)
        self.w.rgb_direct_set_key_by_note(61, 255, 0, 0)
        time.sleep(1)
        self.w.rgb_direct_reset_key_by_note(61)
        time.sleep(1)

    def test_out_of_range(self):
        self.w.rgb_direct_set_key_by_note(150, 255, 0, 0)
        self.w.rgb_direct_reset_key_by_note(150)

    def test_set_key(self):
        time.sleep(2)
        self.w.set_key(3)
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
