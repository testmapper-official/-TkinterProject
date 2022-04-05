import json
import sys
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

from pyclass.Dialog import Dialog
from keys import *


# Класс приложения
class AppFrame(tk.Tk):

    # Инициализация приложения
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        # Жизненные переменные приложения
        self.pressTimer = None
        self.buttonTimer = None
        self.timer = None
        self.keys = set()
        self.mouse = set()
        self.total = 0

        self.var = tk.IntVar()



        # Настройка приложения
        self.geometry('1000x600')
        self.title('Test App')

        # Основной макет

        self.res = tk.Label(self, text='123')
        self.res.grid(column=0, row=0)

        self.QA = None
        self.QAs = []
        with open("data/questions.json", "r", encoding='utf-8') as f:
            self.QA = json.load(f)

        for object in self.QA:
            self.notAnswer = True
            type = object["type"]
            question = object["question"]
            answer = object["answer"]
            var = None
            if type != "Entry":
                var = object["var"]
            self.QAs.append(Dialog(self, type, question, answer, var))

        self.QAs[0].grid(column=0, row=0)

        # Реализация управления клавиатурой и мышью
        self.bind("<KeyPress>", self.onKeyPress)
        self.bind("<KeyRelease>", self.onKeyRelease)
        self.bind("<ButtonPress>", self.onMousePress)
        self.bind("<ButtonRelease>", self.onMouseRelease)

        # Запуск жизненного цикла
        self.timer = self.after(10, self.run)
        # Запуск приложения
        self.mainloop()

    def next(self):
        if len(self.QAs) == 0:
            self.res['text'] = f'Вы набрали {self.total} из {len(self.QA)}!'
            return
        self.QAs[0].grid(column=0, row=0)

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
