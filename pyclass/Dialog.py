import tkinter as tk
import tkinter.ttk as ttk


class Dialog(tk.Frame):

    def __init__(self, master, type, question, answer, var=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.type = type
        self.question = question
        self.answer = answer
        self.var = var

        self.content = tk.Label(self, text=question)
        self.content.pack()
        if self.type == "Entry":
            self.stringVar = tk.StringVar(self)
            self.main = tk.Entry(self, width=50, textvariable=self.stringVar)
            self.main.pack(side=tk.TOP, padx=5, pady=5)
        elif self.type == "Checkbutton":
            self.main = []
            self.mainVar = []
            for i in var:
                self.mainVar.append(tk.BooleanVar())
                self.mainVar[-1].set(False)
                self.main.append(tk.Checkbutton(self, width=50, var=self.mainVar[-1], text=i))
                self.main[-1].pack()
        elif self.type == "Radiobutton":
            self.main = []
            self.mainVar = tk.IntVar()
            for i in range(len(var)):
                self.main.append(tk.Radiobutton(self, width=50, value=i, var=self.mainVar, text=var[i]))
                self.main[-1].pack()

        elif self.type == "Combobox":
            self.main = ttk.Combobox(self, width=50, values=self.var, state="readonly")
            self.main.pack()
        else:
            self.main = ttk.Spinbox(self, width=50, values=self.var, state="readonly")
            self.main.pack()

        self.ok = tk.Button(self, text="Ответить", width=10, command=self._answer)
        self.ok.pack(side=tk.RIGHT, padx=5, pady=5)
        self.cancel = tk.Button(self, text="Пропустить", width=10, command=self.skip)
        self.cancel.pack(side=tk.LEFT, padx=5, pady=5)

    def _answer(self):
        correct = True
        if self.type == "Entry":
            if self.stringVar.get() != self.answer:
                correct = False
        elif self.type == "Checkbutton":
            for i in range(len(self.mainVar)):
                if self.main[i]['text'] in self.answer and not self.mainVar[i].get():
                    correct = False
                    break
        elif self.type == "Radiobutton":
            for i in range(len(self.main)):
                if self.main[i]['text'] != self.answer and self.mainVar.get() == self.main[i]['value']:
                    correct = False
                    break
        elif self.type == "Spinbox" or self.type == "Combobox":
            if self.main.get() != self.answer:
                correct = False

        if correct:
            print("В-верно!")
            self.master.total += 1
        self.skip()

    def skip(self):
        self.destroy()
        self.master.QAs.pop(0)
        self.master.next()

