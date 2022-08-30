# Imports

import tkinter, customtkinter, os, time

from customtkinter import *
from PIL import ImageTk, Image
from application import auth
from tkinter.messagebox import *
from app import App
from user import User

# Custom Tkinter Settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Main Menu

class MainMenu(CTk):

    WIDTH = 700
    HEIGHT = 360

    def __init__(self):

        super().__init__()

        os.chdir(os.path.dirname(os.path.abspath(__file__ )))

        # Initialize CustomTkinter Window

        self.title(f"Hyperium Optimizer")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.resizable(False, False)
    
        # Frames

        # -- Left

        self.left = CTkFrame(master = self, width = (self.WIDTH / 2) - 30, height = self.HEIGHT - 40)
        self.left.grid(row = 0, column = 0, padx = (20, 10), pady = 20)
        self.left.grid_columnconfigure(0, minsize = (self.WIDTH / 2) - 30)
        self.left.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), minsize = (self.HEIGHT - 40) / 7)

        # -- -- Login

        self.loginLabel = CTkLabel(master = self.left, text = "Login", text_font = ("Roboto Medium", -26))
        self.loginLabel.place(relx = 0.5, rely = 0.16, anchor = tkinter.CENTER)

        self.usernameLogin = CTkEntry(master = self.left, placeholder_text = "Username")
        self.usernameLogin.grid(row = 2, column = 0)

        self.passwordLogin = CTkEntry(master = self.left, placeholder_text = "Password", show = "•")
        self.passwordLogin.grid(row = 3, column = 0)
        self.passwordLoginEye = CTkButton(master = self.left, text = "", fg_color = None, width = 22, height = 22, hover_color = "#4c4d4c", corner_radius = 0, image = ImageTk.PhotoImage(Image.open("assets/eye_open.png").resize((20, 20), Image.ANTIALIAS)), command = lambda: self.showContents(self.passwordLogin, self.passwordLoginEye))
        self.passwordLoginEye.place(relx = 0.78, rely = 0.5, anchor = CENTER)

        self.loginButton = CTkButton(master = self.left, text = "Login", command = lambda: self.login(self.usernameLogin.get(), self.passwordLogin.get()))
        self.loginButton.grid(row = 4, column = 0)

        # -- Right

        self.right = CTkFrame(master = self, width = (self.WIDTH / 2) - 30, height = self.HEIGHT - 40)
        self.right.grid(row = 0, column = 1, padx = (10, 20), pady = 20)
        self.right.grid_columnconfigure(0, minsize = (self.WIDTH / 2) - 30)
        self.right.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), minsize = (self.HEIGHT - 40) / 7)

        self.signupLabel = CTkLabel(master = self.right, text = "Signup", text_font = ("Roboto Medium", -26))
        self.signupLabel.place(relx = 0.5, rely = 0.16, anchor = tkinter.CENTER)

        self.usernameSignup = CTkEntry(master = self.right, placeholder_text = "Username")
        self.usernameSignup.grid(row = 2, column = 0)

        self.passwordSignup = CTkEntry(master = self.right, placeholder_text = "Password", show = "•")
        self.passwordSignup.grid(row = 3, column = 0)
        self.passwordSignupEye = CTkButton(master = self.right, text = "", fg_color = None, width = 22, height = 22, hover_color = "#4c4d4c", corner_radius = 0, image = ImageTk.PhotoImage(Image.open("assets/eye_open.png").resize((20, 20), Image.ANTIALIAS)), command = lambda: self.showContents(self.passwordSignup, self.passwordSignupEye))
        self.passwordSignupEye.place(relx = 0.78, rely = 0.5, anchor = CENTER)

        self.confirmPasswordSignup = CTkEntry(master = self.right, placeholder_text = "Confirm Password", show = "•")
        self.confirmPasswordSignup.grid(row = 4, column = 0)
        self.passwordConfirmSignupEye = CTkButton(master = self.right, text = "", fg_color = None, width = 22, height = 22, hover_color = "#4c4d4c", corner_radius = 0, image = ImageTk.PhotoImage(Image.open("assets/eye_open.png").resize((20, 20), Image.ANTIALIAS)), command = lambda: self.showContents(self.confirmPasswordSignup, self.passwordConfirmSignupEye))
        self.passwordConfirmSignupEye.place(relx = 0.78, rely = 0.6445, anchor = CENTER)

        self.signupButton = CTkButton(master = self.right, text = "Signup", command = lambda: self.signup(self.usernameSignup.get(), self.passwordSignup.get(), self.confirmPasswordSignup.get()))
        self.signupButton.grid(row = 5, column = 0)

    def showContents(self, widget: CTkEntry, button: CTkButton):
        widget.configure(show = "")
        button.configure(command = lambda: [self.hideContents(widget, button)])
        
    def hideContents(self, widget: CTkEntry, button: CTkButton):
        widget.configure(show = "•")
        button.configure(command = lambda: [self.showContents(widget, button)])

    def login(self, username, password):
        
        login = auth.login(username, password)

        if login != None:
            return showerror("An Error Occured", login)

        self.withdraw()
        app = App(self, User(username, password))
        app.mainloop()

    def signup(self, username, password, confirmPassword):
        
        # username taken
        if len(username) > 17:
            return showerror("Oops", "Username must be shorter than 18 characters long!")
        elif len(username) < 4:
            return showerror("Oops", "Username must be greater than 3 characters long!")
        elif password != confirmPassword:
            return showerror("Oops!", "Passwords must match!")
        elif len(password) < 5:
            return showerror("Oops", "Password length must be greater than 4 characters!")

        register = auth.register(username, password, "QWTJI9-IHO90K-IWGMXT-T1EVQX-QPUPTG-XTY8LB")

        if register != None:
            return showerror("An Error Occured", register)

        self.withdraw()
        app = App(self, User(username, password))
        app.mainloop()

    def onClose(self, event = 0):
        self.destroy()

app = MainMenu()
app.mainloop()