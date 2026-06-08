"""
Version 1:
Basic Miles ↔ Kilometers converter.
Procedural approach.
"""

from tkinter import *

window = Tk()
window.geometry("500x500")
window.resizable(False, False)
window.title("Mile to Km Convertor")
window.config(padx= 50, pady = 100)

font = ("Arial", 20, "bold")

def calculate():
    measurement = from_unit_label.cget("text")
    if measurement == "Miles":
        try:
            mile = float(entry.get())
            km = mile * 1.60934
            result_label.config(text = str(round(km,3)))
        except ValueError:
            result_label.config(text="Error")
       
    else:
        try:
            km = float(entry.get())
            mile = km * 0.621371
            result_label.config(text = str(round(mile,3)))
        except ValueError:
            result_label.config(text="Error")
        

def switch():
    measurement = from_unit_label.cget("text")
    if measurement == "Miles":
        from_unit_label.config(text = "Km")
        to_unit_label.config(text  = "Miles")
    else:
        from_unit_label.config(text = "Miles")
        to_unit_label.config(text = "Km")
    
entry = Entry(width= 10, font = font)
entry.insert(END, string="0")
entry.grid(row = 0, column = 1)

from_unit_label = Label(text = "Miles", font = font)
from_unit_label.grid(row = 0, column = 2, padx = 10)

equal_label = Label(text = "is equal to", font = font)
equal_label.grid(row = 1, column = 0)

result_label = Label(text = "0", font = font)
result_label.grid(row = 1, column= 1)

to_unit_label = Label(text = "Km", font = font)
to_unit_label.grid(row = 1, column = 2)

button = Button(text = "Calculate", font = font, command = calculate)
button.grid(row = 2, column = 1)

switch_button = Button(text = "Switch", font = font, command = switch)
switch_button.grid(row = 2, column = 2)

window.mainloop()