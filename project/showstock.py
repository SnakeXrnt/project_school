from json import *


data_stock = {}
with open('stock.json') as file:
	data_stock = load(file)

def showstock():
	barang = input('masukan kode barang yang ingin dicari')
	print(f'{data_stock[barang]["barang"]} ada {data_stock[barang]["jumlah"]}' )


