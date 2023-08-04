#import module
from tkinter import *
from tkinter.ttk import *


#import strftime function to

from time import strftime


#creating tkinter window

root=Tk()
root.title('Clock')



def time():
    string=strftime('%H:%M:%S')
    lbl.config(text=string)
    lbl.after(1000,time)


lbl=Label(root,font=('calibri',40,'bold'),
          background="purple",
          foreground='white'
          )


#placing clock at the center of the tkinter window

lbl.pack(anchor='center')
time()

mainloop()


