import rtmidi

def main():

    midiout = rtmidi.MidiOut()
    available_ports = midiout.get_ports()
    print(available_ports)



if __name__ == '__main__':
    main()
