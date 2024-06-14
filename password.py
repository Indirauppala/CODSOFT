from tkinter import *
import string
import random
import tkinter as tk
from tkinter import messagebox

def gen_pass():
    try:
        length = int(entry.get())
        
        if length < 6:
            messagebox.showerror("Error", "Password length should be at least 6")
            entry.delete(0, tk.END)
            return
        
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        spl_symbols = string.punctuation

        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(spl_symbols)
        ]

        all_chars = lowercase + uppercase + digits + spl_symbols
        password += random.choices(all_chars, k=length - 4)

        random.shuffle(password)
        final_password = ''.join(password)
        entry_pass.delete(0, tk.END)
        entry_pass.insert(0, final_password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length")


window = Tk()
window.geometry("500x500")
window.title("Password Generator")
window.configure(bg="#FFBCCC")

empty_label = tk.Label(window, height=5,bg="#FFBCCC")
empty_label.pack()

label = Label(window, text="Enter the length of the password")
label.pack(pady=5)

entry = Entry(window)
entry.pack(pady=5)

button = Button(window, text="Generate", command=gen_pass)
button.pack(pady=10)

label_pass = Label(window, text="Generated Password")
label_pass.pack(pady=5)

entry_pass = Entry(window)
entry_pass.pack(pady=5)

window.mainloop()
