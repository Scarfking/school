#!usr/bin/python

from PIL import Image, ImageDraw, ImageTk
import tkinter as tk

root = tk.Tk()

tp = Image.open("transparant.png")
img = ImageTk.PhotoImage(tp)
canvas = tk.Label(root, image = img)
canvas.pack()

root.mainloop()
