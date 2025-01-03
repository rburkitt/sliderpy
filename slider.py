import tkinter as tk
from tkinter import Frame, messagebox
import random
import re

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", ""]

def extract_number(string):
    match = re.search(r'\d+', string)
    return int(match.group()) if match else None

def click_me(sender):
    text = sender.cget("text")
    if text == "":
        return
    
    index = numbers.index(text) #extract_number(sender.name) -1
    cell = numbers[index]
    empty = numbers.index("")
    if empty != index - 1 and empty != index + 1 and empty != index - 4 and empty != index +4:
        return
    
    numbers[index] = ""
    numbers[empty] = cell

    load_board()

    if ",".join(numbers) == "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,":
        messagebox.showinfo("Hurray!", "You solved it!")

def load_board():
    for i in range(4):
        for j in range(4):
            button = tk.Button(frame, text=f'{numbers[4*i+j]}')
            button.configure(command=lambda b=button: click_me(b))
            button.grid(row=i, column = j)

def begin():
    random.shuffle(numbers)
    load_board()            


root = tk.Tk()

root.title("Slider Puzzle")

frame = Frame(root, bd = 1)
frame.pack(fill = 'both', expand = True,
           padx = 10, pady = 10)

begin()

root.mainloop()        