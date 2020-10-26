from tkinter import Tk, Label, StringVar, ttk, Entry, Button

def calculate():
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


window = Tk()
window.title("Converter Temperature")
#window.minsize(800, 600)
window.resizable(False, False)

header_apps = Label(window, text="TEMPERATUR KONVERTER", font=('arial', 20, 'bold'), bd=20, padx=20, pady=15 )
header_apps.grid(columnspan=3)

label_from = Label(window, text="FROM", font=('arial', 18, 'bold') , justify="left", bd=20, padx=10, pady=15)
label_from.grid(column = 0, row=1)

label_value = Label(window, text="VALUE", font=('arial', 18, 'bold') , justify="left", bd=20, padx=10, pady=15)
label_value.grid(column = 1, row=1)

label_process = Label(window, text="PROCESS", font=('arial', 18, 'bold') , justify="left", bd=20, padx=10, pady=15)
label_process.grid(column = 2, row=1)

suhu = StringVar()
combo_suhu = ttk.Combobox(window, textvariable=suhu, font=('arial', 18, 'bold'), width=8)
combo_suhu.grid(column = 0, row = 2)
combo_suhu.current(0)

nilai_suhu = StringVar()
entry_nilai_suhu = Entry(window, textvariable=nilai_suhu, font=('arial', 18, 'bold'), width=8)
entry_nilai_suhu.grid(column=1, row=2)

button_process = Button(window, font=('arial', 18, 'bold'), text='OK!', command=calculate)
button_process.grid(column=2, row=2)

label_to = Label(window, text="TO", font=('arial', 18, 'bold') , justify="left", bd=20, padx=10, pady=15)
label_to.grid(column = 0, row=3)

label_result = Label(window, text="RESULT", font=('arial', 18, 'bold') , justify="left", bd=20, padx=10, pady=15)
label_result.grid(column = 1, row=3)

toSuhu =StringVar()
combo_toSuhu = ttk.Combobox(window, textvariable=toSuhu, font=('arial', 18, 'bold'), width=8)
combo_toSuhu['values'] = ['F', 'C', 'R', 'K']
combo_toSuhu.grid(column = 0, row = 4)
combo_toSuhu.current(0)

label_val_res = Label(window, text="0", font=('arial', 18, 'bold') , justify="left", bd=20, padx=10, pady=15)
label_val_res.grid(column = 1, row=4)

window.mainloop()
