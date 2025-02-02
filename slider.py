import tkinter as tk
from tkinter import messagebox
import random

# Constants
GRID_SIZE = 4
BUTTON_HEIGHT = 5
BUTTON_WIDTH = 5
BUTTON_BORDER_WIDTH = 5
WINNING_SEQUENCE = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,"

# Initialize numbers
numbers = [str(i) for i in range(1, GRID_SIZE * GRID_SIZE)] + [""]

def click_me(button):
    index = numbers.index(button.cget("text"))
    empty = numbers.index("")
    numbers[index], numbers[empty] = numbers[empty], numbers[index]

    widgets = frame.winfo_children()
    widgets[index].config(text=numbers[index])
    widgets[empty].config(text=numbers[empty])

    if ",".join(numbers) == WINNING_SEQUENCE:
        messagebox.showinfo("Hurray!", "You solved it!")

def load_board():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            button = tk.Button(frame, text=f'{numbers[GRID_SIZE * i + j]}', height=BUTTON_HEIGHT, width=BUTTON_WIDTH, relief=tk.RAISED, borderwidth=BUTTON_BORDER_WIDTH)
            button.configure(command=lambda b=button: click_me(b))
            button.grid(row=i, column=j)

def begin():
    random.shuffle(numbers)
    load_board()

root = tk.Tk()
root.title("Slider Puzzle")

frame = tk.Frame(root)
frame.pack()

begin()
root.mainloop()
