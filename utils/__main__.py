import sys
import tkinter as tk
from utils.convert import CoordConvert

def main():
    def convert(coord_type, input_data):
        coord_type = coord_type.get()
        input_data = input_data.get()
        coords = CoordConvert(coord_type, input_data)
        text.delete(1.0, tk.END)
        for key in coords.conversion:
            ctype = key.upper()
            cval  = coords.conversion[key]
            text.insert(tk.INSERT, '{}\n  {}\n\n'.format(ctype,cval))

    # Window Setup
    window = tk.Tk() 
    window.title("DCS Coordinate Conversion")
    window.geometry("500x300")

    # Primary Frames setup
    topFrame = tk.Frame(window)
    topFrame.pack(side="top")
    bottomFrame = tk.Frame(window)
    bottomFrame.pack(side="bottom")

    # Toolbar menus
    menu = tk.Menu(window)
    window.config(menu=menu)
    subMenu_exit = tk.Menu(menu)
    menu.add_cascade(label="File", menu=subMenu_exit)
    subMenu_exit.add_command(label="Exit", command=window.quit)

    # Coordinate type select
    selectFrame = tk.Frame(topFrame)
    selectFrame.pack(side="left")
    type_label = tk.Label(selectFrame, text='Input Type:')
    type_label.pack()
    radios = ['MGRS', 'DD', 'DMS']
    coord_type = tk.StringVar()
    for text in radios:
        b = tk.Radiobutton(selectFrame, text=text, variable=coord_type, value=text.lower())
        b.pack(anchor="w")
        b.deselect()

    # Input Coordinates
    inputFrame  = tk.Frame(topFrame)
    inputFrame.pack(side="right")
    input_label = tk.Label(inputFrame, text='Coordinates:', width=20)
    input_label.pack(side="left")
    input_data  = tk.StringVar()
    input_entry = tk.Entry(inputFrame, textvariable=input_data, width=40)
    input_entry.pack(side="right")

    # Conversion Button
    convertFrame = tk.Frame(bottomFrame)
    convertFrame.pack(side="top")
    convertButton = tk.Button(convertFrame, text='CONVERT', command=lambda: convert(coord_type,input_data), width=40)
    convertButton.pack(side="right")

    # Output Conversion
    outputFrame = tk.Frame(bottomFrame)
    outputFrame.pack(side="right")
    output_label = tk.Label(outputFrame, text='Conversion:')
    output_label.pack(side="left")
    text = tk.Text(outputFrame, height=6, width=40)
    text.pack(side="right")

    window.mainloop()