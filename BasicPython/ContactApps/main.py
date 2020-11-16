from os import system
from time import sleep

import feature

statusLoading = feature.loadData() #True

system('cls')

if statusLoading :
	#print('Pass')
	passLogin = feature.login() #True
	if passLogin:
		print('Welcome!')
		sleep(2)
		menu_choice = ''

		while menu_choice != 'q':
			system('cls')
			feature.print_menu()
			menu_choice = input('Type in a number : ').lower()

			if menu_choice == '1':
				feature.print_contact()
				input('ENTER to Exit')

			elif menu_choice == '2':
				feature.add_contact()
				input('ENTER to Exit')

			elif menu_choice == '3':
				feature.remove_contact()
				input('ENTER to Exit')

			elif menu_choice == '4':
				feature.lookup_contact()
				input('ENTER to Exit')

			elif menu_choice == 'q':
				break

			else: 
				print('Input Menu Choice Corectly')
				input('ENTER to Exit')

	else:
		print('Failed to login.')
else:
	print('Apps cannot run.')