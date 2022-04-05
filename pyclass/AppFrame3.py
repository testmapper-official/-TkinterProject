import sys
import tkinter
from tkinter import Tk, Button, BooleanVar, IntVar, messagebox
from tkinter.ttk import Combobox, Checkbutton, Radiobutton

from keys import *


# Класс приложения
class AppFrame(Tk):

    # Инициализация приложения
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # Жизненные переменные приложения
        self.pressTimer = None
        self.buttonTimer = None
        self.timer = None
        self.keys = set()
        self.mouse = set()
        self.difficulty = 1
        self.summonTime = 300

        self.isChecked = BooleanVar()
        self.isChecked.set(False)

        self.selected = IntVar()
        self.selected2 = IntVar()

        # Настройка приложения
        self.geometry('1000x600')
        self.title('Test App')

        # Основной макет
        self.combo = Combobox(self)
        self.combo['values'] = (1, 2, 3, 'какой-то текст', 'poooooooooooooooooooooooooooooooooooooower')
        self.combo.current(1)
        self.combo.grid(column=0, row=0)

        self.button = Button(self, text="Click me", command=self.onClick)
        self.button.grid(column=1, row=0)

        self.cButton = Checkbutton(self, text="Mark me", var=self.isChecked)
        self.cButton.grid(column=2, row=0)

        self.rButton = Radiobutton(self, text="Mark me", value=1, variable=self.selected)
        self.rButton.grid(column=3, row=0)
        self.rButton2 = Radiobutton(self, text="Mark me", value=2, variable=self.selected)
        self.rButton2.grid(column=3, row=1)

        self.rButton3 = Radiobutton(self, text="Mark me", value=1, variable=self.selected2)
        self.rButton3.grid(column=4, row=0)
        self.rButton4 = Radiobutton(self, text="Mark me", value=2, variable=self.selected2)
        self.rButton4.grid(column=4, row=1)


        # Реализация управления клавиатурой и мышью
        self.bind("<KeyPress>", self.onKeyPress)
        self.bind("<KeyRelease>", self.onKeyRelease)
        self.bind("<ButtonPress>", self.onMousePress)
        self.bind("<ButtonRelease>", self.onMouseRelease)

        # Запуск жизненного цикла
        self.timer = self.after(10, self.run)
        # Запуск приложения
        self.mainloop()

    def onClick(self):
        messagebox.showinfo('Держи бiмбу', f'{self.isChecked.get()} {self.selected.get()} {self.selected2.get()}')

    # Регистрация нажатия кнопки мыши, побочный поток
    def onMousePress(self, event):
        if event.num in self.mouse:
            return
        self.mouse.add(event.num)
        if not self.buttonTimer:
            self.buttonTimer = self.after(10, self.onMouseEvent)

    # Регистрация отпускания кнопки мыши, побочный поток
    def onMouseRelease(self, event):
        if event.num not in self.mouse:
            return
        self.mouse.discard(event.num)

    # Управление мышью, побочный поток
    def onMouseEvent(self):

        if not self.mouse:
            self.after_cancel(self.buttonTimer)
            self.buttonTimer = None
            return

        self.buttonTimer = self.after(10, self.onMouseEvent)

    # Регистрация нажатия клавиш, побочный поток
    def onKeyPress(self, event):
        if event.keycode in self.keys:
            return
        self.keys.add(event.keycode)
        if not self.pressTimer:
            self.pressTimer = self.after(10, self.onKeyEvent)

    # Регистрация отпускания клавиш, побочный поток
    def onKeyRelease(self, event):
        if event.keycode not in self.keys:
            return
        self.keys.discard(event.keycode)

    # Управление клавишами, побочный поток
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
        self.timer = self.after(10, self.run)

    # Уничтожение приложения
    def destroy(self):
        sys.exit()
