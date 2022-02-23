import math

from PIL import Image, ImageTk

from pyclass.Sprite import Sprite


class Wall(Sprite):

    # Инициализация юнита "Стена"
    def __init__(self, x, y, z, angle, spriteGroup, master):
        super().__init__(x, y, z, 64, hp=10, angle=angle, spriteGroup=spriteGroup, master=master)

        self.image = Image.open('images/wall.png')
        ratio = self.image.size[1] / self.image.size[0]
        self.image = self.image.resize((self.size * 2, int(self.size * 2 * ratio)), Image.ANTIALIAS)
        self.imageTk = ImageTk.PhotoImage(self.image)

    def display(self):
        self.canvas.create_image(self.getX() - self.size, self.getY() - self.image.size[1], anchor="nw", image=self.imageTk)
