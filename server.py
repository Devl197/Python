import tkinter as tk
from tkinter import ttk
import socket
import threading
from create_db import *

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
        port = 12344
        s.bind((host, port))
        s.listen(5)
        print("Listen");
        while True:
            conn, addr = s.accept()
            print('Got connection from', addr)
            data = conn.recv(30)
            data = data.decode()
            data = data.strip()
            poruka = 'dsadas'
            if data == "napravi_tabelu":
                poruka = "Tabela napravljena"
                try:
                    db_create_table('automobili')
                except:
                    poruka = "Tabela vec postoji"
                print(poruka)
            elif data == "napravi_zapis":
                data = conn.recv(1024)
                data = data.decode()
                insert_data = data.split(" ")
                db_insert(insert_data)
                poruka = "Zapis unet: " + data
            elif data == "vrati_zapise":
                poruka = db_select(None)
            conn.send(str(poruka).encode())
            conn.close()

app = App()
app.mainloop()