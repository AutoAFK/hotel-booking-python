from tkinter import *
from tkinter import ttk

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Hotel booking")
        self.resizable(False,False)
        mainframe = ttk.Frame(self, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


        self.center_window()
    
    def center_window(self):
        # The current program size
        self.update_idletasks()
        program_width = 400 
        program_height =  200
        # The user screen size
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight() 

        x = (screen_width - program_width) // 2
        y = (screen_height - program_height) // 2
        self.geometry(f'{program_width}x{program_height}+{x}+{y}')

if __name__ == "__main__":
    app = App()
    app.mainloop()
    