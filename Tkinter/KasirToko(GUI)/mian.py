from tkinter import Tk, ttk , Label, StringVar, ttk, Entry, Button , LabelFrame , Menu , Frame
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msg
from time import strftime
import os
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from json import *

def register():
    global register_screen
    register_screen = Tk()
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register",command = register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    button = Button(login_screen, text="Login", command = login_verify)
    button.pack()


# Implementing event on register button

def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", font=("calibri", 11)).pack()

# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success \n Please close all login window to continue").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
    Home()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login",  command = login).pack()
    Label(text="").pack()


#login()


def Home():
    window = Tk()
    window.geometry('1000x600')
    window.title('Home')



    menu_bar = Menu(window)
    window.config(menu=menu_bar)

    label_menu_file = Menu(menu_bar)

    label_menu_file.add_command(label='NewProgram')
    menu_bar.add_cascade(label='File',menu=label_menu_file)

    def show_msg_box():
        msg.showinfo('About KASIR TOKO TERANGJAYA ','versi 2020.11.2(beta tkinter)')


    label_help_menu = Menu(menu_bar,tearoff=0)
    label_help_menu.add_command(label='HELP')
    label_help_menu.add_command(label='ABOUT',command=show_msg_box)
    menu_bar.add_cascade(label='Help',menu=label_help_menu)




    tabControl = ttk.Notebook(window)
    tab1 = Frame(tabControl)
    tab2 = Frame(tabControl)
    tabControl.add(tab1, text='Home')
    tabControl.add(tab2, text='Settings')
    tabControl.grid(column=0,row=0)

    label = Label(tab1, font=("Courier", 30, 'bold'))
    label.grid(row =0, column=0)

    def digitalclock():
       text_input = strftime("%H:%M:%S")
       label.config(text=text_input)
       label.after(200, digitalclock)
    digitalclock()




    Label(tab1,text='SELAMAT DATANG DI TOKO TERANG JAYA',font=('cabari',25,'bold')).grid(column=0,row=1,columnspan=11)

    Button(tab1,text='MASUKAN BARANG BARU').grid(row=3,column=0,padx=30,pady=20)
    Button(tab1,text='UBAH KODE BARANG').grid(row=5,column=0,padx=30,pady=20)
    Button(tab1,text='UBAH JUMLAH STOCK').grid(row=7,column=0,padx=30,pady=20)
    Button(tab1,text='UBAH HARGA BARANG').grid(row=9,column=0,padx=30,pady=20)

    Button(tab1,text='BUKA MESIN KASIR').grid(row=3,column=2,padx=30,pady=20)
    Button(tab1,text='BUKA LIST HARGA').grid(row=5,column=2,padx=30,pady=20)
    Button(tab1,text='BUKA LIST STOCK').grid(row=7,column=2,padx=30,pady=20)
    Button(tab1,text='BUKA LIST STOCK DAN HARGA').grid(row=9,column=2,padx=30,pady=20)

    Button(tab1,text='LAPOR PEMBELIAN').grid(row=3,column=6,padx=30,pady=20)
    Button(tab1,text='LAPOR ERROR').grid(row=5,column=6,padx=30,pady=20)
    Button(tab1,text='LAPOR PENAMBAHAN UANG').grid(row=7,column=6,padx=30,pady=20)
    Button(tab1,text='LAPOR PENAGMBILAN UANG').grid(row=9,column=6,padx=30,pady=20)

    time = int(strftime('%H'))
    salam = ''
    selamat = ''
    semangat = ''
    selamat1 = ''
    if time < 11 :
        salam += 'Selamat Pagi'
        selamat += 'Semangat Bekerja sekali lagi :)'
        semangat += 'SEMANGAT !'
        selamat1 = 'Selamat Bekerja'
    elif time < 14 :
        salam += 'Selamat Siang'
        selamat += 'Semangat Bekerja sekali lagi :)'
        semangat += 'SEMANGAT !'
        selamat1 = 'Selamat Bekerja'
    elif time < 18 :
        salam += ' Selamat Sore'
        selamat += 'Selamat Istirahat :)'
        semangat += 'Goodbye'
        selamat1 = 'Selamat Pulang'

    else :
        salam += 'Selamat Malam'
        selamat += 'Selamat Beristirahat :)'
        semangat += 'Goodbye'
        selamat1 = 'Selamat Pulang'

    def restart():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        window.destroy()
    def quit():
    	exit()

    Label(tab2,text='Settings',font=('arial',30,'bold')).grid(row=0,column=0)
    Label(tab2,text='Register a new user \t :',font=('arial',10)).grid(row=1,column=0,sticky='w')
    Button(tab2,text="Register", command=register).grid(row=1,column=1,sticky='w')
    Label(tab2,text='Restart App \t \t :',font=('arial',10)).grid(row=2,column=0,sticky='w')
    Button(tab2,text='Restart',command=restart).grid(row=2,column=1,sticky='w')
    Label(tab2,text='Quit\t \t \t :',font=('arial',10)).grid(row=3,column=0,sticky='w')
    Button(tab2,text='QUIT!',command=quit).grid(row=3,column=1,sticky='w')




    Label(tab2,text='Font Size \t \t :',font=('arial',10)).grid(row=4,column=0)
    font_size = IntVar()
    fz = Entry(tab2, textvariable=font_size).grid(column=1,row=4)
    p = font_size.get()

    def change():
        with open('file.json', 'r+') as file:
            m = 10
            m += p
            content = file.read()
            file.seek(0)
            content.replace(content,str(m))
            file.write(str(m))
            file.close()

    Button(tab2,text='Change!',command=change).grid(column=4,row=4)
    s=10









    sapa5 =Label(tab1,text='Halo Workers',font=('arial',s)).grid(row=4,column=8)
    sapa4 =Label(tab1,text='Jangan lupa cuci jangan \n dan jaga kebersihan',font=('arial',s)).grid(row=5,column=8)
    sapa3 =Label(tab1,text='Stay Safe and Healty... \n jangan Lupa berdoa juga ya ',font=('arial',s)).grid(row=6,column=8)

    sapa2 =Label(tab1,text=(selamat),font=('arial',s)).grid(row=7,column=8)
    sapa1 =Label(tab1,text=(semangat),font=('arial',s)).grid(row=9,column=8)















login()



mainloop()
