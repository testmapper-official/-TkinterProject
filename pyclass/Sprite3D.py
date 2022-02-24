import math

from pyclass.Position import Position


class Sprite3D:

    # Инициализация спрайта
    def __init__(self, x, y, z, size, hp=1, angle=270, spriteGroup=None, master=None, fill=None):
        self.canvas = master
        self.position = Position(x, y, z)
        self._animations = ["stand"]
        self.angle = angle
        self.size = size
        self.maxhp = hp
        self.hp = hp
        self.spriteGroup = spriteGroup
        self.animation = "stand"
        self.fill = fill

        if spriteGroup:
            spriteGroup.add(self)

    # Отображение спрайта
    def display(self):
        self.canvas.create_rectangle(self.getX() - self.size, self.getY() - self.size,
                                     self.getX() + self.size, self.getY() + self.size,
                                     fill=self.fill)

    # Анимация
    def animate(self):
        pass

    # Переместить спрайт по координатам
    def move(self, x, y):
        self.position.moveBy(x, y)

    # Переместить спрайт относительно угла
    def moveTowardsAngle(self, dist):
        pass

    # Установить позицию спрайта
    def moveTo(self, x, y, z):
        self.position.moveTo(x, y, z)

    # Установить поворот спрайта на указанный градус
    def setAngle(self, angle):
        self.angle = angle

    # Повернуть спрайта на указанный градус
    def moveAngleBy(self, angle):
        self.angle += angle

    # Получить координату X позиции спрайта
    def getX(self):
        return self.position.x

    # Получить координату Y позиции спрайта
    def getY(self):
        return self.position.y

    # Получить координату Z позиции спрайта
    def getZ(self):
        return self.position.z

    # Уничтожение спрайта
    def destroy(self):
        if self.spriteGroup:
            self.spriteGroup.remove(self)
        self.canvas.visionGroup.remove(self)
        return True

    # Проверка столкновения спрайта с другим
    def isCollided(self, other):
        xRange = abs(self.getX() - other.getX())
        yRange = abs(self.getY() - other.getY())
        zRange = abs(self.getZ() - other.getZ())

        return xRange + yRange + zRange <= 3 * (self.size + other.size)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            self.destroy()

    # Отображение названия класса
    def displayInfo(self):
        return "Sprite"
