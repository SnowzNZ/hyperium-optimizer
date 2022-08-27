import tkinter
import customtkinter
import os
import asyncio
import colorsys
import time

from customtkinter import *
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTkToplevel):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self, user, master):

        super().__init__(master = master)

        self.version = "1.0.0"
        os.chdir(os.path.dirname(os.path.abspath (__file__ )))

        self.username = user.username
        self.password = user.password

        self.title(f"Hyperium Optimizer v{self.version}")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.resizable(False, False)
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.foreground = "#69d466"
        self.hover_colour = "#4fb54c"

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
        self.optimize = CTkButton(master = self.left, width = 140, height = 35, corner_radius=11, text = "Optimize ", text_font = ("Roboto Medium", -16), fg_color = self.foreground, hover_color = self.hover_colour, image = ImageTk.PhotoImage(Image.open("assets/optimize.png").resize((20, 20), Image.Resampling.LANCZOS)), command = lambda: [self.setAllButtonsToNormal(), self.optimize.configure(state = tkinter.DISABLED, fg_color = "#616160"), self.wm_title(f"Hyperium Optimizer v{self.version} | Optimize"), self.clearRightFrame(), self.optimizePanel()])
        self.optimize.grid(row = 3, column = 0, padx = 5, pady = (0, 7))

        # -- -- Clean

        self.clean = CTkButton(master = self.left, width = 140, height = 35, corner_radius=11, text = "Cleaner\t ", text_font = ("Roboto Medium", -16), fg_color = self.foreground, hover_color = self.hover_colour, image = ImageTk.PhotoImage(Image.open("assets/clean.png").resize((20, 20), Image.Resampling.LANCZOS)), command = lambda: [self.setAllButtonsToNormal(), self.clean.configure(state = tkinter.DISABLED, fg_color = "#616160"), self.wm_title(f"Hyperium Optimizer v{self.version} | Clean"), self.clearRightFrame(), self.cleanPanel()])
        self.clean.grid(row = 4, column = 0, padx = 5, pady = 7)

        # -- -- Virus Scan

        self.virusScan = CTkButton(master = self.left, width = 140, height = 35, corner_radius=11, text = "Virus Scan", text_font = ("Roboto Medium", -16), fg_color = self.foreground, hover_color = self.hover_colour, image = ImageTk.PhotoImage(Image.open("assets/virus.png").resize((20, 20), Image.Resampling.LANCZOS)), command = lambda: [self.setAllButtonsToNormal(), self.virusScan.configure(state = tkinter.DISABLED, fg_color = "#616160"), self.wm_title(f"Hyperium Optimizer v{self.version} | Virus Scan"), self.clearRightFrame(), self.virusScanPanel()])
        self.virusScan.grid(row = 5, column = 0, padx = 5, pady = 7)

        # -- -- Settings

        self.settings = CTkButton(master = self.left, width = 140, height = 35, corner_radius=11, text = "Settings\t ", text_font = ("Roboto Medium", -16), fg_color = self.foreground, hover_color = self.hover_colour, image = ImageTk.PhotoImage(Image.open("assets/settings.png").resize((20, 20), Image.Resampling.LANCZOS)), command = lambda: [self.setAllButtonsToNormal(), self.settings.configure(state = tkinter.DISABLED, fg_color = "#616160"), self.wm_title(f"Hyperium Optimizer v{self.version} | Settings"), self.clearRightFrame(), self.settingsPanel()])
        self.settings.grid(row = 6, column = 0, padx = 5, pady = 7)

        # -- -- Account

        self.account = CTkButton(master = self.left, width = 140, height = 35, corner_radius=11, text = "Account\t ", text_font = ("Roboto Medium", -16), fg_color = self.foreground, hover_color = self.hover_colour, image = ImageTk.PhotoImage(Image.open("assets/account.png").resize((20, 20), Image.Resampling.LANCZOS)), command = lambda: [self.setAllButtonsToNormal(), self.account.configure(state = tkinter.DISABLED, fg_color = "#616160"), self.wm_title(f"Hyperium Optimizer v{self.version} | Account"), self.clearRightFrame(), self.accountPanel()])
        self.account.grid(row = 7, column = 0, padx = 5, pady = (7, 0))

        # -- Right Frame

        self.right = customtkinter.CTkFrame(master = self)
        self.right.grid(row = 0, column = 1, sticky = "nswe", padx = 15, pady = 15)

    def optimizePanel(self):
        label = CTkLabel(master = self.right, text = "Optimize Panel", text_font = ("Roboto Medium", -22))
        label.grid(row = 0, column = 0, pady = 20, padx = 20)
        
    def cleanPanel(self):
        label = CTkLabel(master = self.right, text = "Clean Panel", text_font = ("Roboto Medium", -22))
        label.grid(row = 0, column = 0, pady = 20, padx = 20)

    def virusScanPanel(self):
        label = CTkLabel(master = self.right, text = "Virus Scan Panel", text_font = ("Roboto Medium", -22))
        label.grid(row = 0, column = 0, pady = 20, padx = 20)

    def settingsPanel(self):
        label = CTkLabel(master = self.right, text = "Settings Panel", text_font = ("Roboto Medium", -22))
        label.grid(row = 0, column = 0, pady = 20, padx = 20)
        example = CTkSlider(master = self.right, from_ = 0, to = 100, button_length = 10, button_color = "#486ee0", button_hover_color = "#4063c9")
        example.grid(row = 1, column = 0, padx = 20)

    def accountPanel(self):
        pass

    def clearRightFrame(self):
        self.right.destroy()
        self.right = customtkinter.CTkFrame(master = self)
        self.right.grid(row = 0, column = 1, sticky = "nswe", padx = 15, pady = 15)

    def setAllButtonsToNormal(self):
        self.optimize.configure(state = tkinter.NORMAL, fg_color = self.foreground)
        self.clean.configure(state = tkinter.NORMAL, fg_color = self.foreground)
        self.virusScan.configure(state = tkinter.NORMAL, fg_color = self.foreground)
        self.settings.configure(state = tkinter.NORMAL, fg_color = self.foreground)
        self.account.configure(state = tkinter.NORMAL, fg_color = self.foreground)

    def onClose(self, event = 0):
        self.destroy()

def launch(user):
    # Check if user has a license
    master = CTk()
    master.withdraw()
    app = App(user, master)
    app.mainloop()