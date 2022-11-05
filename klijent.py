import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('')
        self.geometry('800x800')
        self.configure(background='red')
        self.resizable(0, 0)

        self.create_header_frame()
        self.create_body_frame()
        self.create_footer_frame()

    def create_header_frame(self):
        self.s = ttk.Style()
        self.s.configure('TFrame', background='green')
        self.s.configure('Frame1.TFrame', background='black')
        self.header = ttk.Frame(self, width=800, height=50, style='Frame1.TFrame')
        self.header.pack()
        self.header.pack_propagate(0)

    def create_body_frame(self):
        self.s.configure('Frame2.TFrame', background='blue')
        self.body = ttk.Frame(self, width=800, height=700, style='Frame2.TFrame')
        self.body.pack()
        self.body.pack_propagate(0)

    def create_footer_frame(self):
        self.s.configure('Frame3.TFrame', background='green')
        self.footer = ttk.Frame(self, width=800, height=50, style='Frame3.TFrame')
        self.labela = ttk.Label(self.footer, text="© 2022 Aleksa Stanković RIN-10/21 | Aleksandar Mladenović RIN-34/21")
        self.labela.configure(anchor="center")
        self.labela.pack(expand=True)
        self.footer.pack()
        self.footer.pack_propagate(0)


app = App()
app.mainloop()
