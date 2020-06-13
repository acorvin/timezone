from tkinter import *
from tkinter.ttk import *
import time
import datetime
import pytz

root = Tk()
root.title('Cluck Clock')
root.configure(bg='black')

img = PhotoImage(file="ducky.png")
canvas = Canvas(root, width = 240, height = 200,background = 'black')
canvas.pack()
canvas.create_image(70,100, anchor=NW, image=img)
canvas.create_text(124,50,fill="white",font="Times 20 italic bold",
                        text="Munich")

def time():
    string = datetime.datetime.now(tz=pytz.timezone('Europe/Berlin'))
    lbl.config(text = string.strftime('%H:%M:%S'))
    lbl.after(1000, time)

lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'black',
            foreground = 'white')

lbl.pack(anchor = 'center')

time()
root.mainloop()

