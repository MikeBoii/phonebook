from tkinter import *
from pygame import mixer
from tkinter import filedialog
import random


mixer.init()
root = Tk()

master_frame = Frame(root)
master_frame.pack()

info_frame = Frame(master_frame)
info_frame.grid(row=0, column=0)

controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0)

file_frame = Frame(master_frame)
file_frame.grid(row=0, column=5)

song_state = Label(info_frame, width=60, text="Choose song.", font="arial-bold")
song_state.grid(row=0, column=0)

song_box = Listbox(info_frame, width=60, selectbackground="green")
song_box.grid(row=1, column=0)

# Хэндлеры-заглушки, для демонстрации результата yes
def back_song():
    prev_s = song_box.curselection()
    prev_s = prev_s[0] - 1
    song = song_box.get(prev_s)
    mixer.music.load(song)
    mixer.music.play()
    song_box.selection_clear(END, 0)
    song_box.activate(prev_s)
    song_box.selection_set(prev_s, last=None)
    song_state['text'] = "Current Song:" , song
def next_song():
    next_s = song_box.curselection()
    next_s = next_s[0] + 1
    song = song_box.get(next_s)
    mixer.music.load(song)
    mixer.music.play()
    song_box.selection_clear(0, END)
    song_box.activate(next_s)
    song_box.selection_set(next_s, last=None)
    song_state['text'] = "Current Song:" , song
def play():
    song = song_box.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()
    song_state['text'] = "Current Song:" , song
def pause():
    song = song_box.get(ACTIVE)
    if song_state['text'] == "Paused":
        mixer.music.unpause()
        song_state['text'] ="Resumed Playing:" , song
    else:
        mixer.music.pause()
        song_state['text'] = "Paused"
def stop():
    mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    song_state['text'] = "Stopped the song"
def openfile():
    song = filedialog.askopenfilename(initialdir='tracks/', title="Выберите песню!", filetypes=(("mp3 Files", "*.mp3"),))
    k = -2
    for i in range(len(song)-1,0,-1):
        if song[i] == "/":
            k=i
            break
    name_short=song[k+1:]
    song_box.insert(END, name_short)
def random_s():
    x = random.randint(0,song_box.size()-1)
    song = song_box.get(x)
    mixer.music.load(song)
    mixer.music.play()
    song_box.activate(x)
    song_state['text'] = "Random Song:", song
def clear_s():
    clear = song_box.curselection()
    song = song_box.get(clear)
    song_box.delete(clear)
    mixer.music.stop()
    song_state['text'] = "Song:" , song , "has been removed."

# Создаем кнопки управления
back_button = Button(controls_frame, text="<-", width=10, height = 4, command=back_song , bg = "gray")
forward_button = Button(controls_frame, text="->", width=10, height = 4, command=next_song , bg = "gray")
play_button = Button(controls_frame, text="|>", width=10, height = 4, command=play , bg = "green")
pause_button = Button(controls_frame, text="||", width=5, height = 2, command=pause , bg = "orange")
stop_button = Button(controls_frame, text="[]", width=5, height = 2, command=stop , bg = "red")
rand_button = Button(controls_frame, text="?", width=5, command=random_s , bg = "blue")
delete_button = Button(controls_frame, text="X", width=5, command=clear_s , bg = "red")

back_button.grid(row=0, column=0)
forward_button.grid(row=0, column=4)
play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=3)
stop_button.grid(row=0, column=1)
rand_button.grid(row=0, column=5)
delete_button.grid(row=0, column=6)

openfile_button = Button(file_frame, width=10, height = 3, text="Enter Song", command=openfile ,bg = "green")

openfile_button.grid(row=1, column=0)

root.mainloop()