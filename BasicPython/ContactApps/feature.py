from json import load, dump
from os import system
from getpass import getpass
from time import sleep

fileUser = 'user.json'
fileContact = 'contact.json'

user = {}
contact = {}

def loadData():
	global user, contact

	with open(fileUser) as f:
		user = load(f)

	with open(fileContact) as f:
		contact = load(f)

	return True

def saveData():
	global user, contact

	with open(fileUser, 'w') as f:
		dump(user, f)

	with open(fileContact, 'w') as f:
		dump(contact, f)

	return True

def login():
	counter = 1
	Username = input('Enter Username : ')
	Password = getpass('Enter Password : ')
	dataCheck = False
	passLogin = False
	if Username in user:
		dataCheck = True
		passLogin = (user[Username] == Password)

	while (not dataCheck) or (not passLogin):
		counter += 1
		if counter > 3:
			return False
		print('Combination Username and Password is Wrong')
		Username = input('Enter Username : ')
		Password = getpass('Enter Password : ')
		if Username in user:
			dataCheck = True
			passLogin = (user[Username] == Password)
	else:
		print('Login Pass')
		return True

def print_menu():
	print('Welcome to Contact Apps')
	print('1. Print Contact')
	print('2. Add A Contact')
	print('3. Remove A Contact')
	print('4. Lookup A Contact')
	print('Q. Quit')

def print_contact():
	if len(contact) > 0:
		for info in contact:
			print(f'Name \t: {info}\t Phone \t: {contact[info]}')
	else:
		print('There is no contact available right now.')

def add_contact():
	print('Add your contact\n')

	name = input('Name \t:')
	phone = input('Phone \t:')

	contact[name] = phone
	saveData()
	print('Saving Data ...')
	sleep(1.5)
	print('Data Saved.')

def remove_contact():
	print('Remove a contact\n')

	name = input('Name \t:')

	if name in contact:
		del contact[name]
		saveData()
		print('Removing Data ...')
		sleep(1.5)
		print('Data Saved.')
	else:
		print(f'{name} doesnot exists in contact')

def lookup_contact():
	print('Lookingup a contact\n')

	name = input('Name \t:')

	if name in contact:
		print(f'Name \t: {name}\t Phone \t:{contact[name]}')
	else:
		print(f'{name} doesnot exists in contact')	


	