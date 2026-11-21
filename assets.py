from pathlib import Path
import tkinter as tk


picture_path1 = Path(__file__).with_name("monster_peaceful.png")
picture1 = tk.PhotoImage(file=str(picture_path1))
picture_path2 = Path(__file__).wth_name("monster_angry.png")
picture2 = tk.PhotoImage(file=str(picture_path2))
picture_path3 = Path(__file__).with_name("monster_enraged.png")
picture3 = tk.PhotoImage(file=str(picture_path3))