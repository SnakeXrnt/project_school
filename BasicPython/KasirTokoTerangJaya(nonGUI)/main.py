from os import *
from semuanya import *
login()
system('clear')

while 1 == 1:
	system('clear')
	print ("selamat datang")
	print ('1. lihat stock')
	print ('2. tambah stock')
	print ('3. lapor pembelian')
	print ('4. update harga barang')
	print ('5. update jumlah stock')
	print ('6. lihat pendapatan hari ini')

	print('menu :')
	user = int(input(''))

	if user == 1 :
		system('clear')
		showstock()
		input('tekan [ENTER] untuk kembali ke menu utama')
	elif user == 2:
		system('clear')
		addstock()
	elif user == 3:
		system('clear')
		laporpembelian()
	elif user == 4:
		system('clear')
		updateharga()
	elif user == 5:
		system('clear')
		updatestock()
