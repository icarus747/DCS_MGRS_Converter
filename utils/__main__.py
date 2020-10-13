import sys
import tkinter as tk
from utils.convert import CoordConvert

def main():
    # Window Setup
    window = tk.Tk() 
    window.title("DCS Coordinate Conversion")
    topFrame = tk.Frame(window)
    topFrame.pack()

    bottomFrame = tk.Frame(window)
    bottomFrame.pack(side=tk.BOTTOM)

    # Toolbar menus
    menu = tk.Menu(window)
    window.config(menu=menu)
    subMenu_exit = tk.Menu(menu)
    menu.add_cascade(label="File", menu=subMenu_exit)
    subMenu_exit.add_command(label="Exit", command=window.quit)

    # Coordinate type select
    selectFrame = tk.Frame(topFrame)
    selectFrame.pack(side=tk.LEFT)
    type_label = tk.Label(selectFrame, text='Input Type:')
    type_label.pack()
    listbox = tk.Listbox(selectFrame, height=3)
    listbox.insert(1, "MGRS")
    listbox.insert(2, "DD")
    listbox.insert(3, "DMS")
    listbox.pack(side=tk.LEFT)

    # Input Coordinates
    inputFrame = tk.Frame(topFrame)
    inputFrame.pack(side=tk.RIGHT)
    input_label = tk.Label(inputFrame, text='Coordinates:', width=20)
    input_label.pack(side=tk.LEFT)
    input_data = tk.Entry(inputFrame)
    input_data.pack(side=tk.RIGHT)

    # Output Conversion
    outputFrame = tk.Frame(bottomFrame)
    outputFrame.pack(side=tk.RIGHT)
    output_label = tk.Label(outputFrame, text='Conversion:')
    output_label.pack(side=tk.LEFT)
    text = tk.Text(outputFrame, width=20, height=3)
    text.insert(tk.INSERT, '\n'.join([ str(i) for i in range(3) ]))
    text.pack(side=tk.RIGHT)

    window.mainloop()