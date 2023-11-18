# Simple Password generator
import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    try:
        length = int(length_var.get())
        if length < 8:
            raise ValueError("Password length must be at least 8 character.")
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError as e:
        messagebox.showwarning("Error", str(e))

def copy_to_clipboard():
    generated_password = password_entry.get()
    if generated_password:
        root.clipboard_clear()
        root.clipboard_append(generated_password)
        root.update()
        messagebox.showinfo("Password copied to clipboard!")

def reset_fields():
    length_var.set(8)
    password_entry.delete(0, tk.END)

root = tk.Tk()
root.geometry("421x460")  #Size
root.resizable(0,0) #preventing from resizing
root.title("Password Generator Rathish")

frame = tk.Frame(root, bg="grey", padx=20, pady=20)
frame.pack(expand=True, fill=tk.BOTH)

password_label = tk.Label(frame, text="Password:")
password_label.grid(row=0, column=0, sticky="W")

password_entry = tk.Entry(frame, width=40)
password_entry.grid(row=0, column=1)

length_label = tk.Label(frame, text="Password Length:")
length_label.grid(row=1, column=0, sticky="W")

length_var = tk.StringVar()
length_var.set(8)  # Default length
length_entry = tk.Entry(frame, textvariable=length_var)
length_entry.grid(row=1, column=1)

generate_button = tk.Button(frame, text="Generate",fg="red",bg="yellow", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=3, pady=10)

copy_button = tk.Button(frame, text="Copy",fg="black",bg="yellow", command=copy_to_clipboard)
copy_button.grid(row=3, column=0, columnspan=3, pady=5)

reset_button = tk.Button(frame, text="Reset",fg="green",bg="yellow", command=reset_fields)
reset_button.grid(row=4, column=0, columnspan=3, pady=5)

root.mainloop()