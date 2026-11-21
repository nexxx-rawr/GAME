import time as tm
import random as r
import tkinter as tk
from tkinter import ttk
from assets import load_pictures

window = tk.Tk()
picture1, picture2, picture3 = load_pictures(window)
window.geometry("400x400")
window.config(bg="light blue")
notebook = ttk.Notebook(window)
notebook.pack(expand=True,fill="both")
entries = {}

def create_t(t,f,s,ts,x,y,tt,bg="light blue"):
    text = tk.Label(tt,text=t,font=(f,s,ts),bg=bg)
    text.place(x=x,y=y)

def create_b(t,f,s,ts,x,y,tt,bg="light blue",c1=None,):
    button = tk.Button(tt,text=t,font=(f,s,ts),bg=bg,command=c1)
    button.place(x=x,y=y)

def create_e(tt,w,x,y,id):
    entry = tk.Entry(tt,width=w)
    entry.place(x=x,y=y)
    entries[id] = entry
    return entry

def check_entry(id,password):
    t = entries[id].get()
    if t == password:
        print(f"Unlocked Entry Number: {id}")
    else:
        print(f"Failed to login into Entry Number: {id}")

def create_ta(name,bg):
    tab = tk.Frame(notebook,bg=bg)
    notebook.add(tab,text=name)
    return tab

home_t = create_ta("Home","light blue")
shop_t = create_ta("Shop","light blue")
create_t("Game","Arial",30,"bold",140,0,home_t,)


monster_image = picture1.subsample(3, 3)
monster_label = tk.Label(home_t, image=monster_image, bg="light blue")
monster_label.place(relx=0.5, y=65, anchor="n")

window.mainloop()