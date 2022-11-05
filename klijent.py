import tkinter as tk
from tkinter import ttk
import socket

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
        self.btn_napravi_tabelu = ttk.Button(self.body, text="Napravi tabelu", command=self.napraviTabelu)
        self.btn_napravi_zapis = ttk.Button(self.body, text="Napravi zapis", command=self.napraviZapis)
        self.btn_vrati_zapise = ttk.Button(self.body, text="Vrati Zapise", command=self.vratiZapise)

        self.btn_napravi_tabelu.pack()
        self.btn_napravi_zapis.pack()
        self.btn_vrati_zapise.pack()
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

    def napraviTabelu(self):
        HOST = socket.gethostname()  # The remote host
        PORT = 12344  # The same port as used by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send('{:<30}'.format("napravi_tabelu").encode())
        data = s.recv(1024)  # razmislite o data = s.recv(1024).decode()
        s.close()
        print('Received', (data))

    def napraviZapis(self):
        HOST = socket.gethostname()  # The remote host
        PORT = 12344  # The same port as used by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send('{:<30}'.format("napravi_zapis").encode())
        s.send('BMW 10000'.encode())
        data = s.recv(1024)
        s.close()
        print('Received', (data))

    def vratiZapise(self):
        HOST = socket.gethostname()  # The remote host
        PORT = 12344  # The same port as used by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send('{:<30}'.format("vrati_zapise").encode())
        data = s.recv(1024)
        s.close()
        print('Received', (data))

app = App()
app.mainloop()
