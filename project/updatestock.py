from json import *
data_stock = {}

with open('stock.json') as file:
	data_stock = load(file)

def updatestock():
	barang = input('update stock kode barang apa:')
	if barang in data_stock:
		print(f"stock lama : {data_stock[barang]['jumlah']}")
		stock = int(input('stock baru masuk :'))
		data_stock[barang]['jumlah'] = stock + data_stock[barang]['jumlah']
		with open('stock.json', 'w') as file:
			dump(data_stock,file)
	else :
		print('maap , barang belum pernah di imput , silahkan kembali ke menu ita a dan tambah stock tersebut')
		input('tekan enter untuk kembali')