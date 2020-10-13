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

    def showWidget(selected):
        if selected == 'mgrs':
            mgrs_entry.grid(column=2, row=2)
            dd_entry_lat.grid_forget()
            dd_entry_lon.grid_forget()
            dms_lat_d.grid_forget()
            dms_lat_m.grid_forget()
            dms_lat_s.grid_forget()
            dms_lon_d.grid_forget()
            dms_lon_m.grid_forget()
            dms_lon_s.grid_forget()
        if selected == 'dd':
            dd_entry_lat.grid(column=2, row=1)
            dd_entry_lon.grid(column=2, row=2)
            mgrs_entry.grid_forget()
            dms_lat_d.grid_forget()
            dms_lat_m.grid_forget()
            dms_lat_s.grid_forget()
            dms_lon_d.grid_forget()
            dms_lon_m.grid_forget()
            dms_lon_s.grid_forget()
        if selected == 'dms':
            dms_lat_d.grid(column=1, row=1)
            dms_lat_m.grid(column=2, row=1)
            dms_lat_s.grid(column=3, row=1)
            dms_lon_d.grid(column=1, row=2)
            dms_lon_m.grid(column=2, row=2)
            dms_lon_s.grid(column=3, row=2)
            mgrs_entry.grid_forget()
            dd_entry_lat.grid_forget()
            dd_entry_lon.grid_forget()

    # Window Setup
    window = tk.Tk() 
    window.title("DCS Coordinate Conversion")
    window.geometry("600x300")

    # Primary Frames setup
    topFrame = tk.Frame(window)
    topFrame.pack(side="top")
    midFrame = tk.Frame(window)
    midFrame.pack()
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
    coord_type = tk.StringVar(value='mgrs')
    mgrs_radio = tk.Radiobutton(selectFrame, text='MGRS', variable=coord_type, value='mgrs', command=lambda: showWidget('mgrs'))
    mgrs_radio.pack(anchor="w")
    dd_radio = tk.Radiobutton(selectFrame, text='DD', variable=coord_type, value='dd', command=lambda: showWidget('dd'))
    dd_radio.pack(anchor="w")
    dms_radio = tk.Radiobutton(selectFrame, text='DMS', variable=coord_type, value='dms', command=lambda: showWidget('dms'))
    dms_radio.pack(anchor="w")

    # Input Coordinates
    labelRight  = tk.Frame(topFrame)
    labelRight.pack(side="left")
    input_label = tk.Label(labelRight, text='Coordinates:')
    input_label.pack(side="left")
   
    inputFrame = tk.Frame(topFrame)
    inputFrame.pack(side="right")
    mgrs_data  = tk.StringVar()
    mgrs_entry  = tk.Entry(inputFrame, textvariable=mgrs_data, width=10)
    mgrs_entry.grid(column=2, row=2)
    
    dd_lat = tk.StringVar()
    dd_lon = tk.StringVar()
    dd_entry_lat = tk.Entry(inputFrame, textvariable=dd_lat, width=10) 
    dd_entry_lon = tk.Entry(inputFrame, textvariable=dd_lon, width=10)
    
    lat, lon = {}, {}
    lat['d'],lat['m'],lat['s'] = tk.StringVar(),tk.StringVar(),tk.StringVar()
    lon['d'],lon['m'],lon['s'] = tk.StringVar(),tk.StringVar(),tk.StringVar()
    dms_lat_d = tk.Entry(inputFrame, textvariable=lat['d'], width=2)
    dms_lat_m = tk.Entry(inputFrame, textvariable=lat['m'], width=2)
    dms_lat_s = tk.Entry(inputFrame, textvariable=lat['s'], width=6)
    dms_lon_d = tk.Entry(inputFrame, textvariable=lon['d'], width=2)
    dms_lon_m = tk.Entry(inputFrame, textvariable=lon['m'], width=2)
    dms_lon_s = tk.Entry(inputFrame, textvariable=lon['s'], width=6)

    # Conversion Button
    convertFrame = tk.Frame(midFrame)
    convertFrame.pack(side="top")
    convertButton = tk.Button(convertFrame, text='CONVERT', command=lambda: convert(coord_type,mgrs_data), width=40)
    convertButton.pack(side="right")

    # Output Conversion
    outputFrame = tk.Frame(bottomFrame)
    outputFrame.pack(side="right")
    output_label = tk.Label(outputFrame, text='Conversion:')
    output_label.pack(side="left")
    text = tk.Text(outputFrame, height=6, width=40)
    text.pack(side="right")

    window.mainloop()