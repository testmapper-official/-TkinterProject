import math

from pyclass.Sprite import Sprite


class Spider(Sprite):

    # Инициализация юнита "Паук"
    def __init__(self, x, y, z, angle, spriteGroup, master):
        super().__init__(x, y, z, 25, hp=10, angle=angle, spriteGroup=spriteGroup, master=master)

        self.bodySpeed = 3
        self.posDif = 0.45
        self.pos = 0
        self._animations = ["stand", "move", "attack"]
        self.animation = 'move'

    # Левая передняя точка
    def getForwardLeft(self):
        dx = self.size * (math.cos(math.radians(self.angle - 90)) + math.cos(math.radians(self.angle)))
        dy = self.size * (math.sin(math.radians(self.angle - 90)) + math.sin(math.radians(self.angle)))
        if self.animation == 'move':
            dx -= self.pos * math.cos(math.radians(self.angle))
            dy -= self.pos * math.sin(math.radians(self.angle))
        return self.getX() + dx, self.getY() - dy

    # Левая передняя точка
    def getForwardRight(self):
        dx = self.size * (math.cos(math.radians(self.angle + 90)) + math.cos(math.radians(self.angle)))
        dy = self.size * (math.sin(math.radians(self.angle + 90)) + math.sin(math.radians(self.angle)))
        if self.animation == 'move':
            dx += self.pos * math.cos(math.radians(self.angle))
            dy += self.pos * math.sin(math.radians(self.angle))
        return self.getX() + dx, self.getY() - dy

    # Левая задняя точка
    def getBackwardLeft(self):
        dx = self.size * (math.cos(math.radians(self.angle - 90)) + math.cos(math.radians(self.angle - 180)))
        dy = self.size * (math.sin(math.radians(self.angle - 90)) + math.sin(math.radians(self.angle - 180)))
        if self.animation == 'move':
            dx -= self.pos * math.cos(math.radians(self.angle))
            dy -= self.pos * math.sin(math.radians(self.angle))
        return self.getX() + dx, self.getY() - dy

    # Правая задняя точка
    def getBackwardRight(self):
        dx = self.size * (math.cos(math.radians(self.angle + 90)) + math.cos(math.radians(self.angle - 180)))
        dy = self.size * (math.sin(math.radians(self.angle + 90)) + math.sin(math.radians(self.angle - 180)))
        if self.animation == 'move':
            dx += self.pos * math.cos(math.radians(self.angle))
            dy += self.pos * math.sin(math.radians(self.angle))
        return self.getX() + dx, self.getY() - dy

    # Основное тело
    def getBody(self):
        # x * x + y * y = 8

        return self.getX() + self.pos * math.cos(math.radians(self.angle + 90)), self.getY() - self.pos * math.sin(
            math.radians(self.angle + 90))

    # Анимация
    def animate(self):
        if self.pos >= 8 and self.posDif == 0.45:
            self.posDif *= -1
        elif self.pos <= -8 and self.posDif == -0.45:
            self.posDif *= -1
        self.pos += self.posDif

    def display(self):
        # Анимация
        if self.animation == 'move':
            self.animate()
        else:
            self.pos = 0

        if self.hp != self.maxhp or self.always_show_hp_indicator:
            self.displayHP()
        # Передние ноги
        self.canvas.create_line(self.getForwardLeft(), self.getBody(), width=2, fill='black')
        self.canvas.create_line(self.getForwardRight(), self.getBody(), width=2, fill='black')
        # Задние ноги
        self.canvas.create_line(self.getBackwardLeft(), self.getBody(), width=2, fill='black')
        self.canvas.create_line(self.getBackwardRight(), self.getBody(), width=2, fill='black')
        # Основное тело
        self.canvas.create_circle(self.getBody()[0], self.getBody()[1], 8, width=1, fill='black')
