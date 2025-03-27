from tkinter import *
from tkinter import messagebox
root =Tk()
 
def popup():
    messagebox.showinfo(title="MessageBox", message="This is my info")

Button(root, text="Popup", command=popup).pack()

root.mainloop()