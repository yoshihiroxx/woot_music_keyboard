import unittest
from src.single_woot_midi_key import SingleWootMidiKey

class TestSingleWootMidiKey(unittest.TestCase):
    """test class of single_woot_midi_key.py
    """

    def test_init(self):
        s = SingleWootMidiKey(57,127, 200)

    def test_addNoteOn(self):

        def noteOnHandler(num, velocity):
            print ('got a note on ', 'num:', num, 'velocity', velocity)

        s = SingleWootMidiKey(57,2, 200)
        s.updateValue(100)
        s.addNoteOnObserver( callback=noteOnHandler )

        s.updateValue(100)
        s.updateValue(201)
        s.updateValue(221)

    def test_addNoteOff(self):
        def noteOffHandler(num, velocity):
            print ('got a note off ', 'num:', num, 'velocity', velocity)
        s = SingleWootMidiKey(57,2, 200)
        s.addNoteOffObserver( callback=noteOffHandler )
        s.updateValue(100)
        s.updateValue(250)
        s.updateValue(0)
        s.updateValue(0)
        s.updateValue(0)



if __name__ == "__main__":
    unittest.main()
