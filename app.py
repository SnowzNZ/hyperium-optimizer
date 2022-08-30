# Imports

import tkinter, customtkinter, os, json, pyperclip
from win10toast import ToastNotifier
from tkinter import messagebox
from customtkinter import *
from PIL import ImageTk, Image
from application import auth

# Custom Tkinter Settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App

class App(CTkToplevel):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self, master, user):

        super().__init__(master = master)

        self.version = "1.0.0"
        self.user = user
        self.toastNotifier = ToastNotifier()
        os.chdir(os.path.dirname(os.path.abspath(__file__ )))

        # Initialize CustomTkinter Window

        self.title(f"Hyperium Optimizer v{self.version}")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.resizable(False, False)
        
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        colour_theme = self.getColourTheme()
        self.foreground = colour_theme[0]
        self.hover_colour = colour_theme[1]
        self.disabled_colour = colour_theme[2]
        self.text_colour = "#ffffff"

        # Frames

        # -- Left Frame

        self.createLeftFrame()
        self.addLeftPanelFeatures()

        # -- Right Frame

        self.createRightFrame()

    def optimizePanel(self):
        label = CTkLabel(master = self.right, text = "Optimize Panel", text_font = ("Roboto Medium", -22))
        label.grid(row = 0, column = 0, pady = 20, padx = 20)

        option = CTkSwitch(master = self.right, text = "Kill all faggots", command = lambda: messagebox.showinfo("Received", option.getint()))
        option.grid(row = 1, row = 2)
        
    def cleanPanel(self):
        label = CTkLabel(master = self.right, text = "Clean Panel", text_font = ("Roboto Medium", -22))
        label.grid(row = 0, column = 0, pady = 20, padx = 20)

    def virusScanPanel(self):
        label = CTkLabel(master = self.right, text = "Virus Scan Panel", text_font = ("Roboto Medium", -22))
        label.grid(row = 0, column = 0, pady = 20, padx = 20)

    def settingsPanel(self):

        label = CTkLabel(master = self.right, text = "Settings Panel", text_font = ("Roboto Medium", -22))
        label.grid(row = 0, column = 0, pady = 20, padx = 20)

        self.colourPicker = CTkOptionMenu(master = self.right, button_color = self.foreground, button_hover_color = self.hover_colour, fg_color = self.hover_colour, values = ["Red", "Green", "Blue", "Yellow", "Orange", "Pink", "Purple", "Grey"], command = self.changeColourTheme)
        self.colourPicker.grid(row = 1, column = 0, padx = 20, pady = 20)
        self.colourPicker.set(self.getColourTheme()[3].capitalize())

    def getColourTheme(self):

        with open("settings.json", "r") as f:
            settings = json.load(f)

        colours = ["#ff6054", "#5fd14d", "#428dd4", "#cccf4e", "#e0900d", "#d498d3", "#b959d9", "#a8a7a8"]
        hover_colours = ["#c7453c", "#46a337", "#3373b0", "#a6a838", "#c47e0c", "#a66da5", "#a34dbf", "#7d7a7d"]
        disabled_colours = ["#610f0a", "#1e5216", "#1a456e", "#6f7018", "#754d0b", "#70436f", "#622775", "#4a494a"]
        index = {"red": 0, "green": 1, "blue": 2, "yellow": 3, "orange": 4, "pink": 5, "purple": 6, "grey": 7}

        colour_theme = [colours[index.get(settings["theme"])], hover_colours[index.get(settings["theme"])], disabled_colours[index.get(settings["theme"])], settings["theme"]]
        return colour_theme

    def changeColourTheme(self, colour):

        colours = ["#ff6054", "#5fd14d", "#428dd4", "#cccf4e", "#e0900d", "#d498d3", "#b959d9", "#a8a7a8"]
        hover_colours = ["#c7453c", "#46a337", "#3373b0", "#a6a838", "#c47e0c", "#a66da5", "#a34dbf", "#7d7a7d"]
        disabled_colours = ["#610f0a", "#1e5216", "#1a456e", "#6f7018", "#754d0b", "#70436f", "#622775", "#4a494a"]

        index = {"red": 0, "green": 1, "blue": 2, "yellow": 3, "orange": 4, "pink": 5, "purple": 6, "grey": 7}

        self.foreground = colours[index.get(colour.lower())]
        self.hover_colour = hover_colours[index.get(colour.lower())]
        self.disabled_colour = disabled_colours[index.get(colour.lower())]

        with open("settings.json", "r") as f:
            settings = json.load(f)

        if settings["theme"] == colour.lower(): return
        
        settings["theme"] = colour.lower()

        with open("settings.json", "w") as f:
            json.dump(settings, f, indent = 2)

        self.refreshLeftFrame()
        self.refreshRightFrame()
        self.settingsPanel()
        self.setAllButtonsToNormal()
        self.settings.configure(state = DISABLED, fg_color = self.disabled_colour)

    def accountPanel(self):

        username = self.user.username

        title = CTkLabel(master = self.right, text = "Account Settings", text_font = ("Roboto Medium", -24))
        title.grid(row = 0, column = 0, padx = 6, pady = 10, sticky = "w")

        frame = CTkFrame(master = self.right, width = 400, height = 300)
        frame.grid(row = 1, column = 0, padx = 10, pady = 7)
        frame.grid_rowconfigure((0, 1, 2, 3, 4), weight = 1, minsize = 60)

        usernameLabel = CTkLabel(master = frame, text = f"Username: {username}")
        usernameLabel.grid(row = 0, column = 0, padx = (1, 0), pady = 10, sticky = "nw")

        usernameCopy = CTkButton(master = frame, text = "Copy", width = 60, fg_color = None, border_width = 2, height = 17, hover_color = self.hover_colour, command = lambda: [pyperclip.copy(username), self.toastNotifier.show_toast("Hyperium Optimizer", "Username Copied", threaded = True, duration = 3.5)])
        usernameCopy.grid(row = 0, column = 1, padx = (0, 10), pady = 10, sticky = "nw")

        deleteAccount = CTkButton(master = frame, text = "Delete Account", fg_color = "#ff554d", hover_color = "#d6453e", width = 100)
        deleteAccount.grid(row = 4, column = 0, padx = 8, pady = 8, sticky = "ws")

    def clearRightFrame(self):
        self.right.destroy()
        self.right = CTkFrame(master = self)
        self.right.grid(row = 0, column = 1, sticky = "nswe", padx = 15, pady = 15)

    def setAllButtonsToNormal(self):
        self.optimize.configure(state = tkinter.NORMAL, fg_color = self.foreground)
        self.clean.configure(state = tkinter.NORMAL, fg_color = self.foreground)
        self.virusScan.configure(state = tkinter.NORMAL, fg_color = self.foreground)
        self.settings.configure(state = tkinter.NORMAL, fg_color = self.foreground)
        self.account.configure(state = tkinter.NORMAL, fg_color = self.foreground)

    def refresh(self):
        master = self.master
        self.destroy()
        app = App(master = master)
        app.mainloop()

    def createRightFrame(self):
        self.right = CTkFrame(master = self)
        self.right.grid(row = 0, column = 1, sticky = "nswe", padx = 15, pady = 15)

    def refreshRightFrame(self):
        self.right.destroy()
        self.createRightFrame()

    def createLeftFrame(self):
        self.left = CTkFrame(master = self, width = 180, corner_radius = 0)
        self.left.grid(row = 0, column = 0, sticky = "nswe")

    def refreshLeftFrame(self):
        self.left.destroy()
        self.createLeftFrame()
        self.addLeftPanelFeatures()

    def addLeftPanelFeatures(self):
        
        # -- -- Title

        self.title = CTkLabel(master = self.left, text = "Hyperium Optimizer", text_font = ("Roboto Medium", -16))
        self.title.grid(row = 0, column = 0, padx = 10, pady = (10, 34))

        self.versionLabel = CTkLabel(master = self.left, text = f"Version {self.version}", text_font = ("Roboto Medium", -10), text_color = "#616160")
        self.versionLabel.grid(row = 0, column = 0, padx = 10, pady = (25, 0))

        # -- -- Optimize

        self.left.rowconfigure((1, 2), minsize = 10)
        self.optimize = CTkButton(master = self.left, width = 140, height = 35, corner_radius=11, text = "Optimize ", text_font = ("Roboto Medium", -16), fg_color = self.foreground, hover_color = self.hover_colour, image = ImageTk.PhotoImage(Image.open("assets/optimize.png").resize((20, 20), Image.ANTIALIAS)), command = lambda: [self.setAllButtonsToNormal(), self.optimize.configure(state = DISABLED, fg_color = self.disabled_colour), self.wm_title(f"Hyperium Optimizer v{self.version} | Optimize"), self.clearRightFrame(), self.optimizePanel()])
        self.optimize.grid(row = 3, column = 0, padx = 5, pady = (0, 7))

        # -- -- Clean

        self.clean = CTkButton(master = self.left, width = 140, height = 35, corner_radius=11, text = "Cleaner\t ", text_font = ("Roboto Medium", -16), fg_color = self.foreground, hover_color = self.hover_colour, image = ImageTk.PhotoImage(Image.open("assets/clean.png").resize((20, 20), Image.ANTIALIAS)), command = lambda: [self.setAllButtonsToNormal(), self.clean.configure(state = DISABLED, fg_color = self.disabled_colour), self.wm_title(f"Hyperium Optimizer v{self.version} | Clean"), self.clearRightFrame(), self.cleanPanel()])
        self.clean.grid(row = 4, column = 0, padx = 5, pady = 7)

        # -- -- Virus Scan

        self.virusScan = CTkButton(master = self.left, width = 140, height = 35, corner_radius=11, text = "Virus Scan", text_font = ("Roboto Medium", -16), fg_color = self.foreground, hover_color = self.hover_colour, image = ImageTk.PhotoImage(Image.open("assets/virus.png").resize((20, 20), Image.ANTIALIAS)), command = lambda: [self.setAllButtonsToNormal(), self.virusScan.configure(state = DISABLED, fg_color = self.disabled_colour), self.wm_title(f"Hyperium Optimizer v{self.version} | Virus Scan"), self.clearRightFrame(), self.virusScanPanel()])
        self.virusScan.grid(row = 5, column = 0, padx = 5, pady = 7)

        # -- -- Settings

        self.settings = CTkButton(master = self.left, width = 140, height = 35, corner_radius=11, text = "Settings\t ", text_font = ("Roboto Medium", -16), fg_color = self.foreground, hover_color = self.hover_colour, image = ImageTk.PhotoImage(Image.open("assets/settings.png").resize((20, 20), Image.ANTIALIAS)), command = lambda: [self.setAllButtonsToNormal(), self.settings.configure(state = DISABLED, fg_color = self.disabled_colour), self.wm_title(f"Hyperium Optimizer v{self.version} | Settings"), self.clearRightFrame(), self.settingsPanel()])
        self.settings.grid(row = 6, column = 0, padx = 5, pady = 7)

        # -- -- Account

        self.account = CTkButton(master = self.left, width = 140, height = 35, corner_radius=11, text = "Account\t ", text_font = ("Roboto Medium", -16), fg_color = self.foreground, hover_color = self.hover_colour, image = ImageTk.PhotoImage(Image.open("assets/account.png").resize((20, 20), Image.ANTIALIAS)), command = lambda: [self.setAllButtonsToNormal(), self.account.configure(state = DISABLED, fg_color = self.disabled_colour), self.wm_title(f"Hyperium Optimizer v{self.version} | Account"), self.clearRightFrame(), self.accountPanel()])
        self.account.grid(row = 7, column = 0, padx = 5, pady = (7, 0))

    def onClose(self, event = 0):
        self.destroy()

