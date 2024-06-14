from tkinter import *
import tkinter as tk
from tkinter import messagebox
def calculate():
    val1=float(firstentry.get())
    val2=float(secentry.get())
    oper=operator.get()
    if oper=="+":
        ans=val1+val2
    elif oper=="-":
        ans=val1-val2
    elif oper=="*":
        ans=val1*val2
    elif oper=="/":
        try:
            ans=val1//val2
        except ZeroDivisionError as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    elif oper=="%":
        ans=val1%val2
    elif oper=="**":
        ans=val1**val2
    answer.insert(0,str(ans))
def clear():
    firstentry.delete(0,tk.END)
    secentry.delete(0,tk.END)
    operator.delete(0,tk.END)
    answer.delete(0,tk.END)
window=Tk()
window.geometry("500x500")
window.title("calculator")
label=Label(window,text="enter the first value")
label.pack()
firstentry=Entry(window)
firstentry.pack()
sec_label=Label(window,text="enter second value")
sec_label.pack()
secentry=Entry(window)
secentry.pack()
label=Label(window,text="enter operator(+,-,*,/,%,**)").pack()
operator=Entry(window)
operator.pack()
Button(window,text="submit",command=calculate).pack()
Label(window,text="reuslt is").pack()
answer = Entry(window)
answer.pack()
Button(window,text="clear",command=clear).pack()
window.mainloop()
