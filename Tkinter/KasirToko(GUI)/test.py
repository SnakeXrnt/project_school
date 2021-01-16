
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msg
from time import strftime
import os
import sys
import tkinter.ttk as ttk
#from ttkthemes import ThemedStyle
from tkinter import Tk, Label, StringVar, ttk, Entry, Button, LabelFrame, Menu, Frame

from json import *
from datetime import *
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet


window = Tk()
window.title("Hypermart Belanja Puas")
# window.minsize(800, 600)
window.resizable(False, False)

##FORM
def put_into_cart():
    kode = nama.get()
    jumlah = jumlah_dibeli.get()
    f = open('barang.json','r+')
    data = {}
    data = load(f)
    benda = data[kode]["Nama"]
    harga = data[kode]["Harga"]
    jumlah_awal = data[kode]["jumlah"]
    jumlah_akhir = int(jumlah_awal) - int(jumlah)
    data[kode] = {
        'Nama' : benda,
        'Harga' : harga,
        'jumlah' : jumlah_akhir
    }
    with open('barang.json','w') as d:
        dump(data,d)
    harga_total_satuan = harga*jumlah
    text = ''
    text = benda +' -> ' + jumlah + ' --> ' + harga_total_satuan
    list_items.config(text=text)



formFrame = LabelFrame(window, text="Form Pembelian")
formFrame.grid(column = 0, row=0, columnspan=3, rowspan=4, padx=5, pady=5)
header_form = Label(formFrame, text="HYPERMART", font=('arial', 16, 'bold'), bd=20, padx=20, pady=15 )
header_form.grid(column=0, row=0, columnspan=2)

label_nama = Label(formFrame, text="Nama : ", font=('arial', 12, 'bold') , justify="left", bd=20, padx=5, pady=5)
label_nama.grid(column = 0, row=1)

nama = StringVar()
entry_nama = Entry(formFrame, textvariable=nama, font=('arial', 12, 'bold'), width=8)
entry_nama.grid(column=1, row=1)

label_harga = Label(formFrame, text="jumlah : ", font=('arial', 12, 'bold') , justify="left", bd=20, padx=5, pady=5)
label_harga.grid(column = 0, row=2)

jumlah_dibeli = StringVar()
entry_harga = Entry(formFrame, textvariable=jumlah_dibeli, font=('arial', 12, 'bold'), width=8)
entry_harga.grid(column=1, row=2)


button_entry = Button(formFrame, font=('arial', 12, 'bold'), text='Entry Barang', command=put_into_cart)
button_entry.grid(column=0, row=3, columnspan=2)


        ##STATUS
statusFrame = LabelFrame(window, text="Status")
statusFrame.grid(column = 0, row=4, columnspan=3, padx=5, pady=5)

header_status = Label(statusFrame, text="Status", font=('arial', 16, 'bold'), bd=20, padx=20, pady=15 )
header_status.grid(column=0, row=0)


        ##TOTAL
totalFrame = LabelFrame(window, text="Total Pembelian")
totalFrame.grid(column=3, row=0, columnspan=2, padx=5, pady=5)

header_total = Label(totalFrame, text="Total", font=('arial', 16, 'bold'), bd=20, padx=20, pady=15 )
header_total.grid(column=0, row=0)


        ##LIST
listFrame = LabelFrame(window, text="Daftar Barang")
listFrame.grid(column=3, row=1, columnspan=2, rowspan=4 , padx=5, pady=5)


header_list = Label(listFrame, text="Daftar Barang", font=('arial', 16, 'bold'), bd=20, padx=20, pady=15 )
header_list.grid(column=0, row=0, columnspan=2)

list_items = Label(listFrame, text="", font=('arial', 10), bd=20, padx=20, pady=15 )
list_items.grid(column = 0, row=1, columnspan=2)



window.mainloop()
