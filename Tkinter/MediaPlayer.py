from tkinter import Tk, Label, StringVar, ttk, Entry, Button
import pygame

pygame.mixer.init()

def play():
    pygame.mixer.music.load("halo.mp3")
    pygame.mixer.music.play(loops=0)

window = Tk()
window.title("Music")
#window.minsize(800, 600)
window.resizable(False, False)

header_apps = Label(window, text="Music", font=('Comic Sans MS', 20, 'bold'), bd=20, padx=20, pady=15 )
header_apps.grid(columnspan=3)

button_play = Button(window, font=('Comic Sans MS', 18, 'bold'), text='play', command=play)
button_play.grid(column=0, row=1)

button_pause = Button(window, font=('Comic Sans MS', 18, 'bold'), text='pause')
button_pause.grid(column=1, row=1)

window.mainloop()
