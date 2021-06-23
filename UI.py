import tkinter as tk
from PIL import ImageTk,Image
from Hope import command,speak,ask,time,date,question,wish,remember,screenshot,cpu,joke,question,screenrec,wish
from Hope import internet_connection,NewsFromBBC
from Main import *
from detect import *
from language import *
from fire import fire
from inpcommand import inpcommand
import time


speak(" Initializing HOPE...Ready")
print("Ready")

wish()

h=700
w=700

root=tk.Tk()


canvas=tk.Canvas(root, height=h, width=w)
canvas.pack()

background_image=ImageTk.PhotoImage(file='bg_img.jpg')
background_label=tk.Label(root, image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

frame=tk.Frame(root, bg='black')
frame.place(relwidth=0.95, relheight=0.1, relx=0.5,rely=0.1,anchor='n')

inp=tk.Entry(frame)
inp.place(relwidth=0.4,relheight=0.5,relx=0.03,rely=0.26)

button=tk.Button(frame, text="Speak", bg='#36d6d9', fg='blue', command=lambda : fire())
button.place(relx=0.73,relwidth=0.25, relheight=0.5, rely=0.26)

buttonone=tk.Button(frame, text="Text Result", bg='#36d6d9', fg='blue',command=lambda:inpcommand(inp.get()))
buttonone.place(relx=0.45,relwidth=0.25, relheight=0.5, rely=0.26)

lower_frame=tk.Frame(root, bg='#002aff', bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')


label=tk.Label(lower_frame, bg='black', fg='blue', text='HELLO, IM HOPE YOUR VIRTUAL ASSISTANT',font=50)
label.place(relwidth=1,relheight=1)
root.mainloop()
