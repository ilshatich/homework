class Color:
    red = 0
    green = 0
    blue = 0

    def __int__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b
    def toHex(self):
        return '#%02x%02x%02x' % (self.red, self.green, self.blue)

gray = Color.__int__(0, 80, 80, 80)