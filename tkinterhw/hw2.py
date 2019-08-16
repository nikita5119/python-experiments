
from tkinter import *
import requests

window= Tk()
window.title("homework-example")
window.geometry('800x400')

def clicked():
    textName= entrybox.get()
    r=requests.get('https://tinyurl.com/api-create.php?url='+textName)
    a=r.text
    text.insert(0.0, a)
    # print(r.text)

l1=Label (window,text="Enter the URL:")
l1.grid(row=0)

entrybox = Entry (window)
entrybox.grid(row = 0, column = 1)

buton = Button(window,text="change", bg = 'pink', fg = 'white', command=clicked) 
buton.grid(row=0, column=3)

text = Text(window, width = 55, height = 55, wrap =WORD)
text.grid(row=2,columnspan=2,sticky = W)

window.mainloop()