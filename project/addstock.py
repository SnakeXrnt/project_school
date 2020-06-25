from json import load, dump

data_stock = {}

with open('stock.json') as file:
	data_stock = load(file)#membaca data




def addstock():
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