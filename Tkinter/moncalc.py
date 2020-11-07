from tkinter import Tk, Label, StringVar, ttk, Entry, Button , LabelFrame , Menu , Frame

def calculate():
	global mainFrame
	suhuFrom = suhu.get()
	suhuTo = toSuhu.get()
	nilai = int(nilai_suhu.get())
	additionalFrom = 0
	additionalTo = 0
	if suhuFrom == 'C':
		suhuFrom = 5
	elif suhuFrom == "F":
		suhuFrom = 9
		additionalFrom = -32
	elif suhuFrom == "R":
		suhuFrom = 4
	elif suhuFrom == "K":
		suhuFrom = 5
		additionalFrom = -273

	if suhuTo == 'C':
		suhuTo = 5
	elif suhuTo == "F":
		suhuTo = 9
		additionalTo = 32
	elif suhuTo == "R":
		suhuTo = 4
	elif suhuTo == "K":
		suhuTo = 5
		additionalTo = 273

	result = ((suhuTo/suhuFrom)*(nilai+additionalFrom))+additionalTo

	label_val_res.config(text=str(result))
	del mainFrame

def close():
	window.quit()
	window.destroy()
	exit()



window = Tk()
window.title("Converter Temperature")
#window.minsize(800, 600)
window.resizable(False, False)

tabControl = ttk.Notebook(window)
tab1 = Frame(tabControl)
tab2 = Frame(tabControl)
tam3 = Frame(tabControl)
tabControl.add(tab1, text='Suhu')
tabControl.add(tab2, text='rectangle')
tabControl.add(tab3,text='Calculator Custom')
tabControl.pack(expand=1,fill='both')


#membuat menu Baru
menu_bar = Menu(window)
window.config(menu=menu_bar)

label_menu_file = Menu(menu_bar)

label_menu_file.add_command(label='NewProgram')
label_menu_file.add_command(label='close',command=close)
menu_bar.add_cascade(label='File',menu=label_menu_file)



label_help_menu = Menu(menu_bar,tearoff=0)
label_help_menu.add_command(label='HELP')
label_help_menu.add_command(label='ABOUT')
menu_bar.add_cascade(label='Help',menu=label_help_menu)



mainFrame = LabelFrame(tab1, text='TemperatureCalculator')
mainFrame.grid(column=0,row=0)

Frame2 = LabelFrame(tab2 , text='RectangleCalculator')
Frame2.grid(column=0,row=0)


header_apps = Label(mainFrame, text="TEMPERATUR KONVERTER", font=('arial', 20, 'bold') )
header_apps.grid(columnspan=3)

label_from = Label(mainFrame, text="FROM", font=('arial', 18, 'bold') , justify="left")
label_from.grid(column = 1, row=2)

label_value = Label(mainFrame, text="VALUE", font=('arial', 18, 'bold') , justify="left")
label_value.grid(column = 3, row=2)

label_process = Label(mainFrame, text="PROCESS", font=('arial', 18, 'bold') , justify="left")
label_process.grid(column = 5, row=2)

suhu = StringVar()
combo_suhu = ttk.Combobox(mainFrame, textvariable=suhu, font=('arial', 18, 'bold'), width=8)
combo_suhu.grid(column = 1, row = 3)
combo_suhu['values'] = ['F', 'C', 'R', 'K']

nilai_suhu = StringVar()
entry_nilai_suhu = Entry(mainFrame, textvariable=nilai_suhu, font=('arial', 18, 'bold'), width=8)
entry_nilai_suhu.grid(column=3, row=3)

button_process = Button(mainFrame, font=('arial', 18, 'bold'), text='OK!', command=calculate)
button_process.grid(column=5, row=3)

label_to = Label(mainFrame, text="TO", font=('arial', 18, 'bold') , justify="left")
label_to.grid(column = 2, row=2)

label_result = Label(mainFrame, text="RESULT", font=('arial', 18, 'bold') , justify="left")
label_result.grid(column = 4, row=2)

toSuhu =StringVar()
combo_toSuhu = ttk.Combobox(mainFrame, textvariable=toSuhu, font=('arial', 18, 'bold'), width=8)
combo_toSuhu['values'] = ['F', 'C', 'R', 'K']
combo_toSuhu.grid(column = 2, row = 3)
combo_toSuhu.current(0)

label_val_res = Label(mainFrame, text="0", font=('arial', 18, 'bold') , justify="left")
label_val_res.grid(column = 4, row=3)
