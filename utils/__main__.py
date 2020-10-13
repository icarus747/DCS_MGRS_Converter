import sys
import tkinter as tk
from utils.convert import CoordConvert

def main():
    def convert(coord_type, input_data):
        coord_type = coord_type.get()
        input_data = input_data.get()
        coords = CoordConvert(coord_type, input_data)
        for k, v in coords.conversion:
            text.insert(tk.INSERT, '{} :: {}'.format(k,v))
            print('{} :: {}'.format(k,v))

    # Window Setup
    window = tk.Tk() 
    window.title("DCS Coordinate Conversion")

    # Primary Frames setup
    topFrame = tk.Frame(window).pack(side=tk.TOP)
    bottomFrame = tk.Frame(window).pack(side=tk.BOTTOM)

    # Toolbar menus
    menu = tk.Menu(window)
    window.config(menu=menu)
    subMenu_exit = tk.Menu(menu)
    menu.add_cascade(label="File", menu=subMenu_exit)
    subMenu_exit.add_command(label="Exit", command=window.quit)

    # Coordinate type select
    selectFrame = tk.Frame(topFrame).pack(side=tk.LEFT)
    type_label = tk.Label(selectFrame, text='Input Type:').pack()
    radios = ['MGRS', 'DD', 'DMS']
    coord_type = tk.StringVar()
    for text in radios:
        b = tk.Radiobutton(selectFrame, text=text, textvariable=coord_type, value=text, width=20).pack()

    # Input Coordinates
    inputFrame  = tk.Frame(topFrame).pack(side=tk.RIGHT)
    input_label = tk.Label(inputFrame, text='Coordinates:', width=20).pack(side=tk.LEFT)
    input_data  = tk.StringVar()
    input_entry = tk.Entry(inputFrame, textvariable=input_data).pack(side=tk.RIGHT)

    # Conversion Button
    convertFrame = tk.Frame(topFrame).pack(side=tk.BOTTOM)
    convertButton = tk.Button(convertFrame, text='CONVERT', command=convert(coord_type,input_data), width=40).pack()

    # Output Conversion
    outputFrame = tk.Frame(bottomFrame)
    outputFrame.pack(side=tk.RIGHT)
    output_label = tk.Label(outputFrame, text='Conversion:')
    output_label.pack(side=tk.LEFT)
    text = tk.Text(outputFrame, height=4)
    # text.insert(tk.INSERT, 'hey\nthis\nis\nfun')
    text.pack(side=tk.RIGHT)

    window.mainloop()