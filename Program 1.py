#Ben Krehbiel
#4/9/2025
#first time with TK

import tkinter
from tkinter import *



saying = Tk()
saying.geometry("500x500")
saying.title("My Favourite saying")


textbox = tkinter.Text(saying, height=1, width=34)
textbox.pack(pady=10)

textbox.insert(tkinter.END, "somewhere in the heavens, we exist")
saying.mainloop()
