database = {
    '0811' : 'Telkomsel',
    '0812' : 'Telkomsel',
    '0815' : 'Indosat',
    '0817' : 'XL',
    '0831' : 'Axis',
    '0899' : 'Tri'
}
 
def isIndonesiaMobilePhoneNumber(text):
    if not (len(text) == 12 or len(text) == 11 or len(text) == 10):
        return False

    if text[0] == '+':
        for i in range(1, len(text)):
            if not text[i].isdecimal(): # decimal untuk ngecek karakter yang dilihat itu angka atau bukan
                return False
    else:
        for i in range(len(text)):
            if not text[i].isdecimal():
                return False

    if not (text[0:2] == '08' or text[0:4] == '+628'):
        return False

    checkProvider(text)
    return True

def checkProvider(text):
    prefix = text[0:4]
    if prefix in database:
        print(database[prefix])
    else:
        print('Unknown Source')

print('\n081234521234 a phone number')
print(isIndonesiaMobilePhoneNumber('081234521234'))

print('\nabn234521234 a phone number')
print(isIndonesiaMobilePhoneNumber('abn234521234'))
