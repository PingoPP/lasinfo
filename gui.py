print("GUI imported")

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
from helper import (
    file_information, crs_button, spatial_extent, point_density, intensity_button,
    scan_angle, gps, edge_of_line, scan_direction, number_of_returns, classification,
    rgb, nir
)
#For making the GUI. I used the tkinter libary. 
#First step is to created the main window.
#Second step is to created the two tabs - Intro and Info.
#Third step is to created buttons for more functionality
#Fourth step is created text widget for showing all information from analysis.py.

#TKINTER
def create_gui():
    app = tk.Tk()
    app.title(".LAS")
    app.configure(bg="black")

    photo = ImageTk.PhotoImage(Image.open(r"C:\Users\jakad\OneDrive\Desktop\lasinfo\lasfortab.png"), master=app)
    app.wm_iconphoto(True, photo)
    app.geometry("900x700")

    style = ttk.Style()
    style.theme_use("default")
    style.configure("TNotebook", background="black", borderwidth=0)
    style.configure("TNotebook.Tab", background="black", foreground="white")

    notebook = ttk.Notebook(app)
    notebook.pack(fill="both", expand=True)

    intro_tab = tk.Frame(notebook, bg="black")
    notebook.add(intro_tab, text="Intro")

    button_frame = tk.Frame(app, bg="black")
    button_frame.pack(padx=10)

    title = tk.Label(
        intro_tab,
        text="LAS.INFO",
        font=("Roboto", 50),
        fg="red",
        bg="black"
    )
    title.pack()

    #INTRO
    intro = tk.Label(
        intro_tab,
        text="Welcome! This application was created by Jaka Dacar aka Dacke. "
             "It provides information about LAS and LAZ files to help you better understand their contents. "
             "I hope you find it helpful! \n\n"
             "*On left side you have two windows - Intro and Info. For more information click on Info*",
        font=("Roboto", 15),
        fg="white",
        bg="black",
        wraplength=800,
        justify="left"
    )
    intro.pack()

    def open_img():
        image_path = r"C:\Users\jakad\OneDrive\Desktop\info\pixil-frame-0 (3).png"
        try:
            img = Image.open(image_path)
        except FileNotFoundError:
            print("My bad")
            return None
#IT'S NOT WORKING
        img = img.resize((300, 300))
        photo = ImageTk.PhotoImage(img, master=app)
        button = tk.Button(intro_tab, image=photo)
        button.image = photo
        button.pack()

        return button

    open_img()

    powered = tk.Label(
        intro_tab,
        text="Powered by: Laspy, Numpy, Tkinter, Sys, PIL \n\n "
            "                           version: 1.1",
        font=("Roboto", 10),
        fg="white",
        bg="black",
        wraplength=800,
        justify="left"
    )
    powered.pack()

    #INFO
    stats_tab = tk.Frame(notebook, bg="black")
    notebook.add(stats_tab, text="Info")
    #ANALYZE THE LAS FILE 
    def select_and_analyze_app():

        filename = filedialog.askopenfilename(
            title = "Select a .LAS / .LAZ file",
            filetypes=[("LAS files", "*.las *.laz")]
                )
        if filename:
            try:
                from analysis import analyze_las
                new_stats = analyze_las(filename)
                for widget in stats_tab.winfo_children():
                    widget.destroy()
                show_stats(stats_tab, new_stats)
            except Exception as e:
                messagebox.showwarning("Error", f"Error:\n{e}")
                return
    #BUTTON FOR SELECTING THE .LAS FILE 
    button_laz = tk.Button(
        button_frame,
        text="Select .LAS file",
        command=select_and_analyze_app
    )
    button_laz.pack()

    def close_app():
        app.destroy()
    #BUTTON FOR EXITING THE APP
    button_exit = tk.Button(
        button_frame,
        text="Exit",
        command=close_app
    )
    button_exit.pack()
    app.mainloop()

#MAKING A BUTTON "?"
def add_line(widget, text, help_func=None):
    """?"""
    widget.insert(tk.END, text)
    if help_func:
        widget.insert(tk.END, "  ")
        btn = tk.Button(
            widget, text="?", width=1, height=1,
            bg="gray20", fg="white", relief="flat",
            command=help_func
        )
        widget.window_create(tk.END, window=btn)
    widget.insert(tk.END, "\n")

#SHWOING ALL INFORMATION FROM ANALYSIS.PY IN GUI.PY
def show_stats(parent, stats):
    text_widget = tk.Text(parent, wrap="word", bg="black", fg="white", font=("Roboto", 12))
    text_widget.pack(padx=10, pady=10, fill="both", expand=True, anchor="center")

    add_line(text_widget, "-----FILE INFORMATION-----", file_information)
    fi = stats.get('file_information')
    #I MADE IN THAT LOGIC; add_line(text_widget, f"x:{xx['xxxx']}" if xx else "x: N/A"), xxxx_button (if is in helper.py written the function for XXXX topic)
    add_line(text_widget, f"File: {fi['file']}" if fi else "File: N/A")
    add_line(text_widget, f"File Size: {fi['file_size']} MB" if fi else "File Size: N/A")
    add_line(text_widget, f"Point Format: {fi['point_format']}" if fi else "Point Format: N/A")
    add_line(text_widget, f"LAS Version: {fi['las_version']}" if fi else "LAS Version: N/A")
    add_line(text_widget, f"Total points: {fi['total_points']}" if fi else "Total points: N/A")
    add_line(text_widget, "\n")

    add_line(text_widget, "-----COORDINATE SYSTEM-----", crs_button)
    cs = stats.get('coordinate_system')
    add_line(text_widget, f"CRS: {cs['crs']}" if cs else "CRS: N/A")
    add_line(text_widget, "\n")

    add_line(text_widget, "-----SPATIAL EXTENT-----", spatial_extent)
    se = stats.get('spatial_extent')
    add_line(text_widget, f"X: {se['x_min']} - {se['x_max']}" if se else "X: N/A")
    add_line(text_widget, f"Y: {se['y_min']} - {se['y_max']}" if se else "Y: N/A")
    add_line(text_widget, f"Z: {se['z_min']} - {se['z_max']}" if se else "Z: N/A")
    add_line(text_widget, "\n")

    add_line(text_widget, "-----POINT STATISTICS-----\n")
    ps = stats.get('point_statistics')
    add_line(text_widget, f"Point Density: {ps['point_density']} pts/m\u00b2" if ps else "Point Density: N/A", point_density)
    add_line(text_widget, f"Edge of Flight Line: {ps['edge_of_flight_line_min']} - {ps['edge_of_flight_line_max']}" if ps else "Edge of Flight Line: N/A", edge_of_line)
    add_line(text_widget, f"Intensity: {ps['intensity_min']} - {ps['intensity_max']}" if ps else "Intensity: N/A", intensity_button)
    add_line(text_widget, f"Scan Angle: {ps['scan_angle_min']} - {ps['scan_angle_max']}" if ps else "Scan Angle: N/A", scan_angle)
    add_line(text_widget, f"GPS Time: {ps['gps_min']} - {ps['gps_max']}" if ps else "GPS Time: N/A", gps)
    add_line(text_widget, "\n")

    add_line(text_widget, "-----RETURN NUMBER-----", number_of_returns)
    ri = stats.get('return_information')
    add_line(text_widget, f"Return Number Min: {ri['return_number_min']}" if ri else "Return Number Min: N/A")
    add_line(text_widget, f"Return Number Max: {ri['return_number_max']}" if ri else "Return Number Max: N/A")
    add_line(text_widget, f"First Return: {ri['first_return']}" if ri else "First Return: N/A")
    add_line(text_widget, f"Last Return: {ri['last_return']}" if ri else "Last Return: N/A")
    add_line(text_widget, f"Intermediate Return: {ri['intermediate_returns']}" if ri else "Intermediate Return: N/A")
    add_line(text_widget, "\n")

    add_line(text_widget, "-----CLASSIFICATION-----", classification)
    cl = stats.get('classification')
    for label, key in [
        ("Never Classified", "never_classified"), ("Unassigned", "unassigned"),
        ("Ground", "ground"), ("Low Vegetation", "low_vegetation"),
        ("Medium Vegetation", "medium_vegetation"), ("High Vegetation", "high_vegetation"),
        ("Building", "building"), ("Low Point", "low_point"),
        ("Water", "water"), ("High Noise", "high_noise"),
    ]:
        add_line(text_widget, f"{label}: {cl[key]}" if cl else f"{label}: N/A")
    add_line(text_widget, "\n")

    add_line(text_widget, "-----RGB-----", rgb)
    rgbv = stats.get('rgb')
    add_line(text_widget, f"Red: {rgbv['red_min']} - {rgbv['red_max']}" if rgbv else "Red: N/A")
    add_line(text_widget, f"Green: {rgbv['green_min']} - {rgbv['green_max']}" if rgbv else "Green: N/A")
    add_line(text_widget, f"Blue: {rgbv['blue_min']} - {rgbv['blue_max']}" if rgbv else "Blue: N/A")
    add_line(text_widget, "\n")

    add_line(text_widget, "-----NIR-----", nir)
    nirv = stats.get('nir')
    add_line(text_widget, f"NIR: {nirv['nir_min']} - {nirv['nir_max']}" if nirv else "NIR: N/A")

    text_widget.config(state="disabled")

    #COPY ALL TEXT IN TEXT WIDGET + BUTTON
    def copy_all(event=None):
        text_widget.clipboard_clear()
        text_widget.clipboard_append(text_widget.get("1.0", tk.END))

    copy_button = tk.Button(
        parent,
        text="Copy",
        command=copy_all
    )
    copy_button.pack(pady=5)

    return text_widget

