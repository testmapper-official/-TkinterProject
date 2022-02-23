class Position:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def moveBy(self, x, y, z=0):
        self.x += x
        self.y += y

    def moveTo(self, x, y, z=None):
        self.x = x
        self.y = y
        if z:
            self.z = z
