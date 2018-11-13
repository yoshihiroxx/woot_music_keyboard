import unittest
from src.led_manager import LedManager
from src.woot_music_keyboard import WootMusicKeyboard
import time

class TestLedManager(unittest.TestCase):
    """test class of led_manager.py
    """

    def setUp(self):
        self.w= WootMusicKeyboard()
        self.manager = LedManager(self.w.midiMapManager)

    def tearDown(self):
        self.w.reset_rgb()

    def test_init_leds(self):
        self.manager.init_leds()
        time.sleep(2)

    def test_key_shift(self):
        self.manager.key_shift(1)
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()
