class Resistor:
    def __init__(self, value, left_terminal, right_terminal):
        self.value = value
        self.left_terminal = left_terminal
        self.right_terminal = right_terminal

    # getter method
    def left_terminal(self):
        return self.left_terminal

    # setter method
    def left_terminal(self, value):
        if value < 0:
            raise ValueError("Value should be negative ")
        self.left_terminal = value

    # getter method
    def right_terminal(self):
        return self.right_terminal

    # setter method
    def right_terminal(self, value):
        if value < 0:
            raise ValueError("Value should be negative ")
        self.right_terminal = value

    # check the connectin in left terminal and right terminal
    def check_connection(self, resistor):
        if not (self.left_terminal == resistor.left_terminal) or not (
                self.right_terminal == resistor.right_terminal):
            print('Invalid connection')

    def add_in_series(self, resistor):
        self.check_connection(resistor)
        return self.value + resistor.value

    def add_in_parallel(self, resistor):
        self.check_connection(resistor)
        return 1 / (1 / self.value + 1 / resistor.value)


# object of the class
resistor1 = Resistor(3, 2, 4)  #(8, 16, 10)
resistor2 = Resistor(3, 2, 4)  #(4, 6, 10)

series_connection = resistor1.add_in_series(resistor2)
print(f"series connection : {series_connection} in Kohms")
parallel_connection = resistor1.add_in_parallel(resistor2)
print(f"parallel_connection : {parallel_connection} in Kohms")