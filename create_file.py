import tkinter as tk
import os
import turtle
import sys

def command(x):
    os.system(x)
    
def create_file(*ignore):
    command("cd ~/Desktop; touch " + entry.get())
    sys.exit(0)


master = tk.Tk()

master.after(1, lambda: master.focus_force())

master.title("Create File")

tk.Label(master, text="File Name").grid(row=0)

entry = tk.Entry(master)
entry.grid(row=0, column=1)
entry.focus()

master.bind('<Return>', create_file)

master.eval('tk::PlaceWindow %s center' % master.winfo_pathname(master.winfo_id()))

os.system("open -a Python")

master.mainloop()
