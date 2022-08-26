import tkinter
import tkinter.messagebox
import customtkinter
import os
import time

from customtkinter import *
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

os.chdir(os.path.dirname (os.path.abspath (__file__ )))

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()
        self.version = "1.0.0"

        self.title(f"Hyperium Optimizer v{self.version}")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.resizable(False, False)
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Frames

        # -- Left Frame

        self.left = customtkinter.CTkFrame(master = self, width = 180, corner_radius = 0)
        self.left.grid(row = 0, column = 0, sticky = "nswe")

        # -- -- Title

        self.title = CTkLabel(master = self.left, text = "Hyperium Optimizer", text_font = ("Roboto Medium", -16))
        self.title.grid(row = 0, column = 0, padx = 10, pady = (10, 34))

        self.versionLabel = CTkLabel(master = self.left, text = f"Version {self.version}", text_font = ("Roboto Medium", -10), text_color = "#616160")
        self.versionLabel.grid(row = 0, column = 0, padx = 10, pady = (25, 0))

        # -- -- Optimize

        self.left.rowconfigure((1, 2), minsize = 10)
        self.optimize = CTkButton(master = self.left, width = 140, text = "Optimizer ", text_font = ("Roboto Medium", -16), fg_color = "#486ee0", hover_color = "#4063c9", image = ImageTk.PhotoImage(Image.open("assets/optimize.png").resize((20, 20), Image.ANTIALIAS)), command = lambda: [self.optimize.configure(state = tkinter.DISABLED, fg_color = "#616160"), self.wm_title(f"Hyperium Optimizer v{self.version} | Optimize"), self.clearRightFrame(), self.optimizePanel()])
        self.optimize.grid(row = 3, column = 0, padx = 5, pady = (0, 7))

        # -- -- Clean

        self.clean = CTkButton(master = self.left, width = 140, text = "Cleaner\t ", text_font = ("Roboto Medium", -16), fg_color = "#486ee0", hover_color = "#4063c9", image = ImageTk.PhotoImage(Image.open("assets/clean.png").resize((20, 20), Image.ANTIALIAS)))
        self.clean.grid(row = 4, column = 0, padx = 5, pady = 7)

        # -- -- Virus Scan

        self.virusScan = CTkButton(master = self.left, width = 140, text = "Virus Scan", text_font = ("Roboto Medium", -16), fg_color = "#486ee0", hover_color = "#4063c9", image = ImageTk.PhotoImage(Image.open("assets/virus.png").resize((20, 20), Image.ANTIALIAS)))
        self.virusScan.grid(row = 5, column = 0, padx = 5, pady = 7)

        # -- -- Settings

        self.settings = CTkButton(master = self.left, width = 140, text = "Settings\t ", text_font = ("Roboto Medium", -16), fg_color = "#486ee0", hover_color = "#4063c9", image = ImageTk.PhotoImage(Image.open("assets/settings.png").resize((20, 20), Image.ANTIALIAS)))
        self.settings.grid(row = 6, column = 0, padx = 5, pady = (7, 0))

        # -- Right Frame

        self.right = customtkinter.CTkFrame(master = self)
        self.right.grid(row = 0, column = 1, sticky = "nswe", padx = 15, pady = 15)

    def optimizePanel(self):

        label = CTkLabel(master = self.right, text = "Optimize Panel", text_font = ("Roboto Medium", -22))
        label.grid(row = 0, column = 0, pady = 20, padx = 20)

    def clearRightFrame(self):

        self.right.destroy()
        self.right = customtkinter.CTkFrame(master = self)
        self.right.grid(row = 0, column = 1, sticky = "nswe", padx = 15, pady = 15)

    def onClose(self, event = 0):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
