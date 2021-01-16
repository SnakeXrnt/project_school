from tkinter import *
from tkinter import StringVar , IntVar
from tkinter.ttk import *
from tkinter import messagebox as msg
from time import strftime
import os
import sys
import tkinter.ttk as ttk
#from ttkthemes import ThemedStyle
from json import *
from datetime import *
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
global Home
from calculator import calculatess
def lapor_pemb():
    new = Tk()
    Label(new,text='Masukan kode barang \t: ').grid(row=1,column=1,sticky='w')
    Label(new,text='Nama barang \t: ').grid(row=2,column=1,sticky='w')
    Label(new,text='Harga satuan \t: ').grid(row=3,column=1,sticky='w')
    Label(new,text='Jumlah stock \t: ').grid(row=4,column=1,sticky='w')
    Label(new,text='Barang Yang Di Beli \t :').grid(row=5,column=1,sticky='w')
    label_nama = Label(new,text='Masukan kode barang')
    label_nama.grid(row=2,column=2)
    label_harga = Label(new,text='Masukan kode barang')
    label_harga.grid(row=3,column=2)
    label_jumlah = Label(new,text='Masukan kode barang')
    label_jumlah.grid(row=4,column=2)
    kode_barang = StringVar()
    Entry(new,textvariable=kode_barang).grid(row=1,column=2)
    dibeli = IntVar()
    Entry(new,textvariable=dibeli).grid(row=5,column=2)

    f = open('barang.json','r+')
    data = load(f)
    def dah():
        print(data)
        code = kode_barang.get()
        print(code)
        namab = data[code]['Nama']
        hargab = data[code]['Harga']
        jumlahb = data[code]['jumlah']
        label_nama.config(text=str(namab))
        label_harga.config(text=str(hargab))
        label_jumlah.config(text=str(jumlahb))

    Button(new,text='Ok',command=dah).grid(row=1,column=3)
    new.mainloop()
