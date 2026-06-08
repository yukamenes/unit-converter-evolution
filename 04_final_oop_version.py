"""
Version 4:
Final OOP implementation using Tk inheritance.
"""

from tkinter import *
from tkinter import ttk


class UnitConverterApp(Tk):

    """
    A Tkinter-based unit converter application.

    Supports multiple unit conversions with real-time updates
    and stores the last 10 conversion operations in history.
    """

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

    FONT = ("Arial", 13, "bold")

    def __init__(self):
        """
        Initialize the application window, widgets,
        and event bindings.
        """
        super().__init__()
        self.geometry("600x400")
        self.resizable(False, False)
        self.title("Unit Converter")
        self.configure(padx=80, pady=80)

        self.operations = []


        self.title_label = Label(text="Choose a conversion type", font=self.FONT)
        self.title_label.grid(row=0, column=0)

        self.options = list(self.CONVERSIONS.keys())

        self.combobox = ttk.Combobox(values=self.options, state="readonly", font=self.FONT)
        self.combobox.grid(row=0, column=1, padx=20, columnspan=4)
        self.combobox.bind("<<ComboboxSelected>>", self.convert)

        self.entry_var = StringVar()
        self.entry_var.set("0")
        self.entry_var.trace_add("write", lambda *args: self.convert())

        self.entry = Entry(width=20, font=self.FONT, textvariable=self.entry_var)
        self.entry.grid(row=1, column=0, columnspan=2)

        self.from_unit_label = Label(text="From Unit", font=self.FONT)
        self.from_unit_label.grid(row=1, column=1)

        self.equal_label = Label(text="is equal to", font=self.FONT)
        self.equal_label.grid(row=1, column=2)

        self.result_label = Label(text="0", font=self.FONT)
        self.result_label.grid(row=1, column=3)

        self.to_unit_label = Label(text="To Unit", font=self.FONT)
        self.to_unit_label.grid(row=1, column=4)

        self.history_label = Label(text="History of operations", font=self.FONT)
        self.history_label.grid(row=2, column=0, columnspan=5, pady=10)

        self.listbox = Listbox(height=6, width=40, font = self.FONT)
        self.listbox.grid(row=3, column=0, columnspan=5)

    def convert(self, *args):

        """
        Convert the entered value using the selected conversion type.

        Updates:
        - conversion result
        - displayed units
        - operation history
        """

        selection = self.combobox.get()

        try:
            entry_get = float(self.entry_var.get())
        except ValueError:
            self.result_label.config(text="Error")
            return
        
        from_u, to_u, func = self.CONVERSIONS[selection]

        result = func(entry_get)
        
        self.from_unit_label.config(text=from_u)
        self.to_unit_label.config(text=to_u)

        self.result_label.config(text=str(round(result, 2)))     

        operation = f"{entry_get} {from_u} → {round(result, 2)} {to_u}"


        self.operations.append(operation)
        self.listbox.insert(0, operation)

        if len(self.operations) > 10:
            self.operations.pop()
            self.listbox.delete(10)


converterApp= UnitConverterApp()
converterApp.mainloop()