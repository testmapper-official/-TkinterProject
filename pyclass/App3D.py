import sys
import tkinter as tk

from keys import *
from pyclass.Canvas3D import Canvas3D


# Класс приложения
class App3D(tk.Tk):

    # Инициализация приложения
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # Жизненные переменные приложения
        self.pressTimer = None
        self.buttonTimer = None
        self.timer = None
        self.keys = set()
        self.btn = set()
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()

        # Настройка холста
        self.attributes('-fullscreen', True)
        self.canvas = Canvas3D(self, width=self.width, height=self.height)
        self.canvas.pack()

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

        self.canvas.display()
        self.timer = self.after(10, self.run)

    # Уничтожение приложения
    def destroy(self):
        sys.exit()
