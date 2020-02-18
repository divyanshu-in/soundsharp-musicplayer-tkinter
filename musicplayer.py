import pygame
from tkinter import Listbox
from tkinter import PhotoImage
import os
from tkinter.filedialog import *
from PIL import Image

par = 1
playlist = []

root = Tk()
root.title("soundsharp")
root.state("iconic")

#commands assigned to buttons
def select_dir():
    directory = askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):
        if files.endswith("mp3"):
            playlist.append(files)

    for t in playlist:
        listbox.insert(0, t)
        
def play(): 
    global par
    par += 1
    if (par%2 ==1):
        bt1.config(image=ps)
        bt1.image = ps
    else:
        bt1.config(image=pl)
        bt1.image = pl

    b = listbox.curselection()[0]
    global i
    i = len(playlist) - b - 1
    pygame.mixer.pre_init(44100,-16,2, 1024)
    pygame.mixer.init()
    pygame.mixer.music.load(playlist[i])
    pygame.mixer.music.play()
def nxt():
    global i 
    i -= 1
    pygame.mixer.pre_init(44100,-16,2, 1024)
    pygame.mixer.init()
    pygame.mixer.music.load(playlist[i])
    pygame.mixer.music.play()
def prev():
    global i 
    i += 1
    pygame.mixer.pre_init(44100,-16,2, 1024)
    pygame.mixer.init()
    pygame.mixer.music.load(playlist[i])
    pygame.mixer.music.play()
def pause():
    pygame.mixer.music.pause()
def stop():
    pygame.mixer.music.stop()

#symbols to be displayed on button
playImage = PhotoImage(file = "./play.png")
nextImage = PhotoImage(file = "./next.png")
prevImage = PhotoImage(file = "./priv.png")
listImage = PhotoImage(file = "./list.png")
exitImage = PhotoImage(file = "./exit.png")
pauseImage = PhotoImage(file = "./pause.png")

pl = playImage.subsample(3, 3)
ps = pauseImage.subsample(3, 3)
nx = nextImage.subsample(3,3);prv = prevImage.subsample(3,3)
lst = listImage.subsample(3, 3);pwr = exitImage.subsample(3,3)

#gui structure
bt1 = Button(root, text="play", command=play, image=pl)
bt1.config(height=40, width=40)
bt2 = Button(root, text="prev", image=prv, command=prev)
bt2.config( height=40, width=40)
bt3 = Button(root, text="next", image=nx, command=nxt)
bt3.config(height=40, width=40)
bt4 = Button(root, text="list", command=select_dir, image=lst)
bt4.config(height=40, width=40)
bt5 = Button(root, text="exit", image=pwr, command=root.destroy)
bt5.config(height=40, width=40)
bt1.grid(column=0, row=0, padx=2, pady=2);bt2.grid(column=1, row=0, padx=2, pady=2)
bt3.grid(column=2, row=0, padx=2, pady=2);bt4.grid(column=3, row=0, padx=2, pady=2)
bt5.grid(column=4, row=0, padx=2, pady=2)
listbox = Listbox(root, relief='sunken', width=30, height=20)
listbox.grid(row=1, columnspan=8)

root.mainloop()


