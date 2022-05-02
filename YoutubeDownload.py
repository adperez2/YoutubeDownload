
from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("500x300")
root.config(bg="purple")
root.resizable(0,0)

def xyz():
  url= YouTube(str(abc.get()))
  video=url.streams.get_highest_resolution()
  video.download()
  Label(root, text="Your video has downloaded ", bg="purple").grid(row=4, column=2)

abc =StringVar()

linkEnter=Entry(root, width=50, textvariable=abc, font='arial 15 bold', justify="center")
linkEnter.grid(row=3, column=2)

button1 =Button(root, text="Click Download", font='arial', fg='white', bg='black',command=xyz)
button1.grid(row=4, column=2)


root.mainloop()
