import math

from pyclass.Functions import *
from pyclass.Position import Position
from pyclass.Sprite import Sprite


class Bullet(Sprite):

    # Инициализация юнита "Турель"
    def __init__(self, x, y, z, endpos, angle, spriteGroup, master):
        super().__init__(x, y, z, 8, hp=1, angle=angle, spriteGroup=spriteGroup, master=master)

        self.endPosition = Position(*endpos)

    # Анимация
    def animate(self):
        self.moveTowardsAngle(15)
        if not(0 <= self.getX() <= self.canvas.master.winfo_screenwidth()) or \
                not(0 <= self.getY() <= self.canvas.master.winfo_screenheight()):
            self.destroy()

    def display(self):

        points = [(self.getX() - self.size, self.getY() - self.size // 8),
                  (self.getX(), self.getY() - self.size // 8),
                  (self.getX(), self.getY() + self.size // 8),
                  (self.getX() - self.size, self.getY() + self.size // 8)]
        self.canvas.create_polygon(rotateBy2((self.getX(), self.getY()), self.angle, points),
                                     fill='yellow', width=0)

        self.animate()

