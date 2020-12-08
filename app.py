import vlc
import os
from time import *
import re
from tkinter import *
from tkinter import messagebox
from mutagen.mp3 import MP3
from threading import Thread
from frames import help, play_list, about, play_from_list, number

PATH = "PATH TO MP FILES\\"
#files = filedialog.askopenfilenames()
song = os.listdir(PATH)
songs = []
b=0
a = 0

current = 0

for s in song:
    songs.append(
        {'no' : a,
         'name' : s
            })
    a = a + 1
total = a

status = ""
exist = False
is_playing = False
stoped = False
mute = False

def threadmethod():
    elapsed_time = 0
    volume = 50
    global status, player, is_playing, songs, size, number
    global instance, current, stoped, total, song, mute, b

    while True:

        if status == "Play_from":
            try:
                number = int(number[b])-1
                b=b+1
                for x in songs:
                    if number == x['no']:
                        current = number
                        status = "Play"
                        break
                else:
                    messagebox.showinfo(message="Invalid Song number", icon="error")
                    current=0
                    status = "Play"

            except (ValueError):
                messagebox.showinfo(message="Enter the song number", icon="error")
                quit()

        elif status == "Unmute":
            mute = False
            player.audio_set_volume(volume)

        elif status == "Resume":
            is_playing = True
            status = ""
            player.pause()

        elif status == "Play":
            elapsed_time = 0
            is_playing = True
            stoped = False
            song = songs[current]['name']
            player = vlc.MediaPlayer(PATH + song)
            instance = MP3(PATH+song)
            change()
            size = instance.info.length

            sleep(2)
            track_length = size
            player.audio_set_volume(volume)
            player.play()
            status = ""

        elif status == "Mute":
            mute = True
            player.audio_set_volume(0)
            status = ""

        elif status == "Next":
            player.stop()
            sleep(2)
            if current+1 < total:
                current = current + 1
                
            else:
                current = 0
                
            song = songs[current]['name']
            player = vlc.MediaPlayer(PATH + song)
            instance = MP3(PATH+song)
            size = instance.info.length
            status = "Play"

        elif status == "Previous":
            player.stop()
            sleep(2)
            current = current - 1
            song = songs[current-1]['name']
            player = vlc.MediaPlayer(PATH + song)
            instance = MP3(PATH+song)
            size = instance.info.length
            status = "Play"

        elif status == "Pause":
            is_playing = False
            status = ""
            player.pause()

        elif status == "Stop":
            is_playing = False
            change()
            stoped = True
            status = ""
            player.stop()

        elif status == "Increase":
            volume = volume + 5
            player.audio_set_volume(volume)
            status = ""

        elif status == "Decrease":
            volume = volume - 5
            player.audio_set_volume(volume)
            status = ""

        if is_playing:
            elapsed_time = elapsed_time + 0.1

            if elapsed_time >= track_length:

                if current+1 < total:
                    current = current + 1
                    
                else:
                    current = 0
                    
                song = songs[current]['name']
                player = vlc.MediaPlayer(PATH + song)
                instance = MP3(PATH+song)
                size = instance.info.length
                status = "Play"

        sleep(0.1)

def change():
    global root, instance, song

    can = Canvas(root, height=110, width=380, bg="black")
    can.place(x=11, y=55)

    if is_playing:
        try:
            x = song
            x = re.split("[.]", x)
            name = x[0]
            singer = instance['TPE1']
            album = instance['TALB']
        except:
            name = "DATA NOT FOUND"
            singer = "DATA NOT FOUND"
            album = "DATA NOT FOUND"
    else:
        name = "----------"
        singer = "----------"
        album = "----------"

    name = f"NAME : {name}"
    singer = f"SINGER : {singer}"
    album = f"ALBUM : {album}"

    _1 = Label(can, text=name, font=("Arabia", 16, "bold"), bg="white", fg="black")
    _1.place(x=5, y=5)

    _2 = Label(can, text=album, font=("Arabia", 16, "bold"), bg="white", fg="black")
    _2.place(x=5, y=40)

    _3 = Label(can, text=singer, font=("Arabia", 16, "bold"), bg="white", fg="black")
    _3.place(x=5, y=75)

    return

def join(operation):
    global exist, status, is_playing, stoped, mute, songs

    if exist == False:
        if operation == "Play_from":
            play_from_list(songs)
            status = operation

        else:
            status = operation
        a = Thread(target=threadmethod)
        print("Started")
        a.start()
        exist = True
        a.join(0.1)
        is_playing = True

    else:
        if mute:
            status = "Unmute"

        elif stoped:
            status = "Play"

        elif is_playing == False:
           if operation == "Play":
               status = "Resume"

        elif operation == "Play_from":
            song = play_from_list()
            status = operation

        else:
            status = operation
 
def main():
    global root
    global player, songs, size, current

    root = Tk()
    root.title("MP3 PLAYER")
    root.geometry("491x260")
    root.config(bg="black")
    root.resizable(width = False, height = False)
    
    change()
    __0 = Button(root, text="Playlist", width=10, bd=10, font=('', 11, ''), bg="black", fg="white", command=lambda:play_list(songs))
    __0.place(x=14, y=4)

    __1 = Button(root, text="Help", width=10, bd=10, font=('', 11, ''), bg="black", fg="white", command=lambda:help())
    __1.place(x=140, y=4)

    __2 = Button(root, text="About", width=10, bd=10, font=('', 11, ''), bg="black", fg="white", command=lambda:about())
    __2.place(x=266, y=4)

    can1 = Canvas(root, height=70, width=375, bg="black")
    can1.place(x=10, y=180)

    _1 = Button(can1, text="STOP", height=3, width=7, bd=10, bg="black", fg="white", command=lambda:join("Stop"))
    _1.place(x=4, y=1)

    _2 = Button(can1, text="PREV", height=3, width=7, bd=10, bg="black", fg="white", command=lambda:join("Previous"))
    _2.place(x=78, y=1)

    _3 = Button(can1, text="PLAY", height=3, width=7, bg="black", bd=10, fg="white", command=lambda:join("Play"))
    _3.place(x=152, y=1)

    _4 = Button(can1, text="PAUSE", height=3, width=7, bg="black", bd=10, fg="white", command=lambda:join("Pause"))
    _4.place(x=226, y=1)

    _5 = Button(can1, text="NEXT", height=3, width=7, bg="black", bd=10, fg="white", command=lambda:join("Next"))
    _5.place(x=300, y=1)

    can = Canvas(root, height=250, width=80, bg="black")
    can.place(x=400, y=4)

    __1 = Button(can, text="Play from\nPlaylist", height=3, width=8, bg="black", bd=7, fg="white", command=lambda:join("Play_from"))
    __1.place(x=5,y=5)
    _6 = Button(can, text="Volume\nIncrease", height=3, width=8, bg="black", bd=7, fg="white", command=lambda:join("Increase"))
    _6.place(x=5, y=70)
    
    _7 = Button(can, text="Mute", height=2, width=8, bg="black", bd=7, fg="white", command=lambda:join("Mute"))
    _7.place(x=5, y=135)

    _7 = Button(can, text="Volume\nDecrease", height=3, width=8, bg="black", bd=7, fg="white", command=lambda:join("Decrease"))
    _7.place(x=5, y=185)

    root.mainloop()

m = Thread(target=main)
m.start()
m.join()

