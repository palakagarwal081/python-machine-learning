import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as ttk

from tkinter import *
from PIL import Image,ImageTk

# Create an instances of tkinter frame 
win = Tk()

# Set the geometry of tkinter frame
win.geometry("750x270")

# Create a canvas
canvas = Canvas(win, width = 600,height = 400) 
canvas.pack()

# Load an image in the script
img = ImageTk.PhotoImage(Image.open("ml.png"))

# Add image to the Canvas items
canvas.create_image(10,10, anchor  = NW , image = img)

win.mainloop()
