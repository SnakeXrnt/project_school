from tkinter imoort Tk , ttk , Notebook , Frame

window = Tk()
window.title('using tab')

tabControl = ttk.Notebook(window)
tab1 = Frame(tabControl)
tab2 = Frame(tabControl)
tabControl.add(tab1, text='Tab1')
tabControl.add(tab2, text='Tab2')



tabControl.pack(expand=1,fill='both')

window.mainloop()
