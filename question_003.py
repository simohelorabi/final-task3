class InvalidConnection(Exception):
    """Triggered when we have an invalid connection."""
    pass


class Resistor():
    def __init__(self, value, left_terminal, right_terminal):
        self.value = value
        self._left_terminal = left_terminal
        self._right_terminal = right_terminal

    @property
    def left_terminal(self):
        return self._left_terminal

    @left_terminal.setter
    def left_terminal(self, value):
        if value < 0:
            raise ValueError('Value of left termainl should be non negative')
        self._left_terminal = value

    @property
    def right_terminal(self):
        return self._right_terminal

    @right_terminal.setter
    def right_terminal(self, value):
        if value < 0:
            raise ValueError('Value of right termainl should be non negative')
        self._right_terminal = value

    def check_connection(self, r):
        if self.left_terminal != r.left_terminal or self.right_terminal != r.right_terminal:
            raise InvalidConnection('Invalid connection')

    def add_in_series(self, r):
        self.check_connection(r)
        return self.value + r.value

    def add_in_parallel(self, r):
        self.check_connection(r)
        return 1 / (1 / self.value + 1 / r.value)

    def __str__(self):
        return f'Resistor({self.value},{self.left_terminal},{self.right_terminal})'


def main():
    # Test in series.
    r1 = Resistor(10, 10, 11)
    r2 = Resistor(12, 10, 11)
    print(f'Adding in series {r1} and {r2} = {r1.add_in_series(r2)} kOhms')

    # Test in parallel.
    r1 = Resistor(10, 10, 11)
    r2 = Resistor(12, 10, 11)
    print(f'Adding in parallel {r1} and {r2} = {r1.add_in_parallel(r2)} kOhms')


if __name__ == '__main__':
    main()
