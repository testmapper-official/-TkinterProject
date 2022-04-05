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
        self.geometry('182x250')
        self.title('Test App')
        self.text_result = tk.StringVar()

        self.result_field = tk.Entry(self, width=20, font=('Agency FB', 16), textvariable=self.text_result)
        self.result_field.grid(column=0, row=0, columnspan=8)
        self.result_field.config(state='disabled')
        lst = "123456789"
        self.numpad = []
        for i in range(len(lst)):
            Button = tk.Button(self, text=lst[i], font=('Agency FB', 16), bg='purple', fg='pink',
                                      command=lambda text=lst[i]: self.clicked(text), width=5)
            Button.grid(column=i % 3, row=2 + i // 3)
            self.numpad.append(Button)
        # ±
        self.btn_equal = tk.Button(self, text='±', font=('Agency FB', 16), bg='purple', fg='pink',
                                   command=lambda: self.clicked("±"), width=5)
        self.btn_equal.grid(column=0, row=5)
        # 0
        Button = tk.Button(self, text="0", font=('Agency FB', 16), bg='purple', fg='pink',
                           command=lambda text="0": self.clicked(text), width=5)
        Button.grid(column=1, row=5)
        self.numpad.append(Button)
        # =
        self.btn_equal = tk.Button(self, text='=', font=('Agency FB', 16), bg='purple', fg='pink',
                                   command=lambda: self.clicked("="), width=5)
        self.btn_equal.grid(column=2, row=5)
        # Ресет
        self.btn_reset = tk.Button(self, text='CE', font=('Agency FB', 16), bg='purple', fg='pink',
                                   command=lambda: self.clicked("RESET"), width=5)
        self.btn_reset.grid(column=2, row=1)
        # +
        self.btn_plus = tk.Button(self, text='+', font=('Agency FB', 16), bg='purple', fg='pink',
                                    command=lambda: self.clicked("+"), width=5)
        self.btn_plus.grid(column=3, row=2)
        # -
        self.btn_minus = tk.Button(self, text='-', font=('Agency FB', 16), bg='purple', fg='pink',
                                    command=lambda: self.clicked("-"), width=5)
        self.btn_minus.grid(column=3, row=3)
        # *
        self.btn_multiplier = tk.Button(self, text='*', font=('Agency FB', 16), bg='purple', fg='pink',
                                    command=lambda: self.clicked("*"), width=5)
        self.btn_multiplier.grid(column=3, row=4)
        # /
        self.btn_divide = tk.Button(self, text='/', font=('Agency FB', 16), bg='purple', fg='pink',
                                    command=lambda: self.clicked("/"), width=5)
        self.btn_divide.grid(column=3, row=5)

        # Реализация управления клавиатурой и мышью
        self.bind("<KeyPress>", self.onKeyPress)
        self.bind("<KeyRelease>", self.onKeyRelease)
        self.bind("<ButtonPress>", self.onMousePress)
        self.bind("<ButtonRelease>", self.onMouseRelease)

        # Запуск жизненного цикла
        self.timer = self.after(10, self.run)
        # Запуск приложения
        self.mainloop()

    def clicked(self, text):
        if text == "RESET" or self.text_result.get() == "ERROR":
            self.text_result.set("")
        elif text == "±":
            pass
        elif text != "=":
            self.text_result.set(self.text_result.get() + text)
        else:
            try:
                self.text_result.set(eval(self.text_result.get()))
            except:
                self.text_result.set("ERROR")

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
