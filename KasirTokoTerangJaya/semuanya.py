from json import *

data_stock = {}
with open('stock.json') as file:
	data_stock = load(file)

def laporpembelian():
	dibeli = input('Kode benda yang dibeli : ')
	if dibeli in data_stock:
		q = int(input('berapa jumlah barang tersebut dibeli : '))
		sisa_stock = data_stock[dibeli]['jumlah'] - q 
		data_stock[dibeli]['jumlah'] = sisa_stock
		p = data_stock[dibeli]['harga'] * q
		with open('stock.json', 'w') as file:
			dump(data_stock,file)

		with open('test.txt','a') as w:
			w.write(f'pendapatan dari {data_stock[dibeli]["barang"]} dengan jumlah {q} adalah Rp{p}')
			w.write('\n')

	else :
		print('maaf , stock tidak ada')

def addstock():
	#global data_stock
	kode = input('masukan kode barang : ')
	barang = input('masukan nama barang : ')
	jumlah = int(input('masukan jumlah : '))
	harga = int(input('masukan harga barang : '))
	data_stock[kode] = {
	'barang' : barang , 
	'jumlah' : jumlah , 
	'harga' : harga 
	}
	with open('stock.json', 'w') as file:
		dump(data_stock,file)

from getpass import *

def login():
    count = 0 
    while True: 
        userName = input("Hello! Welcome to Ebast app!, \n\nUsername: ") 
        password = getpass("Password: ")
        count += 1
        if count == 3: 
            #tells user bye
            break #exit
        else:
            if userName == 'Herman' and password == '2177':
                #let them in
                print("hello mr , welcome back")
                break #they are in, exit loop
            else:
                print("sorry wrong password")


data_stock = {}
with open('stock.json') as file:
	data_stock = load(file)

def showstock():
	barang = input('masukan kode barang yang ingin dicari')
	print(data_stock)
	if barang in data_stock :
		print(f'{data_stock[barang]["barang"]} ada {data_stock[barang]["jumlah"]}' )
	else :
		print("maaf , kode barang yang dimasukan salah ")

def updateharga():
	barang = input('update harga kode barang :')
	if barang in data_stock:
		print(f"harga lama : {data_stock[barang]['harga']}")
		stock = int(input('harga baru :'))
		data_stock[barang]['harga'] = stock 
		with open('stock.json', 'w') as file:
			dump(data_stock,file)
	else :
		print('maap , barang belum pernah di imput , silahkan kembali ke menu ita a dan tambah stock tersebut')
		input('tekan enter untuk kembali')

def updatestock():
	barang = input('update stock kode barang apa:')
	if barang in data_stock:
		print(f"stock lama : {data_stock[barang]['jumlah']}")
		stock = int(input('stock baru masuk :'))
		data_stock[barang]['jumlah'] = stock + data_stock[barang]['jumlah']
		with open('stock.json', 'w') as file:
			dump(data_stock,file)
	else :
		print('maap , barang belum pernah di input , silahkan kembali ke menu ita a dan tambah stock tersebut')
		input('tekan enter untuk kembali')