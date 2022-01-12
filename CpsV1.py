import tkinter as tk
import time
import random

root = tk.Tk()
root.title("Clicker V1")
root.geometry("1000x1000")
root.configure(background="Gray")
count = 0

def Color():
    if count > 0:
        root.configure(background= "green")
    elif count < 0:
        root.configure(bg= "red")
    else:
        root.configure(bg= "gray")

def UpF():
    global count
    count += 1
    Number.configure(text= count)
    Color()

def DownF():
    global count
    count -= 1
    Number.configure(text= count)
    Color()


Up = tk.Button(
    root,
    text= "Up",
    font= ('Calibri', 40, 'bold'),
    fg= "white",
    bg= "Black",
    command= UpF
)
Up.pack()

Number = tk.Label(
    root,
    text= count,
    font= ('Calibri', 40, 'bold'),
    fg= "white",
    bg= "Black",
)
Number.pack()

Down = tk.Button(
    root,
    text= "Down",
    font= ('Calibri', 40, 'bold'),
    fg= "white",
    bg= "Black",
    command= DownF
)
Down.pack()



root.mainloop()