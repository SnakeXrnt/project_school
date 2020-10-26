
from tkinter import Tk, Label, StringVar, ttk, Entry, Button

window = Tk()
window.title('Rectangle Calculator')
window.minsize(500,250)

def calculate():
    sett = set.get()
    panj = int(panjang.get())
    leb = int(lebar.get())
    ting = int(tinggi.get())

    if sett == "LUAS" :
        out = panj*leb
        output.config(text=str(out))
    else :
        out = panj*leb*tinggi
        output.config(text=str(out))

header_title = Label(window , text='Rectangle Calculator', font=('arial',20,'bold'))
header_title.grid(columnspan=3)

header_secondary = Label(window , text='By : EthanBastian', font=('arial',10,'bold'))
header_secondary.grid(columnspan=3)

label1 = Label(window,text='Settings',font=('arial',15))
label1.grid(column=0,row=3)

label2 = Label(window,text='Panjang',font=('arial',15))
label2.grid(column=1,row=3)

label3 = Label(window,text='Lebar',font=('arial',15))
label3.grid(column=2,row=3)

label4 = Label(window,text='Tinggi',font=('arial',15),bd=20, padx=10, pady=15)
label4.grid(column=3,row=3)

label5 = Label(window,text='Hasil',font=('arial',15))
label5.grid(column=4,row=3)


set = StringVar()
setting = ttk.Combobox(window,textvariable=set,width=8)
setting['values'] = ['LUAS','VOLUME']
setting.grid(column=0,row=4)
setting.current(0)

panjang = StringVar()
p_entry = Entry(window,textvariable=panjang,font=('arial',15),width=8)
p_entry.grid(column=1,row=4)

lebar = StringVar()
l_entry = Entry(window,textvariable=lebar,font=('arial',15),width=8)
l_entry.grid(column=2,row=4)

tinggi = StringVar()
t_entry = Entry(window,textvariable=tinggi,font=('arial',15),width=8)
t_entry.grid(column=3,row=4)

output = Label(window,text='0',font=('arial',17))
output.grid(column=4,row=4)

note = Label(window,text='*jika anda ingin menghitung luas maka column tinggi diisi dengan 1 :)',font=('arial',16),bd=20, padx=10, pady=15)
note.grid(columnspan=5)
note.grid(column=0,row=5)

button = Button(window,font=('arial',19),text='CALCULATE!',command=calculate)
button.grid(column=0,row=6)







window.mainloop()
