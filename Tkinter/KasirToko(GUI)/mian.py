
from tkinter import *
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





def Home():
    global Home
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
    win = Frame(tabControl)
    tabControl.add(tab1, text='Home')
    tabControl.add(tab2, text='Settings')
    tabControl.add(win,text='Calculator')
    tabControl.grid(column=0,row=0)

    def btn_click(item):
        global expression
        expression = expression + str(item)
        input_text.set(expression)

    # 'bt_clear' function :This is used to clear
    # the input field

    def bt_clear():
        global expression
        expression = ""
        input_text.set("")

    # 'bt_equal':This method calculates the expression
    # present in input field

    def bt_equal():
        global expression
        result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
        input_text.set(result)
        expression = ""

    expression = ""

    # 'StringVar()' :It is used to get the instance of input field

    input_text = StringVar()

    # Let us creating a frame for the input field

    input_frame = Frame(win, width=312, height=50 )

    input_frame.pack(side=TOP)

    #Let us create a input field inside the 'Frame'

    input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50,  justify=RIGHT)

    input_field.grid(row=0, column=0)

    input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field

    #Let us creating another 'Frame' for the button below the 'input_frame'

    btns_frame = Frame(win, width=312, height=272.5)

    btns_frame.pack()

    # first row

    clear = Button(btns_frame, text = "C", width = 32,    cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

    divide = Button(btns_frame, text = "/", width = 10,    cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

    # second row

    seven = Button(btns_frame, text = "7", width = 10,    cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)

    eight = Button(btns_frame, text = "8", width = 10,    cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)

    nine = Button(btns_frame, text = "9", width = 10,   cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)

    multiply = Button(btns_frame, text = "*", width = 10,    cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

    # third row

    four = Button(btns_frame, text = "4", width = 10,    cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)

    five = Button(btns_frame, text = "5", width = 10,  cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)

    six = Button(btns_frame, text = "6", width = 10,  cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)

    minus = Button(btns_frame, text = "-", width = 10,    cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

    # fourth row

    one = Button(btns_frame, text = "1", width = 10,  cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)

    two = Button(btns_frame, text = "2", width = 10,  cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)

    three = Button(btns_frame, text = "3", width = 10,  cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)

    plus = Button(btns_frame, text = "+", width = 10,    cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

    # fourth row

    zero = Button(btns_frame, text = "0", width = 21,  cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)

    point = Button(btns_frame, text = ".", width = 10,    cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)

    equals = Button(btns_frame, text = "=", width = 10,    cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

    label = Label(tab1, font=("Courier", 30, 'bold'))
    label.grid(row =0, column=0)

    def digitalclock():
       text_input = strftime("%H:%M:%S")
       label.config(text=text_input)
       label.after(200, digitalclock)
    digitalclock()




    def masukan_barang_baru():
        msk_brng = Toplevel(window)




        Label(msk_brng,text='Nama barang \t :').grid(row=1,column=1)
        nama_barang = StringVar()
        nama_barang_tool = Entry(msk_brng,textvariable=nama_barang).grid(row=1,column=2)

        Label(msk_brng,text='Harga Barang \t : ').grid(row=2,column=1)
        Harga_barang = IntVar()
        harga_barang_tool = Entry(msk_brng,textvariable=Harga_barang).grid(row=2,column=2)


        Label(msk_brng,text='Kode barang \t : ').grid(row=3,column=1)
        kode_barang = StringVar()
        kode_barang_tool = Entry(msk_brng,textvariable=kode_barang).grid(row=3,column=2)

        Label(msk_brng,text='Jumah Stock \t : ').grid(row=4,column=1)
        Jumlah_barang = IntVar()
        Jumlah_barang_tool = Entry(msk_brng,textvariable=Jumlah_barang).grid(row=4,column=2)

        def msk_brng_bru():
            data = {

            }
            f = open('barang.json','r')
            data = load(f)
            name = nama_barang.get()
            price = Harga_barang.get()
            code = str(kode_barang.get())
            quantity = Jumlah_barang.get()

            data[code] = {
                'Nama' : name,
                'Harga' : price,
                'jumlah' : quantity

            }

            print (data)

            with open('barang.json','w') as d:
                dump(data,d)




        Button(msk_brng,text='SAVE !!',command=msk_brng_bru).grid(row=5,column=2)


    def ubah_kode_barang():
        ubh_kde = Toplevel(window)
        Label(ubh_kde,text='Kode barang yang akan di hapus \t : ').grid(row=1,column=1)
        kode_barang = StringVar()
        Entry(ubh_kde,textvariable=kode_barang).grid(row=2,column=1)

        def ubh_kde_brng():
            f = open('barang.json','r')
            data = {

            }
            data = load(f)
            code = kode_barang.get()

            data.pop(code,None)
            with open('barang.json' , 'w') as d:
                dump(data,d)



        Button(ubh_kde,text='SAVE!',command=ubh_kde_brng).grid(row=2,column=2)

    def ubah_jumlah_stock():
        ubah_jmlh_stck1 = Toplevel(window)
        Label(ubah_jmlh_stck1,text='Kode barang \t : ').grid(row=1,column=1)
        kode_barang= StringVar()
        Entry(ubah_jmlh_stck1,textvariable=kode_barang).grid(row=1,column=2)
        def new():
            new = Toplevel(window)
            code = kode_barang.get()


            f = open('barang.json','r+')
            data = load(f)
            stock_old = data[code]['jumlah']
            Label(new,text='jumlah stock sekarang : ').grid(row=1,column=1)
            Label(new,text=stock_old).grid(row=1,column=2)
            Label(new,text='jumlah stock baru : ').grid(row=2,column=1)
            stock_new = IntVar()
            Entry(new,textvariable=stock_new).grid(row=2,column=2)

            def save():
                updt = stock_new.get()
                f = open('barang.json','r')
                data = load(f)
                name = data[code]['Nama']
                price = data[code]['Harga']
                data[code] = {
                    'Nama' : name,
                    'Harga' : price,
                    'Jumlah' : updt

                }
                with open('barang.json','w') as d:
                    dump(data,d)

            Button(new,text='SAVE!!',command=save).grid(row=3,column=2)

        Button(ubah_jmlh_stck1,text='OK',command=new).grid(row=2,column=2)

    def ubah_harga():
        ubh_hrga = Toplevel(window)
        Label(ubh_hrga,text='Kode barang \t : ').grid(row=1,column=1)
        kode_barang= StringVar()
        Entry(ubh_hrga,textvariable=kode_barang).grid(row=1,column=2)
        def new():
            new = Toplevel(window)
            code = kode_barang.get()


            f = open('barang.json','r+')
            data = load(f)
            stock_old = data[code]['Harga']
            Label(new,text='Harga sekarang : ').grid(row=1,column=1)
            Label(new,text=stock_old).grid(row=1,column=2)
            Label(new,text='Harga baru : ').grid(row=2,column=1)
            stock_new = IntVar()
            Entry(new,textvariable=stock_new).grid(row=2,column=2)

            def save():
                updt = stock_new.get()
                f = open('barang.json','r')
                data = load(f)
                name = data[code]['Nama']
                Stock = data[code]['jumlah']
                data[code] = {
                    'Nama' : name,
                    'Harga' : updt,
                    'Jumlah' : Stock

                }
                with open('barang.json','w') as d:
                    dump(data,d)

            Button(new,text='SAVE!!',command=save).grid(row=3,column=2)

        Button(ubh_hrga,text='OK',command=new).grid(row=2,column=2)




    Label(tab1,text='SELAMAT DATANG DI TOKO TERANG JAYA',font=('cabari',25,'bold')).grid(column=0,row=1,columnspan=11)

    Button(tab1,text='MASUKAN BARANG BARU',command=masukan_barang_baru).grid(row=3,column=0,padx=30,pady=20)
    Button(tab1,text='HAPUS BARANG',command=ubah_kode_barang).grid(row=5,column=0,padx=30,pady=20)
    Button(tab1,text='UBAH JUMLAH STOCK',command=ubah_jumlah_stock).grid(row=7,column=0,padx=30,pady=20)
    Button(tab1,text='UBAH HARGA BARANG',command=ubah_harga).grid(row=9,column=0,padx=30,pady=20)

    def buat_list_stock():
        now = datetime.now()

        b = str(now.strftime("%x"))

        q = str(now) +  ' LIST HARGA DAN STOCK BARANG.pdf'

        styles = getSampleStyleSheet()
        report = SimpleDocTemplate(f'report/LIST HARGA DAN STOCK BARANG.pdf')
        report_title = Paragraph("LIST HARGA DAN STOCK BARANG", styles["h1"])
        report.title = (str(now))
        report.build([report_title])

        fruit = {

        }

        f = open('barang.json','r')

        fruit = load(f)

        table_data = []
        for k, v in fruit.items():
            table_data.append([k, v])


        report_table = Table(data=table_data)
        report.build([report_title, report_table])
        from reportlab.lib import colors

        table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
        report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
        report.build([report_title, report_table])

        new = Toplevel(window)
        Label(new,text='List sudah dibuat di \n C:\github\Tkinter\KasirToko(GUI)\Report').grid(column=1,row=1)
        def del_new():
            del new

        Button(new,text='OK',).grid(row=2,column=1)


    def buat_login_save():
        now = datetime.now()

        q = str(now) +  ' LIST HARGA DAN STOCK BARANG.pdf'

        styles = getSampleStyleSheet()
        report = SimpleDocTemplate('report/LOGIN SAVE INFO.pdf')
        report_title = Paragraph("LOGIN SAVE INFO", styles["h1"])
        report.title = (str(now))
        report.build([report_title])

        fruit = {

        }

        f = open('login_info.json','r')

        fruit = load(f)

        table_data = []
        for k, v in fruit.items():
            table_data.append([k, v])


        report_table = Table(data=table_data)
        report.build([report_title, report_table])
        from reportlab.lib import colors

        table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
        report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
        report.build([report_title, report_table])
        new = Toplevel(window)
        Label(new,text='List sudah dibuat di \n C:\github\Tkinter\KasirToko(GUI)\Report').grid(column=1,row=1)
        def del_new():
            del new
        Button(new,text='OK').grid(row=2,column=1)


    def laporan_pembelian():
        now = datetime.now()

        b = str(now.strftime("%x"))

        q = str(now) +  ' LIST HARGA DAN STOCK BARANG.pdf'

        styles = getSampleStyleSheet()
        report = SimpleDocTemplate(f'report/LAPORAN PEMBELIAN.pdf')
        report_title = Paragraph("PEMBELIAN HARI INI", styles["h1"])
        report.title = (str(now))
        report.build([report_title])

        fruit = {

        }

        f = open('pembelian.json','r')

        fruit = load(f)

        table_data = []
        for k, v in fruit.items():
            table_data.append([k, v])


        report_table = Table(data=table_data)
        report.build([report_title, report_table])
        from reportlab.lib import colors

        table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
        report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
        report.build([report_title, report_table])

        new = Toplevel(window)
        Label(new,text='List sudah dibuat di \n C:\github\Tkinter\KasirToko(GUI)\Report').grid(column=1,row=1)
        def del_new():
            del new

        Button(new,text='OK',).grid(row=2,column=1)





    Button(tab1,text='BUKA MESIN KASIR{BETA}').grid(row=3,column=2,padx=30,pady=20)
    Button(tab1,text='BUAT LIST STOCK DAN HARGA',command=buat_list_stock).grid(row=5,column=2,padx=30,pady=20)
    Button(tab1,text='BUAT LAPORAN PEMBELIAN',command=laporan_pembelian).grid(row=7,column=2,padx=30,pady=20)
    Button(tab1,text='BUAT LOGIN SAVE INFO',command=buat_login_save).grid(row=9,column=2,padx=30,pady=20)

    def lapor_pembelian():
        new = Toplevel(window)
        Label(new,text='Kode barang yang di beli : ').grid(row=1,column=1)
        kode_barang = StringVar()
        Entry(new,textvariable=kode_barang).grid(row=1,column=2)
        Label(new,text='Jumlah barang yang di beli : ').grid(row=2,column=1)
        jumlah_dibeli = IntVar()
        Entry(new,textvariable=jumlah_dibeli).grid(row=2,column=2)

        def lapor_pembelian_main():
            code = kode_barang.get()
            quantity = jumlah_dibeli.get()
            f = open('barang.json','r')
            data = {}
            data = load(f)
            jumlah_awal = data[code]["jumlah"]
            name = data[code]["Nama"]
            price = data[code]['Harga']

            if quantity < jumlah_awal :
                jumlah_akhir = jumlah_awal - quantity
                data[code] = {
                    'Nama' : name,
                    'Harga' : price,
                    'jumlah' : jumlah_akhir
                }

                k = open('pembelian.json','r+')
                report = {}
                report = load(k)
                harga_report = price * quantity
                now = str(datetime.now())
                report[now] = {
                    'Kode' : code,
                    'Nama' : name,
                    'Jumlah Beli' : quantity,
                    'Total Harga' : harga_report

                }
                with open('pembelian.json','w') as g:
                    dump(report,g)
                with open('barang.json','w') as d:
                    dump(data,d)
            else :
                error = Tk()
                Label(error,text='Jumlah Tidak Cukup Gengsss')
        Button(new,text='OK',command=lapor_pembelian_main).grid(row=3,column=2)



    Button(tab1,text='LAPOR PEMBELIAN',command=lapor_pembelian).grid(row=3,column=6,padx=30,pady=20)
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
    Button(tab2,text="Register").grid(row=1,column=1,sticky='w')
    Label(tab2,text='Restart App \t \t :',font=('arial',10)).grid(row=2,column=0,sticky='w')
    Button(tab2,text='Restart',command=restart).grid(row=2,column=1,sticky='w')
    Label(tab2,text='Quit\t \t \t :',font=('arial',10)).grid(row=3,column=0,sticky='w')
    Button(tab2,text='QUIT!',command=quit).grid(row=3,column=1,sticky='w')



    """
    Label(tab2,text='Font Size \t \t :',font=('arial',10)).grid(row=4,column=0)
    font_size = IntVar()
    fz = Entry(tab2, textvariable=font_size).grid(column=1,row=4)

    def change():
        f = open('font.json','r')
        m = font_size.get()
        data = {

        }
        data= load(f)
        data['font'] = {
            'font' : 'Arial',
            'font_size' : m
        }

        with open('font.json','w') as g:
            dump(data,g)




    Button(tab2,text='Change!',command=change).grid(column=4,row=4)

    h = open('font.json','r')
    l = {

    }
    l = load(h)
    s = l["font"]["font_size"]"""
    s = 15
    sapa5 =Label(tab1,text='Halo Workers',font=('arial',s)).grid(row=4,column=8)
    sapa4 =Label(tab1,text='Jangan lupa cuci jangan \n dan jaga kebersihan',font=('arial',s)).grid(row=5,column=8)
    sapa3 =Label(tab1,text='Stay Safe and Healty... \n jangan Lupa berdoa juga ya ',font=('arial',s)).grid(row=6,column=8)

    sapa2 =Label(tab1,text=selamat,font=('arial',s)).grid(row=7,column=8)
    sapa1 =Label(tab1,text=semangat,font=('arial',s)).grid(row=9,column=8)

'''
log = Tk()
log.geometry('300x200')
app = False
Label(log,text='Please enter your \n username and password below :').pack()
Label(log,text='Username :').pack()
username_given = StringVar()
Entry(log,textvariable=username_given).pack()
Label(log,text='Password :').pack()
password_given = StringVar()
Entry(log,textvariable=password_given,show='*').pack()

user_given = username_given.get()
pass_given = password_given.get()

def check():
    global Home
    user = open('user.json','r+')
    username_aviable = {}
    username_aviable = load(user)

    for key,value  in username_aviable.items():
        username = key
        password = value

    if user_given in username:
        if pass_given in password :
            Home()
        else:
            pass
    else :
        pass
Button(log,text='LOGIN',command=check).pack()
'''
Home()

mainloop()
