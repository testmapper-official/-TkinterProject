import tkinter as tk
from pyclass.Canvas import Canvas
import sys


# Класс приложения
class AppGraph(tk.Tk):

    # Инициализация приложения
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.timer = None

        # Настройка холста
        self.canvas = Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight(), bg='white')
        self.canvas.pack()
        self.canvas.bind('<Button-1>', lambda x, amount=0.01: self.redraw(amount))
        self.canvas.bind('<ButtonRelease-1>', lambda x: self.after_cancel(self.timer))
        self.canvas.bind('<Button-3>', lambda x, amount=-0.01: self.redraw(amount))
        self.canvas.bind('<ButtonRelease-3>', lambda x: self.after_cancel(self.timer))

        self.zoom = 1

        # Изображение
        self.draw()

        # Старт жизненного цикла
        self.canvas.mainloop()

    def redraw(self, amount=0):
        if self.timer:
            self.after_cancel(self.timer)
        if self.zoom > 0.1 and amount < 0:
            self.zoom += amount
        elif self.zoom < 3 and amount > 0:
            self.zoom += amount
        self.canvas.delete("all")
        self.draw()
        self.timer = self.after(10, lambda: self.redraw(amount))

    # Отображение объектов на холсте
    def draw(self):
        h = self.winfo_screenheight()
        w = self.winfo_screenwidth()
        x0, y0 = w * 0.5, h * 0.5
        cell = (int(100 * self.zoom), int(100 * self.zoom))

        y = lambda x: 1 / x
        points = []
        for i in range(-w // 2, w // 2):
            try:
                points.append((x0 + i, y0 - y(i / cell[0]) * cell[1]))
            except:
                pass

        for i in range(-w // cell[0], w // cell[0]):
            self.canvas.create_line(x0 + i * cell[0], 0, x0 + i * cell[0], h, width=0, fill='#aaaaaa')
        for i in range(-h // cell[1], h // cell[1]):
            self.canvas.create_line(0, y0 + i * cell[1], w, y0 + i * cell[1], width=0, fill='#aaaaaa')

        self.canvas.create_line(0, y0, w, y0, arrowshape='10 20 10', arrow=tk.LAST, width=2, fill='gray')
        self.canvas.create_line(x0, h, x0, 0, arrowshape='10 20 10', arrow=tk.LAST, width=2, fill='gray')

        self.canvas.create_line(points, fill='black')

    def destroy(self):
        super().destroy()
        sys.exit()
