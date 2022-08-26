import customtkinter, tkinter, os

from customtkinter import *
from app import launch
from user import User

class Login(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title(f"Hyperium Optimizer | Login")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.resizable(False, False)

        self.grid_columnconfigure((0, 2), weight = 1)

        title = CTkLabel(text = "Login", text_font = ("Roboto Medium", -32))
        title.grid(row = 0, column = 1, pady = 20)

        self.username = CTkEntry(placeholder_text = "Username")
        self.username.grid(row = 1, column = 1, pady = (10, 80))

        self.password = CTkEntry(placeholder_text = "Password", show = "•")
        self.password.grid(row = 1, column = 1, pady = (80, 80))

        self.login = CTkButton(master = self, text = "Login", fg_color = "#486ee0", hover_color = "#4063c9", command = self.login)
        self.login.grid(row = 1, column = 1, pady = (80, 0))

    def onClose(self, event = 0):
        self.destroy()

    def login(self):
        user = User(self.username.get(), self.password.get())
        self.destroy()
        launch(user)

app = Login()
app.mainloop()