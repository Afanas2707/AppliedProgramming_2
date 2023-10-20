import tkinter as tk
from time import strftime


def time():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000, time)


def date():
    date_string = strftime('%A, %B %d, %Y')
    date_label.config(text=date_string)


root = tk.Tk()
root.title('Электронные часы')

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
date_label = tk.Label(root, font=('calibri', 20, 'bold'), background='black', foreground='cyan')

label.pack(anchor='center')
date_label.pack(anchor='center')

time()
date()

root.geometry('400x150')
root.configure(background='black')
root.mainloop()
