import sys
import tkinter as tk

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
        self.difficulty = 1
        self.summonTime = 300

        # Настройка приложения
        self.geometry('1000x600')
        self.title('Test App')
        # текст
        self.lbl = tk.Label(self, text='a=', font=('Calibri', 16))
        self.lbl.grid(column=0, row=0)

        self.lbl1 = tk.Label(self, text='b=', font=('Calibri', 16))
        self.lbl1.grid(column=0, row=1)

        self.lbl2 = tk.Label(self, text='c=', font=('Calibri', 16))
        self.lbl2.grid(column=0, row=2)

        self.lbl3 = tk.Label(self, text='X1=', font=('Calibri', 16))
        self.lbl3.grid(column=0, row=3)

        self.lbl4 = tk.Label(self, text='X2=', font=('Calibri', 16))
        self.lbl4.grid(column=0, row=4)

        self.lbl5 = tk.Label(self, text=' ', font=('Calibri', 16))
        self.lbl5.grid(column=1, row=3)

        self.lbl6 = tk.Label(self, text=' ', font=('Calibri', 16))
        self.lbl6.grid(column=1, row=4)

        # кнопки
        self.btn = tk.Button(self, text='посчитать', bg='purple', fg='pink', command=self.summa)
        self.btn.grid(column=3, row=0)

        self.btn1 = tk.Button(self, text='очистить', bg='purple', fg='pink', command=self.delete)
        self.btn1.grid(column=3, row=2)

        # вводить текст
        self.txt = tk.Entry(self, width=50)
        self.txt.grid(column=1, row=0)

        self.txt1 = tk.Entry(self, width=50)
        self.txt1.grid(column=1, row=1)

        self.txt2 = tk.Entry(self, width=50)
        self.txt2.grid(column=1, row=2)

        # Реализация управления клавиатурой и мышью
        self.bind("<KeyPress>", self.onKeyPress)
        self.bind("<KeyRelease>", self.onKeyRelease)
        self.bind("<ButtonPress>", self.onMousePress)
        self.bind("<ButtonRelease>", self.onMouseRelease)

        # Запуск жизненного цикла
        self.timer = self.after(10, self.run)
        # Запуск приложения
        self.mainloop()

    def summa(self):
        a = int(self.txt.get())
        b = int(self.txt1.get())
        c = int(self.txt2.get())
        if a == 0:
            if b == 0:
                if c == 0:
                    res = ('ANY')
                else:
                    res = ('NO')
                self.lbl5["text"] = str(res)
                self.lbl6["text"] = str(res)
            else:
                self.lbl5["text"] = str(round((-1 * (c / b)), 4))
        else:
            D = (b ** 2) - 4 * a * c
            if D < 0:
                res = ('NO')
                self.lbl5["text"] = str(res)
                self.lbl6["text"] = str(res)
            else:
                x1 = (-b + (D ** 0.5)) / (2 * a)
                x2 = (-b - (D ** 0.5)) / (2 * a)
                self.lbl5["text"] = str(round(x1, 4))
                self.lbl6["text"] = str(round(x2, 4))

    def delete(self):
        self.lbl5["text"] = ""
        self.lbl6["text"] = ""
        self.txt.delete(0, tk.END)
        self.txt1.delete(0, tk.END)
        self.txt2.delete(0, tk.END)

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
