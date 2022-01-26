class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__ (self, start):
        """create a SerialGenerator instance from start"""
        self.start_num = start - 1
        self.last_num = start - 1
    
    def generate (self):
        """increments last_num by one and returns last_num"""
        self.last_num += 1
        return self.last_num 

    def reset (self):
        """resets last_num to start_num"""
        self.last_num = self.start_num


