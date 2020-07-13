import tkinter as tk
import json
import sys


#read file
with open('player_info.json', 'r') as myfile:
    data=myfile.read()

    obj = json.loads(data)
# GUI window is a subclass of the basic tkinter Frame object
class HelloWorldFrame(tk.Frame):
    def __init__(self, master,name):
        # Call superclass constructor
        tk.Frame.__init__(self, master)
        # Place frame into main window
        self.grid()
        # Create text box with "Hello World" text
        hello = tk.Label(self, text=f"{name}")
        # Place text box into frame
        hello.grid(row=0, column=0)

# Spawn window
if __name__ == "__main__":
    
    # Create main window object
    root = tk.Tk()
    # Set title of window
    root.title("Player Info!!!")
    # Instantiate HelloWorldFrame object
    hello_frame = HelloWorldFrame(root,data)
    # Start GUI
    hello_frame.mainloop()
