class SpriteGroup:

    def __init__(self, sprites=None):
        if not sprites:
            sprites = []

        self.sprites = sprites

    # Добавление спрайтов, группы спрайтов внутрь группы спрайтов
    def add(self, other):
        try:
            if other.displayInfo() == "Sprite":
                self.sprites.append(other)
            elif other.displayInfo() == "SpriteGroup":
                for sprite in other.sprites:
                    if sprite not in self.sprites:
                        self.sprites.append(sprite)
            return True
        except TypeError:
            pass
        except AttributeError:
            pass
        return False

    # Удаление спрайтов, группы спрайтов внутрь группы спрайтов
    def remove(self, other):
        try:
            if other.displayInfo() == "Sprite":
                if other in self.sprites:
                    self.sprites.remove(other)
            elif other.displayInfo() == "SpriteGroup":
                for sprite in other.sprites:
                    if sprite in self.sprites:
                        self.sprites.remove(sprite)
            return True
        except ValueError:
            pass
        except TypeError:
            pass
        except AttributeError:
            pass
        return False

    def getArray(self):
        return self.sprites

    # Проверка столкновения группы с спрайтом. Если истинно, то возвращает столкнувшиеся спрайты группы.
    def isCollided(self, other):
        lst = []
        for sprite in self.sprites:
            if other.isCollided(sprite):
                lst.append(sprite)
        return lst if len(lst) > 0 else None

    # Проверка столкновения группы с группой. Если истинно, то выполняет функцию для столкнувшихся спрайтов.
    # Возвращает логическое выражение, столкнулись ли группы.
    def isCollidedGroup(self, other, doOne=None, doTwo=None):
        for sprite in self.sprites:
            for other_sprite in other.sprites:
                if other_sprite.isCollided(sprite):
                    if doOne:
                        doOne(sprite)
                    if doTwo:
                        doTwo(other_sprite)

    def doGroup(self, do):
        for sprite in self.sprites:
            do(sprite)



    # Отображение всех спрайтов внутри группы на холсте
    def display(self):
        self.sprites.sort(key=lambda x: (x.getZ(), x.getY()))
        for sprite in self.sprites:
            sprite.display()

    # Отображение названия класса
    def displayInfo(self):
        return "SpriteGroup"
