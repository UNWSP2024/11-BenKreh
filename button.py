#ben Krehbiel
#4/11/2025
#who askin... 

from tkinter import *
def click():
    label.config(text= "Benjamin Krehbiel\n1234 tutle Dr \nhastings MN 55033")

def stop():
    window.destroy()

window = Tk()
window.geometry("500x500")

Show_info = Button(window, text="show info")
Show_info.config(command=click)
Show_info.pack()

Stop = Button(window, text="Quit")
Stop.config(command=stop)
Stop.pack()

label = Label(window, text="")
label.pack()

window.mainloop()
