from tkinter import Tk, ttk , Label, StringVar, ttk, Entry, Button , LabelFrame , Menu , Frame
from tkinter import *
from tkinter.ttk import *
from time import strftime
import os

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
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
    login_screen = Toplevel(main_screen)
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
    main_screen.destroy()


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
    Button(text="Register", command=register).pack()

main_account_screen()

def Home():
    window = Tk()
    window.geometry('1000x600')
    window.title('Home')

    tabControl = ttk.Notebook(window)
    tab1 = Frame(tabControl)
    tab2 = Frame(tabControl)
    tabControl.add(tab1, text='Home')
    tabControl.add(tab2, text='Settings')
    tabControl.pack(expand=1,fill='both')

    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text = string)
        lbl.after(1000, time)
            # Styling the label widget so that clock
            # will look more attractive
    lbl = Label(tab1, font = ('calibri', 40, 'bold'))

        # Placing clock at the centre
        # of the tkinter window
    lbl.grid(column=0,row=0,sticky='wens')
    time()


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
        selamat += 'Selamat Beristirahat:)'
        semangat += 'Goodbye'
        selamat1 = 'Selamat Pulang'

    sapa = Label(tab1,text=(salam),font=('Arial',25,'bold')).grid(row=3,column=8)


    Label(tab1,text='Halo Workers',font=('Arial',10)).grid(row=4,column=8)
    Label(tab1,text='Jangan lupa cuci jangan \n dan jaga kebersihan',font=('Arial',10)).grid(row=5,column=8)
    Label(tab1,text='Stay Safe and Healty... \n jangan Lupa berdoa juga ya ',font=('Arial',10)).grid(row=6,column=8)

    Label(tab1,text=(selamat),font=('Arial',10)).grid(row=7,column=8)
    Label(tab1,text=(semangat),font=('Arial',15,'bold')).grid(row=9,column=8)












mainloop()
main_screen.mainloop()
