import math

class SingleWootMidiKey:
    """single key to handle note on and note off"""

    def __init__(self, number, current_pressure, threshold):
        self._number = number
        self._preview_pressure = 0
        self._current_pressure = current_pressure
        self._threshold = threshold
        self._observers = {}
        self._is_triggered = False

    def on(self, name, callback):
        self._observers[name] = callback

    def update_value(self, p_pressure):
        self._current_pressure = p_pressure

        if self._is_triggered:
            if p_pressure <= 0:
                if 'noteOff' in self._observers:
                    self._observers['noteOff'](self._number, 0)
                self._is_triggered = False
            return False

        elif p_pressure >= self._threshold:
            velocity = p_pressure - self._preview_pressure
            if 'noteOn' in self._observers:
                velocity = math.floor(velocity/2)
                if velocity > 127:
                    velocity = 127
                self._observers['noteOn'](self._number, velocity)
            self._is_triggered = True

        self._preview_pressure = self._current_pressure
