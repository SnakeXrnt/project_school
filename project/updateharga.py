from json import *

data_stock = {}

with open('stock.json') as file:
	data_stock = load(file)

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