print("GUI imported")

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import filedialog

def create_gui():
    app = tk.Tk()
    app.title(".LAS")
    app.configure(bg="black")

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
            "                           version: 1.0",
        font=("Roboto", 10),
        fg="white",
        bg="black",
        wraplength=800,
        justify="left"
    )
    powered.pack()

    stats_tab = tk.Frame(notebook, bg="black")
    notebook.add(stats_tab, text="Info")

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

    button_laz = tk.Button(
        button_frame, 
        text="Select .LAS file",
        command=select_and_analyze_app
    )
    button_laz.pack()

    def close_app():
        app.destroy()
    
    button_exit = tk.Button(
        button_frame,
        text="Exit",
        command=close_app
    )
    button_exit.pack()
    app.mainloop()
    
def show_stats(parent, stats):
    infotext = "\n".join([
        f"-----FILE INFORMATION-----\n\n"
        f"File: {stats['file_information']['file']}" if stats['file_information'] else "File: N/A",
        f"File Size: {stats['file_information']['file_size']} MB" if stats['file_information'] else "File: N/A",
        f"Point Format: {stats['file_information']['point_format']}" if stats['file_information'] else "File: N/A",
        f"LAS Version: {stats['file_information']['las_version']}" if stats ['file_information'] else "File: N/A",
        f"Total points: {stats['file_information']['total_points']}" if stats ['file_information'] else "File: N/A \n\n",

        f"\n\n-----COORDINATE SYSTEM-----\n\n"
        f"CRS: {stats['coordinate_system']['crs']}" if stats['coordinate_system'] else "CRS: N/A \n\n",
        
        f"\n\n-----SPATIAL EXTENT-----\n\n"
        f"X: {stats['spatial_extent']['x_min']} - {stats['spatial_extent']['x_max']}" if stats['spatial_extent'] else "X: N/A",
        f"Y: {stats['spatial_extent']['y_min']} - {stats['spatial_extent']['y_max']}" if stats['spatial_extent'] else "Y: N/A",
        f"Z: {stats['spatial_extent']['z_min']} - {stats['spatial_extent']['z_max']}" if stats['spatial_extent'] else "Z: N/A \n\n",

        f"\n\n-----POINT STATISTICS-----\n\n"
        f"Point Density: {stats['point_statistics']['point_density']} pts/m²" if stats['point_statistics'] else "Point Density: N/A",
        f"Edge of Flight Line: {stats['point_statistics']['edge_of_flight_line_min']} - {stats['point_statistics']['edge_of_flight_line_max']}" if stats['point_statistics'] else "Edge of Flight Line: N/A",
        f"Intensity: {stats['point_statistics']['intensity_min']} - {stats['point_statistics']['intensity_max']}" if stats['point_statistics'] else "Intensity: N/A",
        f"Scan Angle: {stats['point_statistics']['scan_angle_min']} - {stats['point_statistics']['scan_angle_max']}" if stats['point_statistics'] else "Scan angle: N/A",
        f"GPS Time: {stats['point_statistics']['gps_min']} - {stats['point_statistics']['gps_max']}" if stats['point_statistics'] else "GPS Time: N/A \n\n",

        f"\n\n-----RETURN NUMBER-----\n\n"
#       f"Return Number: {stats['return_information']['return_number']}" if stats['return_information'] else "Return Number: N/A",
        f"Return Number Min: {stats['return_information']['return_number_min']}" if stats['return_information'] else "Return Number Min: N/A",
        f"Return Number Max: {stats['return_information']['return_number_max']}" if stats['return_information'] else "Return Number Max: N/A",
        f"First Return: {stats['return_information']['first_return']}" if stats['return_information'] else "First Returns: N/A",
        f"Last Return: {stats['return_information']['last_return']}" if stats['return_information'] else "Last Returns: N/A",
        f"Intermediate Return: {stats['return_information']['intermediate_returns']}" if stats['return_information'] else "Intermediate Returns: N/A \n\n",

        f"\n\n-----CLASSIFICATION-----\n\n"
        f"Never Classified: {stats['classification']['never_classified']}" if stats['classification'] else "Never Classified: N/A",
        f"Unassigned: {stats['classification']['unassigned']}" if stats['classification'] else "Unassigned: N/A",
        f"Ground: {stats['classification']['ground']}" if stats['classification'] else "Ground: N/A",
        f"Low Vegetation: {stats['classification']['low_vegetation']}" if stats['classification'] else "Low Vegetation: N/A",
        f"Medium Vegetation: {stats['classification']['medium_vegetation']}" if stats['classification'] else "Medium Vegetation: N/A",
        f"High Vegetation: {stats['classification']['high_vegetation']}" if stats['classification'] else "High Vegetation: N/A",
        f"Building: {stats['classification']['building']}" if stats['classification'] else "Building: N/A",
        f"Low Point: {stats['classification']['low_point']}" if stats['classification'] else "Low Point: N/A",
        f"Water: {stats['classification']['water']}" if stats['classification'] else "Water: N/A",
        f"High Noise: {stats['classification']['high_noise']}" if stats['classification'] else "High Noise: N/A \n\n",

        f"\n\n-----RGB-----\n\n"
        f"Red: {stats['rgb']['red_min']} - {stats['rgb']['red_max']}" if stats['rgb'] else "Red: N/A",
        f"Green: {stats['rgb']['green_min']} - {stats['rgb']['green_max']}" if stats['rgb'] else "Green: N/A",
        f"Blue: {stats['rgb']['blue_min']} - {stats['rgb']['blue_max']}" if stats['rgb'] else "Blue: N/A \n\n",

        f"\n\n-----NIR-----\n\n"
        f"NIR: {stats['nir']['nir_min']} - {stats['nir']['nir_max']}" if stats['nir'] else "NIR: N/A \n\n",
    ])

    text_widget = tk.Text(parent, wrap="word", bg="black", fg="white", font=("Roboto", 12))
    text_widget.insert("1.0", infotext)
    text_widget.config(state="normal")
    text_widget.pack(padx=10, pady=10, fill="both", expand=True, anchor="center")

    def copy_all(event=None):
        text_widget.clipboard_clear()
        text_widget.clipboard_append(infotext)

    copy_button = tk.Button(
        parent, 
        text="Copy",
        command=copy_all
    )
    copy_button.pack(pady=5)

    return text_widget

