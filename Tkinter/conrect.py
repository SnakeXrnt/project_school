
from tkinter import Tk, Label, StringVar, ttk, Entry, Button

window = Tk()
window.title('Rectangle Calculator')
window.minsize(800,600)

header_title = Label(window , text='Rectangle Calculator', font=('arial',20,'bold'))
header_title.grid(columnspan=3)

header_secondary = Label(window , text='By : EthanBastian', font=('arial',10,'bold'))
header_secondary.grid(columnspan=3)
