from tkinter import *

window = Tk()
import random

RANDOM_COLORS = ["red", "grey", "green", "black"]


def change_colors():
    grid_list = [r, g, f, h]
    for i in grid_list:
        random_color = RANDOM_COLORS[random.randint(0, len(RANDOM_COLORS) - 1)]
        i.config(bg=random_color)
        RANDOM_COLORS.remove(random_color)


r = Label(bg="black", width=20, height=5)
r.grid(row=0, column=0)

g = Label(bg="red", width=20, height=5)
g.grid(row=0, column=1)

f = Label(bg="red", width=20, height=5)
f.grid(row=1, column=1)

h = Label(bg="red", width=20, height=5)
h.grid(row=1, column=0)

m = Label(bg="pink", width=40, height=5)
m.config(padx=0, pady=0)
m.grid(row=2, column=0, columnspan=2)
change_colors()
window.mainloop()
