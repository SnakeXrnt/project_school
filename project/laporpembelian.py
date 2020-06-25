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