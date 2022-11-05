import tkinter as tk
from tkinter import ttk
import socket
import threading

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('')
        self.geometry('100x800')
        self.configure(background='red')
        self.resizable(0, 0)
        self.create_body_frame()
        t1 = threading.Thread(target=self.napraviKonekciju)
        t1.start()

    def create_body_frame(self):
        self.s = ttk.Style()
        self.s.configure('Frame2.TFrame', background='blue')
        self.body = ttk.Frame(self, width=100, height=800, style='Frame2.TFrame')
        self.body.pack()
        self.body.pack_propagate(0)

    def dodajLabelu(self):
        self.labela = ttk.Label(self.body, text="tekst")
        self.labela.pack()

    def napraviKonekciju(self):
        s = socket.socket()
        host = socket.gethostname()
        port = 12345
        s.bind((host, port))
        s.listen(5)
        print("Listen");
        while True:
            conn, addr = s.accept()
            print('Got connection from', addr)
            poruka = 'Thank you for connecting'
            conn.send(poruka.encode())
            conn.close()

app = App()
app.mainloop()