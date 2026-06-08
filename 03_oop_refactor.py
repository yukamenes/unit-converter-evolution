"""
Version 3:
First object-oriented refactoring.
"""

from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("600x400")
window.resizable(False, False)
window.title("Unit Converter")
window.configure(padx=80, pady=80)

font = ("Arial", 13, "bold")

class UnitConverterApp:

    CONVERSIONS = {
        "Miles to Km": ("Miles", "Km", lambda x: x * 1.60934),
        "Km to Miles": ("Km", "Miles", lambda x: x * 0.621371),
        "Celsius to Fahrenheit": ("Celsius", "Fahrenheit", lambda x: (x * 9/5) + 32),
        "Fahrenheit to Celsius": ("Fahrenheit", "Celsius", lambda x: (x - 32) / 1.8),
        "Kilograms to Pounds": ("Kilograms", "Pounds", lambda x: x * 2.20462),
        "Pounds to Kilograms": ("Pounds", "Kilograms", lambda x: x * 0.453592),
        "Meters to Feet": ("Meters", "Feet", lambda x: x * 3.28084),
        "Feet to Meters": ("Feet", "Meters", lambda x: x * 0.3048)
    }

    def __init__(self):
        self.operations = []


    def convert(self, *args):

        selection = combobox.get()

        try:
            entry_get = float(entry_var.get())
        except ValueError:
            result_label.config(text="Error")
            return
        
        from_u, to_u, func = self.CONVERSIONS[selection]

        result = func(entry_get)
        
        from_unit_label.config(text=from_u)
        to_unit_label.config(text=to_u)

        result_label.config(text=str(result))

        operation = f"{entry_get} {from_u} → {result} {to_u}"

        self.operations.append(operation)
        listbox.insert(0, operation)

        if len(self.operations) > 10:
            self.operations.pop()
            listbox.delete(10)


converterApp= UnitConverterApp()

title = Label(text="Choose a conversion type", font=font)
title.grid(row=0, column=0)

options = list(converterApp.CONVERSIONS.keys())

combobox = ttk.Combobox(values=options, state="readonly", font=font)
combobox.grid(row=0, column=1, padx=20, columnspan=4)
combobox.bind("<<ComboboxSelected>>", converterApp.convert)

entry_var = StringVar()
entry_var.set("0")
entry_var.trace_add("write", lambda *args: converterApp.convert())

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