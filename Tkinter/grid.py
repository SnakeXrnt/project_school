from tkinter import Tk, Label, IntVar, ttk, Entry, Button , LabelFrame , Menu , Frame , StringVar , Checkbutton
from tkinter import messagebox as msg
from PIL import Image , ImageTk

mainWindow = Tk()
mainWindow.title('BelajarGridLayout')

#pengaturan default font untuk aplikasi
default_font = ('Arial' , 15)

def show_msg_box():
    msg.showinfo('About JM KASIR','JM KASIR 2020\n versi 2020.11.2(beta tkinter)')

def show_warning():
    msg.showwarning('PERINGATAN', 'ANDA TIDAK ADA AKSES GBLK !!!!!!!!!')

def show_error():
    msg.showerror('Error!','code: BPKKAU!! \n WRONG FATHER NAME')
def show_ask():
    result_user = msg.askyesnocancel('Conformation Father Name','ARE YOU SURE THAT THIS IS YOUR FATHERS NAME')

#membuat menu baru untuk main window
main_menu_bar = Menu(mainWindow)
mainWindow.config(menu=main_menu_bar)

#membut item untuk main_menu_bar unt
help_menu = Menu(main_menu_bar,tearoff=0)
help_menu.add_command(label='about', command=show_msg_box)
help_menu.add_command(label='asking', command=show_ask)
help_menu.add_command(label='WARN', command=show_warning)
help_menu.add_command(label='error', command=show_error)
main_menu_bar.add_cascade(label='help',menu=help_menu)





label1 = Label(mainWindow,text='Nama Depan \t: ',font=default_font)
label1.grid(row=0,column=0 , sticky='w')

entry1 = Entry(mainWindow,font=default_font)
entry1.grid(row=0,column=1)

label2 = Label(mainWindow,text='Nama belakang \t: ',font=default_font)
label2.grid(row=1,column=0,sticky='w')

entry2 = Entry(mainWindow,font=default_font)
entry2.grid(row=1,column=1)

checkBtn1Var = IntVar() #Check = 1 , unCheck = 0
checkBtn1 = Checkbutton(mainWindow,text='DONT REMIND ME AGAIN!',variable=checkBtn1Var)
checkBtn1.grid(row=2,columnspan=2,sticky='w')

openImage = Image.open('img/Ibm.jpg')#membuka gambar
imageDone = ImageTk.PhotoImage(openImage)#merender
imageLabel = Label(mainWindow,image=imageDone)
imageLabel.grid(row=0,column=2,columnspan=2,rowspan=2,sticky='wens')

button1 = Button(mainWindow,text='ZOOM IN',font=default_font)
button1.grid(row=2,column=2)

button2 = Button(mainWindow,text='ZOOM OUT',font=default_font)
button2.grid(row=2,column=3)



mainWindow.mainloop()
