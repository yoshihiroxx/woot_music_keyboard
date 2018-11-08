import sys, os


base_path = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(base_path, '..\\src')
sys.path.append(src_path)
from woot_music_keyboard import WootMusicKeyboard

import rtmidi


def main():
    woot_music_keyboard = WootMusicKeyboard()

    midiout = rtmidi.MidiOut()
    available_ports = midiout.get_ports()
    print(available_ports)
    if available_ports:

        # select a port you want to send midi messages
        midiout.open_port(7)

    else:
        midiout.open_virtual_port("My virtual output")

    def noteOnHandler(note, vel):
        note_on = [0x90, note, vel]
        midiout.send_message(note_on)
        print('note on ', note, vel)

    woot_music_keyboard.on('noteOn', noteOnHandler)


    def noteOffHandler(note, vel):
        note_off = [0x80, note, vel]
        midiout.send_message(note_off)
        print('noteoff ',note, vel)

    woot_music_keyboard.on('noteOff', noteOffHandler)


    while (1):
        woot_music_keyboard.update()


if __name__ == '__main__':
    main()
