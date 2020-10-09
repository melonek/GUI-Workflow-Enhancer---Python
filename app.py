import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.geometry("600x600")
root.resizable(0, 0)
apps = []


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title="Select File", filetypes=(("Disk iMaGe", "*.dmg"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


canvas = tk.Canvas(root, height=500, width=500, bg='#263D42')
canvas.pack()

frame = tk.Frame(master=root,
                 width=300,
                 height=500,
                 bg='white')
frame.place(relwidth=0.8, relheight=0.6, relx=0.1,
            rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="darkgreen", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="darkgreen", bg="#263D42")
runApps.pack()

root.mainloop()
