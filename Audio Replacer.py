#Audio Replacer, a GUI tool for replace audio track in mp4 video file using FFmpeg
from tkinter import *
import tkinter.filedialog
import os

root = Tk()
root.title("Audio Replacer 0.1")
root.geometry("400x120")

# ask FFmpeg to copy video and audio as input files and make a new container as output video file
def replace_audio():
    string = f"ffmpeg.exe -i {Ent1.get()} -i {Ent2.get()} -map 0:v -map 1:a -c:v copy {Ent3.get()}"
    os.system(string)
# open mp4 video file
def open_file():
    input_file_name= tkinter.filedialog.askopenfilename(defaultextension=".mp4",
                                       filetypes=[("*.mp4", "All Files"), ("*.mp4", "mp4 files" )])
    Ent1.insert(END, input_file_name)
    Ent3.insert(END, input_file_name)
# open wav audio file
def open_file2():
    input_file_name= tkinter.filedialog.askopenfilename(defaultextension=".wav",
                                       filetypes=[("*.wav", "All Files"), ("*.wav", "wav files" )])
    Ent2.insert(END, input_file_name)

# set button and entry frame for choose input video
x = StringVar()
frame1 =Frame(root)
frame1.pack(side= TOP)
But1 = Button(frame1, text= "Choose MP4", command= open_file)
But1.pack(side=LEFT)
Ent1 = Entry(frame1, width=50, textvariable= x)
Ent1.pack(side= LEFT)
# setbutton and entry frame for choose input audio
y = StringVar()
frame2 = Frame(root)
frame2.pack(side= TOP)
But2 = Button(frame2,text= "Choose WAV", command= open_file2)
But2.pack(side= LEFT)
Ent2 = Entry(frame2, width= 50, textvariable= y)
Ent2.pack(side= LEFT)
# add entry frame for choose output video file path
Label = Label(root, text= "Choose new output filename:")
Label.pack(side= TOP)
z = StringVar()
frame3 = Frame(root)
frame3.pack(side= TOP)
Ent3 = Entry(frame3, width= 50, textvariable= z)
Ent3.pack(side= LEFT)
# command button
But3 = Button(text= "Replace Audio",command=replace_audio)
But3.pack(side= BOTTOM)

root.mainloop()