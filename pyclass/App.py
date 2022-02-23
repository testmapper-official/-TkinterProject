import math
import random
import sys
import tkinter as tk

from PIL import Image, ImageTk

from keys import *
from pyclass.Canvas import Canvas
from pyclass.Functions import *
from pyclass.Position import Position
from pyclass.SpriteGroup import SpriteGroup


# Класс приложения
class App(tk.Tk):

    # Инициализация приложения
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # Жизненные переменные приложения
        self.pressTimer = None
        self.buttonTimer = None
        self.timer = None
        self.keys = set()
        self.btn = set()
        self.difficulty = 1
        self.summonTime = 300

        # Настройка холста
        self.attributes('-fullscreen', True)
        self.canvas = Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight(), bg='white')
        self.canvas.pack()

        # Группы спрайтов
        self.enemyGroup = SpriteGroup()
        self.blockGroup = SpriteGroup()
        self.effectGroup = SpriteGroup()
        self.bulletGroup = SpriteGroup()
        self.wallGroup = SpriteGroup()

        for i in range(11):
            a = self.canvas.create_tree(random.randint(200, self.winfo_screenwidth() - 400),
                                        random.randint(100, self.winfo_screenheight() - 100),
                                        spriteGroup=self.blockGroup)

        for i in range(self.winfo_screenheight() // 64 + 1):
            a = self.canvas.create_wall(self.winfo_screenwidth() - 32, i * 64, spriteGroup=self.wallGroup)

        # Создание главного героя

        self.mainHero = self.canvas.create_turrel(self.winfo_screenwidth() - 48, self.winfo_screenheight() // 2, 20)
        self.mainHero.setAngle(0)

        self.bind("<KeyPress>", self.onPress)
        self.bind("<KeyRelease>", self.onRelease)
        self.bind("<ButtonPress>", self.onMouseClick)
        self.bind("<ButtonRelease>", self.onMouseRelease)

        self.timer = self.after(10, self.run)
        # Старт жизненного цикла
        self.mainloop()

    def onMouseClick(self, event):
        if event.num in self.btn:
            return
        self.btn.add(event.num)
        if not self.buttonTimer:
            self.buttonTimer = self.after(10, self.onMouseEvent)

    def onMouseRelease(self, event):
        if event.num not in self.btn:
            return
        self.btn.discard(event.num)

    def onMouseEvent(self):

        if not self.btn:
            self.after_cancel(self.buttonTimer)
            self.buttonTimer = None
            return

        if LEFT_BTN in self.btn and self.mainHero.attackPeriod <= 0:
            self.mainHero.attackPeriod = random.randint(3, 7)
            cursor = self.cursor()
            pt = polarOffsetBy2((self.mainHero.getX(), self.mainHero.getY()),
                                self.mainHero.size + 8, self.mainHero.angle + 180 + random.randint(-10, 10))
            self.canvas.create_bullet(pt[0], pt[1], 0, cursor, angle=self.mainHero.angle + 180,
                                      spriteGroup=self.bulletGroup)

        self.buttonTimer = self.after(10, self.onMouseEvent)

    # Регистрация нажатия клавиш, побочный поток
    def onPress(self, event):
        if event.keycode in self.keys:
            return
        self.keys.add(event.keycode)
        if not self.pressTimer:
            self.pressTimer = self.after(10, self.onKeyEvent)

    # Регистрация отпускания клавиш, побочный поток
    def onRelease(self, event):
        if event.keycode not in self.keys:
            return
        self.keys.discard(event.keycode)

    # Управление клавиш, побочный поток
    def onKeyEvent(self):
        if not self.keys:
            self.after_cancel(self.pressTimer)
            self.pressTimer = None
            return

        if KEY_ESCAPE in self.keys:
            self.destroy()

        self.pressTimer = self.after(10, self.onKeyEvent)

    def cursor(self):
        return self.winfo_pointerx() - self.winfo_rootx(), self.winfo_pointery() - self.winfo_rooty()

    # Жизненный цикл приложения
    def run(self):
        self.canvas.delete("all")
        self.canvas.set_background()

        if self.mainHero.hp <= 0:
            self.destroy()

        # Спавн монстров
        self.summonTime -= 1

        if self.summonTime <= 0:
            print(self.difficulty)
            self.summonTime = random.randint(666, 999)
            self.difficulty += 0.1
            if self.difficulty > 5:
                self.summonTime -= max(400, 50 * (self.difficulty - 5))
            for i in range(min(13, int(self.difficulty))):
                x, y = random.randint(-200, -25), random.randint(50, self.winfo_screenheight() - 50)

                self.canvas.create_spider(x, y, 0, angle=0, spriteGroup=self.enemyGroup)



        # Движение монстров

        self.enemyGroup.doGroup(lambda x: x.moveTowardsAngle(1))

        for sprite in self.enemyGroup.getArray():
            if sprite.getX() >= self.winfo_screenwidth() - 32:
                sprite.destroy()
                self.mainHero.damage(1)


        # Установка угла наклона турели
        angle = self.cursor()
        angle = math.degrees(math.atan2(self.mainHero.getY() - angle[1], self.mainHero.getX() - angle[0]))

        dangle = angle - self.mainHero.angle

        if dangle > 0:
            self.mainHero.setAngle(self.mainHero.angle + 1)
        if dangle < 0:
            self.mainHero.setAngle(self.mainHero.angle - 1)

        # Столкновение групп спрайтов
        self.bulletGroup.isCollidedGroup(self.blockGroup, lambda x: x.destroy(), lambda x: x.damage(1))
        self.bulletGroup.isCollidedGroup(self.enemyGroup, lambda x: x.destroy(), lambda x: x.damage(1))

        self.canvas.display()

        print(self.enemyGroup.getArray())
        self.timer = self.after(10, self.run)

    # Уничтожение приложения
    def destroy(self):
        sys.exit()