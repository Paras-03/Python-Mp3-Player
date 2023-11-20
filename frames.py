from tkinter import *
import re
from tkinter.filedialog import *

box = Listbox
number = []

def help():
    PATH = r"//Enter your path here//"
    h1 = " To be able to play songs : "
    step1 = "Step-1]   You can only play files \nwith .mp3 extension."

    step2 = f"Step-2]   You should store the \nsongs in the path :\n{PATH} ."

    step3 = "Step-3]   And then just run the \napp.py file and enjoy \nlistening music."


    root = Tk()
    root.title("Help")
    root.config(bg="black")
    root.geometry("400x400")
    root.resizable(width = False, height = False)

    _1 = Label(root, text=h1, bg="black", fg="white", font=("Arabia", 18, "bold"))
    _1.place(x=30, y=15)

    can1 = Canvas(root, bg="black", width=350, height=240)
    can1.place(x=25, y=70)

    __1 = Label(can1, bg="white", fg="black", text=step1, font=("Aria", 14, "bold"), width=27)
    __1.place(x=12, y=10)

    __2 = Label(can1, bg="white", fg="black", text=step2, font=("Aria", 14, "bold"), width=27)
    __2.place(x=12, y=70)

    __3 = Label(can1, bg="white", fg="black", text=step3, font=("Aria", 14, "bold"), width=27)
    __3.place(x=12, y=155)

    __4 = Button(root, bg="white", fg="black", text="Back", font=("Aria", 14, "bold"), width=8, height=2, command=lambda:root.destroy())
    __4.place(x=150, y=330)
    root.mainloop()

def play_list(song):
    global s
    songs = []
    s = song
    for x in s:
        song_name = split(x['name'])
        songs.append(song_name)
    s = songs

    root = Tk()
    root.title("Playlist")
    root.geometry("350x350")
    root.config(bg="black")
    root.title("PLAYLIST")
    root.resizable(width = False, height = False)

    _1 = Label(root, text="PLAY LIST : ", fg="white", bg="black", font=("Arabia", 18, "bold"))
    _1.place(x=90, y=10)

    _2 = Button(root, text="BACK", fg="white", bg="black", font=("Arabia", 14, "bold"), width=8, height=2, bd=10, command=lambda:root.destroy())
    _2.place(x=120, y=273)

    _3 = Button(root, text="ADD", fg="white", bg="black", font=("Arabia", 12, ""), width=4, height=2, bd=10, command=lambda:add(s))
    
    b = box(root, width=35, height=10, font=("Arabia", 12, "bold"), bg="black", fg="white")
    b.place(x=15, y=60)
    b.insert('end', "\n")

    a=1
    for x in songs:
        q = x
        q = re.split("[.]", q)
        name = q[0]

        text = f"{a}]   {name}."
        b.insert('end', text)
        b.insert('end', "\n")
        a=a+1
    root.mainloop()

def add(s):
    song=askopenfilenames()

def split(song):
    x = song
    v=0
    s = re.findall("[/]", song)
    for a in s:
        v=v+1

    s = re.split("[/]", song)
    song_name = s[v]
    return song_name

def play_from_list(song):
    global __2
    songs = []
    s = song
    for x in s:
        song_name = split(x['name'])
        songs.append(song_name)

    root = Tk()
    root.title("Playlist")
    root.geometry("350x405")
    root.config(bg="black")
    root.title("PLAY FROM")
    root.resizable(width = False, height = False)

    _1 = Label(root, text="PLAY LIST : ", fg="white", bg="black", font=("Arabia", 18, "bold"))
    _1.place(x=90, y=10)

    _3 = Canvas(root, width=280, height=60, bg="black")
    _3.place(x=20, y=275)
    
    __1 = Label(_3, text="Enter on of song to : \nbe played", bg="white", fg="black", font=("Arabia", 14, "bold"))
    __1.place(x=5, y=7)

    __2 = Entry(_3, width=3, font=("Arabia", 28, "bold"), justify="right")
    __2.place(x=210, y=7)

    _2 = Button(root, text="OK", fg="white", bg="black", font=("Arabia", 14, "bold"), width=5, height=1, bd=10, command=lambda:print1(__2, root))
    _2.place(x=130, y=350)
    
    b = box(root, width=35, height=10, font=("Arabia", 12, "bold"), bg="black", fg="white")
    b.place(x=15, y=60)
    b.insert('end', "\n")

    a=1
    for x in songs:
        q = x
        q = re.split("[.]", q)
        name = q[0]

        text = f"{a}]   {name}."
        b.insert('end', text)
        b.insert('end', "\n")
        a=a+1
    root.mainloop()

def print1(no, root):
    global number
    number.append(no.get())
    root.destroy()
    root.quit()
    return
