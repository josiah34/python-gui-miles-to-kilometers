import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Miles to Kilometers Converter")
        self.window.geometry("300x150")

        # title
        title = ttk.Label(master=self.window, text="Miles to Kilometers Converter", font='Calibri 14 bold')
        title.pack()

        # input field
        input_frame = ttk.Frame(master=self.window)
        self.entry = ttk.Entry(master=input_frame, width=10)
        button = ttk.Button(master=input_frame, text="Convert", command=self.convert)
        self.entry.pack(side='left', padx=10)
        button.pack(side='left')
        input_frame.pack(pady=10)

        # output field
        self.output_label = ttk.Label(master=self.window, text="Kilometers: ")
        self.output_label.pack(pady=10)

    def convert(self):
        try:
            miles = float(self.entry.get())
            km = miles * 1.609344
            self.output_label.config(text=f"{km:.2f} km")  # Display up to 2 decimal places
        except ValueError:
            self.output_label.config(text="Invalid input")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
