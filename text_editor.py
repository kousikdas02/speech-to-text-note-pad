from tkinter import *
from tkinter import filedialog
import speech_recognition as sr
import pyaudio
from gtts import gTTS
import playsound
import pyttsx3
from recordfile import recordaudio
from googletrans import Translator



fname = ''


root = Tk()
root.title("Speech to text editor")
root.config(background='black')
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)
#root.wm_iconbitmap("magichat.ico")

txt = Text(root, width=500, height=500, background='white', foreground='black',font='Arial 14 bold')
txt.pack()
translator = Translator



def NewFile():
    global fname
    fname='Untitled'
    txt.delete(0.0,END)


def OpenFile():
    global fname
    fname = filedialog.askopenfilename()
    f = open(fname, mode='r')
    root.title("Das-text_editor "+fname)
    t = f.read()
    txt.delete(0.0, END)
    txt.insert(0.0, t)


def SaveFile():
    f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    print(f)
    t = txt.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        tkinter.messagebox.showerror(title="Error", message='Could not save file')


def save_f():
    global fname
    t = txt.get(0.0, END)
    print(fname)
    if fname == '':
        SaveFile()
    else:
        f = open(fname, 'w')
        f.write(t)
        f.close()


def sp_recog():
    r = sr.Recognizer()
    audio = filedialog.askopenfilename()
    with sr.AudioFile(audio) as source:
        txt_audio = r.record(source)
    t = (str(r.recognize_google(txt_audio)))
    txt.insert(END,t)


def mic():
        recordaudio()
        r = sr.Recognizer()
        audio =  "E:\\College Project\\Text Editor\\file.wav"
        with sr.AudioFile(audio) as source:
            txt_audio = r.record(source)
        t = (str(r.recognize_google(txt_audio)))
        txt.insert(END,t)


def narratee():
    engine = pyttsx3.init(driverName='sapi5')
    t = txt.get(0.0,END)
    engine.setProperty('rate', 120)
    engine.say(t)
    engine.runAndWait()


def convert():
    recordaudio()
    r = sr.Recognizer()
    audio = "E:\\College Project\\Text Editor\\file.wav"
    with sr.AudioFile(audio) as source:
        txt_audio = r.record(source)
    t=(str(r.recognize_google(txt_audio)))
    a=translator.translate(t,src='en',dest='hi')
    txt.insert(END,a.text)


mbar = Menu(root)
menc = Menu(mbar)
menc.add_command(label ="New File", command=NewFile)
menc.add_command(label ="Open File", command=OpenFile)
menc.add_command(label ="Save As", command=SaveFile)
menc.add_command(label ="Save File", command=save_f)
menc.add_command(label ="Audio Mode", command=sp_recog)
menc.add_command(label ="Microphone Mode", command=mic)
menc.add_command(label ="Narrate", command=narratee)
# menc.add_command(label ="Hindi Coverter", command=convert)
# menc.add_command(label ="Close", command=root.close)

mbar.add_cascade(label='Menu', menu=menc)

root.config(menu=mbar)
print(fname)
root.mainloop()