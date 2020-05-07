import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msg


class DateOfBirth:
    def __init__(self):
        self.window = tk.Tk()
        self.day = tk.IntVar()
        self.month = tk.StringVar()
        self.year = tk.IntVar()
        self.label = tk.Label(self.window, text='Select your date of birth: ')
        self.label.pack(side=tk.TOP)

        self.combobox_day = ttk.Combobox(self.window, textvariable=self.day)
        list_day = [x for x in range(1, 32)]
        self.combobox_day['values'] = list_day
        self.combobox_day.current(0)
        self.combobox_day.pack()

        self.combobox_month = ttk.Combobox(self.window, textvariable=self.month)
        list_month = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December']
        self.combobox_month['values'] = list_month
        self.combobox_month.current(0)
        self.combobox_month.pack()

        self.combobox_year = ttk.Combobox(self.window, textvariable=self.year)
        list_years = [x for x in range(1950, 2021)]
        self.combobox_year['values'] = list_years
        self.combobox_year.current(0)
        self.combobox_year.pack()

        button = tk.Button(self.window, text='Show', height=2, width=15, command=self.show_info)
        button.pack(side=tk.BOTTOM)
        self.window.mainloop()

    def show_info(self):
        msg.showinfo("Your Birth Date: ",
                     f"{self.combobox_day.get()} {self.combobox_month.get()} {self.combobox_year.get()}")


if __name__ == '__main__':
    yourdate = DateOfBirth()
