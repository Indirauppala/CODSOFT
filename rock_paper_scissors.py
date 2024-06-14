from tkinter import *
import tkinter as tk
import random

def game():
    user=entry.get()
    ls=["rock","paper","scissor"]
    comp=random.choice(ls)
    comp_entry.insert(0,"computers choice is "+comp)
    if user==comp:
        output.insert(0,"it's a tie")
    elif user=="rock" and comp=="paper":
        output.insert(0,"computer wins")
    elif user=="rock" and comp=="scissor":
        output.insert(0,"you won")
    elif user=="paper" and comp=="rock":
        output.insert(0,"user wins")
    elif user=="paper" and comp=="scissor":
        output.insert(0,"computer wins")
    elif user=="scissor" and comp=="rock":
        output.insert(0,"computer wins")
    elif user=="scissor" and comp=="paper":
        output.insert(0,"you won")

def play_again():
    entry.delete(0,tk.END)
    output.delete(0,tk.END)
    comp_entry.delete(0,tk.END)
    
window=Tk()
window.geometry("500x500")
window.title("rock paper scissors")
window.configure(bg="#ffe1bd")

empty_label = tk.Label(window, height=5,bg="#ffe1bd")
empty_label.pack()

label=Label(window,text="enter your choice")
label.pack(pady=5)

entry=Entry(window)
entry.pack(pady=5)

button=Button(window,text="submit",command=game)
button.pack(pady=10)

comp_entry=Entry(window,width=30)
comp_entry.pack(pady=5)

output=Entry(window)
output.pack(pady=5)

play=Button(window,text="play again",command=play_again)
play.pack(pady=5)

window.mainloop()



