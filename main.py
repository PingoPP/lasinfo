#import os 
#import sys
#conda_env = os.path.dirname(sys.executable)
#os.environ["TCL_LIBRARY"] = os.path.join(conda_env, "Library", "lib", "tcl8.6")
#os.environ["TK_LIBRARY"] = os.path.join(conda_env, "Library", "lib", "tk8.6")
print("Main imported")

from gui import create_gui 
import tkinter as tk

def main(stats=None):
    root = tk.Tk()
    root.withdraw()

    open = create_gui()
    return open


if __name__ == "__main__":
    main()