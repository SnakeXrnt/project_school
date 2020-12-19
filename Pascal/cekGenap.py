
def cekGenap(number):
    if number % 2 == 0:
        return True
    else:
        return False

def main():
    myNumber = 10
    if cekGenap(myNumber):
        print('Genap!')
    else:
        print('Ganjil!')

main()    
