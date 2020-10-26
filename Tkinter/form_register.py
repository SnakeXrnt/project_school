from tkinter import Tk, Label, StringVar, ttk, Entry, Button , Checkbutton , Radiobutton , IntVar , scrolledtext , LabelFrame

window = Tk()
window.title('formPendaftaranSiswaBaru')

header_apps = Label(window,text='Pendaftaran Siswa Baru',font=('arial',20,'bold'),justify='left')
header_apps.grid(columnspan=3)

label_name = Label(window,text='nama :',font=('arial',16),justify='left')
label_name.grid(column=0,row=1)

name = StringVar()
entry_name = Entry(window,textvariable=name,width=30)
entry_name.grid(column=1,row=1,columnspan=2)

label_wn = Label(window,text='kewarganegaraan :',font=('arial',16),justify='left')
label_wn.grid(column=0,row=2)

WNI = StringVar()
wni_check = Checkbutton(window,text='WNI',font=('arial',16),variable=WNI)
wni_check.deselect()
wni_check.grid(column=1,row=2)

WNA = StringVar()
wna_check = Checkbutton(window,text='WNA',font=('arial',16),variable=WNA)
wna_check.deselect()
wna_check.grid(column=2,row=2)

label_jenis = Label(window,text='jenis :',font=('arial',16),justify='left')
label_jenis.grid(column=0,row=3)


jenis = IntVar()
laki_radio = Radiobutton(window,text='LANANG',variable=jenis,value='L')
laki_radio.grid(column=1,row=3)
pr_radio = Radiobutton(window,text='TINO',variable=jenis,value='P')
pr_radio.grid(column=2,row=3)

label_history = Label(window,text='Riwayat Penyakit :',font=('arial',16),justify='left')
label_history.grid(column=0,row=4)

deskripsi = scrolledtext.ScrolledText(window,width=30 , height=5 )
deskripsi.grid(column=1,row=4,columnspan=2)

frame1 = LabelFrame(window,text='INFORMASI ORANG TUA')
frame1.grid(column=0,row=5)

label_ayah = Label(frame1,text='Nama Ayah :')
label_ayah.grid(column=0,row=0)

ayah = StringVar()
entry_ayah = Entry(frame1,textvariable=ayah,width=20)
entry_ayah.grid(column=1,row=0)



label_ibu = Label(frame1,text='Nama Ibu :')
label_ibu.grid(column=0,row=1)

ibu = StringVar()
entry_ibu = Entry(frame1,textvariable=ibu,width=20)
entry_ibu.grid(column=1,row=1)


window.mainloop()
