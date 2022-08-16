import pygame 
import time # An included library with Python install.
from tkinter import Listbox 
from tkinter import PhotoImage
import os 
from tkinter.filedialog import *
from PIL import Image 
from tkinter import Tk, Button
import sys
from pygame import mixer
pygame.mixer.init()
from tkinter import messagebox



par = 1
playlist = []

player = Tk()
player.title("Music Player") #name of the program when you run it
player.state("iconic")
# player.iconbitmap("./logo.ico") # if you get an error on this line, just delete this whole line
messagebox.showinfo("MusicPlayer", "To play some music, first click the plus then navigate to a folder on your computer which has music in it then click open.\n\nThen just click one of the songs from the lsit below and click play")

#commands assigned to buttons
def select_dir():
    directory = askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):
        if files.endswith("mp3"):
            playlist.append(files)

    for t in playlist:
        listbox.insert(0, t)



        
        
def play_music():
    b = listbox.curselection()[0]
    global i
    i = len(playlist) - b - 1
    global paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        stop_music()
        time.sleep(1)
        pygame.mixer.music.load(playlist[i])
        pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


paused = False


def pause_music():
    global paused
    paused = True
    pygame.mixer.music.pause()


"""NEED THIS"""
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



#symbols to be displayed on button
playImage = PhotoImage(file = "./icons/play.png")
nextImage = PhotoImage(file = "./icons/next.png")
prevImage = PhotoImage(file = "./icons/priv.png")
listImage = PhotoImage(file = "./icons/list.png")
exitImage = PhotoImage(file = "./icons/exit.png")
pauseImage = PhotoImage(file = "./icons/pause.png")
stopImage = PhotoImage(file = "./icons/stop.png")

pl = playImage.subsample(3, 3)
ps = pauseImage.subsample(3, 3)
nx = nextImage.subsample(3,3);prv = prevImage.subsample(3,3)
lst = listImage.subsample(3, 3);pwr = exitImage.subsample(3,3)
st = stopImage.subsample(3, 3)

#gui structure
bt1 = Button(player, text="play", command=play_music, image=pl)
bt1.config(height=40, width=40)
bt2 = Button(player, text="pause", command=pause_music, image=ps)
bt2.config(height=40, width=40)
bt3 = Button(player, text="prev", image=prv, command=prev)
bt3.config( height=40, width=40)
bt4 = Button(player, text="next", image=nx, command=nxt)
bt4.config(height=40, width=40)
bt5 = Button(player, text="stop", image=st, command=stop_music)
bt5.config(height=40, width=40)
bt6 = Button(player, text="list", command=select_dir, image=lst)
bt6.config(height=40, width=40)
bt7 = Button(player, text="exit", image=pwr, command=sys.exit)
bt7.config(height=40, width=40)
bt1.grid(column=0, row=0, padx=2, pady=2);bt2.grid(column=1, row=0, padx=2, pady=2)
bt3.grid(column=2, row=0, padx=2, pady=2);bt4.grid(column=3, row=0, padx=2, pady=2)
bt5.grid(column=4, row=0, padx=2, pady=2);bt6.grid(column=5, row=0, padx=2, pady=2)
bt7.grid(column=6, row=0, padx=2, pady=2)
listbox = Listbox(player, relief='sunken', width=30, height=20)
listbox.grid(row=1, columnspan=8)


player.mainloop()
