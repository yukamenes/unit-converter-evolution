"""
Version 2:
Multi-converter with operation history and real-time updates.
"""

from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("600x400")
window.resizable(False, False)
window.title("Unit Converter")
window.configure(padx=80, pady=80)

font = ("Arial", 13, "bold")
operations = []

def convert(from_unit_text, to_unit_text, formula):
    from_unit_label.config(text=from_unit_text)
    to_unit_label.config(text=to_unit_text)

    result = round(formula, 3)
    result_label.config(text=str(result))

    try:
        input_value = float(entry_var.get())
    except ValueError:
        return

    operation = f"{input_value} {from_unit_text} → {result} {to_unit_text}"

    operations.append(operation)
    listbox.insert(0, operation)

    if len(operations) > 10:
        operations.pop()
        listbox.delete(10)


def calculate(*args):
    selection = combobox.get()

    try:
        entry_get = float(entry_var.get())
    except ValueError:
        result_label.config(text="Error")
        return

    if selection == "Miles to Km":
        convert("Miles", "Km", entry_get * 1.60934)

    elif selection == "Km to Miles":
        convert("Km", "Miles", entry_get * 0.621371)

    elif selection == "Celsius to Fahrenheit":
        convert("Celsius", "Fahrenheit", (entry_get * 9/5) + 32)

    elif selection == "Fahrenheit to Celsius":
        convert("Fahrenheit", "Celsius", (entry_get - 32) / 1.8)

    elif selection == "Kilograms to Pounds":
        convert("Kg", "Pounds", entry_get * 2.20462)

    elif selection == "Pounds to Kilograms":
        convert("Pounds", "Kg", entry_get * 0.453592)

    elif selection == "Meters to Feet":
        convert("Meters", "Feet", entry_get * 3.28084)

    elif selection == "Feet to Meters":
        convert("Feet", "Meters", entry_get * 0.3048)


title = Label(text="Choose a conversion type", font=font)
title.grid(row=0, column=0)

options = [
    "Miles to Km",
    "Km to Miles",
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius",
    "Kilograms to Pounds",
    "Pounds to Kilograms",
    "Meters to Feet",
    "Feet to Meters"
]

combobox = ttk.Combobox(values=options, state="readonly", font=font)
combobox.grid(row=0, column=1, padx=20, columnspan=4)
combobox.bind("<<ComboboxSelected>>", calculate)

entry_var = StringVar()
entry_var.set("0")
entry_var.trace_add("write", lambda *args: calculate())

entry = Entry(width=20, font=font, textvariable=entry_var)
entry.grid(row=1, column=0, columnspan=2)

from_unit_label = Label(text="From Unit", font=font)
from_unit_label.grid(row=1, column=1)

equal_label = Label(text="is equal to", font=font)
equal_label.grid(row=1, column=2)

result_label = Label(text="0", font=font)
result_label.grid(row=1, column=3)

to_unit_label = Label(text="To Unit", font=font)
to_unit_label.grid(row=1, column=4)

history_label = Label(text="History of operations", font=font)
history_label.grid(row=2, column=0, columnspan=5, pady=10)

listbox = Listbox(height=6, width=40, font = font)
listbox.grid(row=3, column=0, columnspan=5)

window.mainloop()