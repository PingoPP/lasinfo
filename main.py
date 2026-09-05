print("Main imported")

from gui import create_gui 
import tkinter as tk

#Main funcition is the entry point of the program.
#It creates the main window and starts the GUI event loop

def main(stats=None):
    root = tk.Tk()
    root.withdraw()

    open = create_gui()
    return open


if __name__ == "__main__":
    main()