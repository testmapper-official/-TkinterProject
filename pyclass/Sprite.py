import math

from pyclass.Position import Position


class Sprite:

    # Инициализация спрайта
    def __init__(self, x, y, z=0, size=1, hp=1, angle=270, spriteGroup=None, master=None, fill=None):
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
        self.always_show_hp_indicator = False

        if spriteGroup:
            spriteGroup.add(self)

    def showDisplayHP(self):
        self.always_show_hp_indicator = True

    def hideDisplayHP(self):
        self.always_show_hp_indicator = False

    def displayHP(self):
        self.canvas.create_rectangle(self.getX() - self.size,
                                     self.getY() - self.size - 8,
                                     self.getX() - self.size + self.size * 2 * self.hp // self.maxhp,
                                     self.getY() - self.size - 16,
                                     width=0, fill='red')
        self.canvas.create_rectangle(self.getX() - self.size, self.getY() - self.size - 8,
                                     self.getX() + self.size, self.getY() - self.size - 16,
                                     width=3)

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
        self.position.moveBy(dist * math.cos(math.radians(self.angle)), dist * math.sin(math.radians(self.angle)))

    # Установить позицию спрайта
    def moveTo(self, x, y):
        self.position.moveTo(x, y)

    # Установить анимацию спрайта
    def setAnimation(self, string):
        global _animations
        self.animation = string
        if string not in self._animations:
            self.animation = "stand"

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

        return xRange <= self.size + other.size and yRange <= self.size + other.size

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            self.destroy()

    # Отображение названия класса
    def displayInfo(self):
        return "Sprite"
