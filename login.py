import customtkinter, tkinter, os

from customtkinter import *
from app import launch
from user import User

from PIL import ImageTk, Image

class Login(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title(f"Hyperium Optimizer | Login")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.resizable(False, False)

        self.background = ImageTk.PhotoImage(Image.open("assets/gradient.png").resize((Login.WIDTH, Login.HEIGHT), Image.ANTIALIAS))

        self.image_label = tkinter.Label(master = self, image = self.background)
        self.image_label.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        self.center = CTkFrame(master = self, height = Login.HEIGHT, width = 270, corner_radius = 0)
        self.center.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        title = CTkLabel(master = self.center, text = "Login", text_font = ("Roboto Medium", -32))
        title.place(relx = 0.5, rely = 0.1, anchor = tkinter.CENTER)

        self.username = CTkEntry(master = self.center, placeholder_text = "Username")
        self.username.place(relx = 0.5, rely = 0.2, anchor = tkinter.CENTER)

        self.password = CTkEntry(master = self.center, placeholder_text = "Password", show = "•")
        self.password.place(relx = 0.5, rely = 0.275, anchor = tkinter.CENTER)

        self.login = CTkButton(master = self.center, text = "Login", fg_color = "#486ee0", hover_color = "#4063c9", command = self.login)
        self.login.place(relx = 0.5, rely = 0.35, anchor = tkinter.CENTER)

    def onClose(self, event = 0):
        self.destroy()

    def login(self):
        user = User(self.username.get(), self.password.get())
        self.destroy()
        launch(user)

app = Login()
app.mainloop()