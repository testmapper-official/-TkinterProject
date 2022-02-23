import math

from PIL import Image, ImageTk

from pyclass.Sprite import Sprite


class Tree(Sprite):

    # Инициализация юнита "Дерево"
    def __init__(self, x, y, z, angle, spriteGroup, master):
        super().__init__(x, y, z, 32, hp=400, angle=angle, spriteGroup=spriteGroup, master=master)

        self.image = Image.open('images/tree2.png')
        ratio = self.image.size[1] / self.image.size[0]
        self.image = self.image.resize((self.size * 4, int(self.size * 4 * ratio)), Image.ANTIALIAS)
        self.imageTk = ImageTk.PhotoImage(self.image)

    def display(self):
        self.canvas.create_image(self.getX() - self.size * 1.8,
                                 self.getY() - self.image.size[1] + self.size // 1.6, anchor="nw",
                                 image=self.imageTk)

        """self.canvas.create_rectangle(self.getX() - self.size, self.getY() - self.size,
                                     self.getX() + self.size, self.getY() + self.size)"""
