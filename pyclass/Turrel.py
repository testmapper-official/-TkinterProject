import math

from pyclass.Functions import *
from pyclass.Position import Position
from pyclass.Sprite import Sprite


class Turrel(Sprite):

    # Инициализация юнита "Турель"
    def __init__(self, x, y, z, angle, spriteGroup, master):
        super().__init__(x, y, z, 32, hp=100, angle=angle, spriteGroup=spriteGroup, master=master)

        self.attackPeriod = 0

    # Анимация
    def animate(self):
       self.attackPeriod -= 1

    def display(self):
        self.animate()

        self.displayHP()

        points = [(self.getX() - self.size // 3, self.getY() - self.size),
                  (self.getX() - self.size // 3, self.getY()),
                  (self.getX() + self.size // 3, self.getY()),
                  (self.getX() + self.size // 3, self.getY() - self.size)]
        self.canvas.create_polygon(rotateBy2((self.getX(), self.getY()), self.angle, points),
                                     fill='#131517', width=0)
        points = [(self.getX() - self.size, self.getY() - self.size // 8),
                  (self.getX(), self.getY() - self.size // 8),
                  (self.getX(), self.getY() + self.size // 8),
                  (self.getX() - self.size, self.getY() + self.size // 8)]
        self.canvas.create_polygon(rotateBy2((self.getX(), self.getY()), self.angle, points),
                                     fill='black', width=0)

        self.canvas.create_circle(self.getX(), self.getY(), self.size // 2, fill='#212023', width=0)
