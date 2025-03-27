import tkinter as tk

window = tk.Tk()
window.title("My First Tkinter Window")
window.geometry("300x150")

label = tk.Label(window, text="Hello, Kristina!", font=("Arial", 14))
label.pack(pady=20)

window.mainloop()
