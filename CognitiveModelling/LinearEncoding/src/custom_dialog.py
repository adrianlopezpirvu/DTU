import tkinter as tk

class CustomDialog(tk.Toplevel):
    def __init__(self, parent, title=None, message=None):
        tk.Toplevel.__init__(self, parent)
        
        self.overrideredirect(True) # Remove title bar
        self.title(title)
        self.result = None
        tk.Label(self, text=message, font=("Helvetica", "13", "bold")).pack(padx=20, pady=20)
        self.buttonbox()

        # Wait for the window to be rendered before getting its dimensions
        self.wait_visibility()
        
        # Calculate the position of the input window
        x = parent.winfo_screenwidth() // 2 - self.winfo_reqwidth() // 2
        y = parent.winfo_screenheight() // 2 + 200  # Number of pixels below the center of the screen
        self.geometry("+%d+%d" % (x, y))
        
        # Make the dialog modal
        self.grab_set()
        
        
    def buttonbox(self):
        box = tk.Frame(self)
        c1 = "#f2f2f2"
        c2 = "#d1d1d1"
        c3 = "#8f8f8f"

        self.colors = {
            "Very feminine": c3,
            "Feminine": c2,
            "Neutral": c1,
            "Masculine": c2,
            "Very masculine": c3
        }
        for label, color in self.colors.items():
            tk.Button(box, text=label, width=13, bg=color, font=("Helvetica", "15", "bold"), command=lambda label=label: self.set_result(label)).pack(side=tk.LEFT, padx=5, pady=5)
        
        box.pack()

    # Convert "colors" values to numbers
    def set_result(self, value):
        ratings = list(self.colors.keys())
        self.result = ratings.index(value) + 1
        self.destroy()
