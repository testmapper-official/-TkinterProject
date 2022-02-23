import tkinter as tk

from pyclass.Bullet import Bullet
from pyclass.Spider import Spider
from pyclass.Sprite import Sprite
from PIL import Image, ImageTk

from pyclass.Tree import Tree
from pyclass.Turrel import Turrel
from pyclass.Wall import Wall
from pyclass.SpriteGroup import SpriteGroup


class Canvas(tk.Canvas):

    # Инициализация холста
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        # Глобальная группа спрайтов для отображения

        self.visionGroup = SpriteGroup()

        # Получение фонового изображения
        self.background = Image.open('images/grass-tile.png')
        self.background = self.background.resize((64, 64), Image.ANTIALIAS)
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        image1 = Image.new("RGB", (width, height), (255, 255, 255))
        for i in range(width // 64 + 1):
            for j in range(height // 64 + 1):
                image1.paste(self.background, (64 * i, 64 * j))

        self.background = ImageTk.PhotoImage(image1)

    def setVisionTo(self, sprites):
        self.visionGroup.add(sprites)

    # Построение дуги круга по центру
    def create_arc_circle(self, x, y, r=1, *args, **kw):
        return super().create_arc((x - r, y - r) + (x + r, y + r) + args, kw)

    # Построение круга по центру
    def create_circle(self, x, y, r=1, *args, **kw):
        return super().create_oval((x - r, y - r) + (x + r, y + r) + args, kw)

    # Построение юнита "Паук"
    def create_spider(self, x, y, z, angle=270, spriteGroup=None):
        unit = Spider(x, y, z, angle=angle, spriteGroup=spriteGroup, master=self)
        self.setVisionTo(unit)
        return unit

    # Установить фоновое изображение
    def set_background(self):
        self.create_image(0, 0, anchor="nw", image=self.background)

    # Построение спрайта
    def create_sprite(self, x, y, z=0, size=1, angle=270, spriteGroup=None, fill='white'):
        unit = Sprite(x, y, z, size, angle=angle, spriteGroup=spriteGroup, master=self, fill=fill)
        self.setVisionTo(unit)
        return unit

    def create_tree(self, x, y, z=0, angle=270, spriteGroup=None):
        unit = Tree(x, y, z, angle=angle, spriteGroup=spriteGroup, master=self)
        self.setVisionTo(unit)
        return unit

    def create_wall(self, x, y, z=0, angle=270, spriteGroup=None):
        unit = Wall(x, y, z, angle=angle, spriteGroup=spriteGroup, master=self)
        self.setVisionTo(unit)
        return unit

    def create_turrel(self, x, y, z=0, angle=270, spriteGroup=None):
        unit = Turrel(x, y, z, angle=angle, spriteGroup=spriteGroup, master=self)
        self.setVisionTo(unit)
        return unit

    def create_bullet(self, x, y, z=0, endpos=None, angle=270, spriteGroup=None):
        unit = Bullet(x, y, z, endpos, angle=angle, spriteGroup=spriteGroup, master=self)
        self.setVisionTo(unit)
        return unit

    def display(self):
        self.visionGroup.display()
