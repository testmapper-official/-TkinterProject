import tkinter as tk


class Target(tk.Canvas):
    def __init__(self, x, y, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        print(self.coords())
        self.moveto(x, y)

        self.update()

