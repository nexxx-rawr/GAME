from pathlib import Path
import tkinter as tk


def load_pictures(window):
    picture1 = tk.PhotoImage(
        master=window, file=str(Path(__file__).with_name("monster_peaceful.png"))
    )
    picture2 = tk.PhotoImage(
        master=window, file=str(Path(__file__).with_name("monster_angry.png"))
    )
    picture3 = tk.PhotoImage(
        master=window, file=str(Path(__file__).with_name("monster_enraged.png"))
    )
    return picture1, picture2, picture3
