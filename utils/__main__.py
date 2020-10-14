import sys
import tkinter as tk
from utils.convert import CoordConvert

def main():
    def convert(coord_type, mgrs_data, dd_lat_data, dd_lon_data, lat, lon):
        coord_type = coord_type.get()
        if coord_type == 'mgrs':
            input_data = mgrs_data.get()
        if coord_type == 'dd':
            input_data = '({}, {})'.format(dd_lat_data.get(), dd_lon_data.get())
        if coord_type == 'dms':
            input_data = '[({},{},{}),({},{},{})]'.format(lat['d'].get(), lat['m'].get(), lat['s'].get(), lon['d'].get(), lon['m'].get(), lon['s'].get())
        coords = CoordConvert(coord_type, input_data)
        text.delete(1.0, tk.END)
        for key in coords.conversion:
            ctype = key.upper()
            cval  = coords.conversion[key]
            text.insert(tk.INSERT, '{}\n  {}\n\n'.format(ctype,cval))

    def showWidget(selected):
        if selected == 'mgrs':
            mgrs_entry.grid(column=2, row=2)
            latLabel.grid_forget()
            lonLabel.grid_forget()
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
            latLabel.grid(column=3, row=1, sticky="w")
            dd_entry_lon.grid(column=2, row=2)
            lonLabel.grid(column=3, row=2, sticky="w")
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
            latLabel.grid(column=4, row=1, sticky="w")
            dms_lon_d.grid(column=1, row=2)
            dms_lon_m.grid(column=2, row=2)
            dms_lon_s.grid(column=3, row=2)
            lonLabel.grid(column=4, row=2, sticky="w")
            mgrs_entry.grid_forget()
            dd_entry_lat.grid_forget()
            dd_entry_lon.grid_forget()

    # Window Setup
    window = tk.Tk() 
    window.title("DCS Coordinate Conversion")
    window.geometry("500x400")

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
   
    # MGRS Input
    inputFrame = tk.Frame(topFrame)
    inputFrame.pack(side="right")
    mgrs_data  = tk.StringVar()
    mgrs_entry  = tk.Entry(inputFrame, textvariable=mgrs_data, width=20)
    mgrs_entry.grid(column=2, row=2)
    
    # DD Inputs
    latLabel = tk.Label(inputFrame, text='Latitude')
    lonLabel = tk.Label(inputFrame, text='Longitude')
    dd_lat_data = tk.StringVar()
    dd_lon_data = tk.StringVar()
    dd_entry_lat = tk.Entry(inputFrame, textvariable=dd_lat_data, width=10) 
    dd_entry_lon = tk.Entry(inputFrame, textvariable=dd_lon_data, width=10)
    
    # DMS Inputs
    lat, lon = {}, {}
    lat['d'],lat['m'],lat['s'] = tk.StringVar(),tk.StringVar(),tk.StringVar()
    lon['d'],lon['m'],lon['s'] = tk.StringVar(),tk.StringVar(),tk.StringVar()
    dms_lat_d = tk.Entry(inputFrame, textvariable=lat['d'], width=4)
    dms_lat_m = tk.Entry(inputFrame, textvariable=lat['m'], width=4)
    dms_lat_s = tk.Entry(inputFrame, textvariable=lat['s'], width=8)
    dms_lon_d = tk.Entry(inputFrame, textvariable=lon['d'], width=4)
    dms_lon_m = tk.Entry(inputFrame, textvariable=lon['m'], width=4)
    dms_lon_s = tk.Entry(inputFrame, textvariable=lon['s'], width=8)

    # Conversion Button
    convertFrame = tk.Frame(midFrame)
    convertFrame.pack(side="top")
    convertButton = tk.Button(convertFrame, text='CONVERT', command=lambda: convert(coord_type, mgrs_data, dd_lat_data, dd_lon_data, lat, lon), width=40)
    convertButton.pack(side="right")

    # Output Conversion
    outputFrame = tk.Frame(bottomFrame)
    outputFrame.pack(side="right")
    output_label = tk.Label(outputFrame, text='Conversion:')
    output_label.pack()
    text = tk.Text(outputFrame, height=10, width=40)
    text.pack(side="right")

    window.mainloop()