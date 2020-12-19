from json import *

f = open('barang.json','r+')

data = {

}

data = load(f)

v = input('CODE : ')

print(data[v]['jumlah'])
