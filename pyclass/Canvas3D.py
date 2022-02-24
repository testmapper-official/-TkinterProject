import tkinter as tk

from pyclass.Sprite3D import Sprite3D
from pyclass.SpriteGroup import SpriteGroup


class Canvas3D(tk.Canvas):

    # Инициализация холста
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        # Глобальная группа спрайтов для отображения
        self.visionGroup = SpriteGroup()

    # Добавить спрайт в группу спрайтов для отображения
    def setVisionTo(self, sprites):
        self.visionGroup.add(sprites)

    # Построение дуги круга по центру
    def create_arc_circle(self, x, y, r=1, *args, **kw):
        return super().create_arc((x - r, y - r) + (x + r, y + r) + args, kw)

    # Построение круга по центру
    def create_circle(self, x, y, r=1, *args, **kw):
        return super().create_oval((x - r, y - r) + (x + r, y + r) + args, kw)

    # Построение спрайта
    def create_sprite(self, x, y, z=0, size=1, angle=270, spriteGroup=None, fill='white'):
        unit = Sprite3D(x, y, z, size, hp=1, angle=angle, spriteGroup=spriteGroup, master=self, fill=fill)
        self.setVisionTo(unit)
        return unit

    def display(self):
        self.visionGroup.display()
