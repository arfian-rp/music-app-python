import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()
musicplayer.title("Arfian play music")
musicplayer.geometry("450x350")
directory = askdirectory()
os.chdir(directory)
songList = os.listdir()
playlist = tkr.Listbox(musicplayer, font="Cambria 14 bold", bg="cyan2", selectmode=tkr.SINGLE)
for item in songList:
    pos = 0
    playlist.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()

def play(): #play F
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def exitMusic(): #stop F
    pygame.mixer.music.stop()

def pause(): #pause F
    pygame.mixer.music.pause()

def resume(): #resume F
    pygame.mixer.music.unpause()


Btn_play = tkr.Button(musicplayer, height=2, width=7, text="play", font="Cambria 14 bold", command=play, bg="lime green", fg="black")
Btn_stop = tkr.Button(musicplayer, height=2, width=7, text="stop", font="Cambria 14 bold", command=exitMusic, bg="red", fg="black")
Btn_pause = tkr.Button(musicplayer, height=2, width=7, text="pause", font="Cambria 14 bold", command=pause, bg="yellow", fg="black")
Btn_resume = tkr.Button(musicplayer, height=2, width=7, text="resume", font="Cambria 14 bold", command=resume, bg="yellow", fg="black")

Btn_play.pack()
Btn_stop.pack()
Btn_pause.pack()
Btn_resume.pack()

playlist.pack(fill="both", expand="yes")
var = tkr.StringVar()
songTitle = tkr.Label(musicplayer, font="Cambria 12 bold", textvariable=var)
songTitle.pack()
musicplayer.mainloop()