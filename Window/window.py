import tkinter
from .widgets import Widgets


class MainWindow(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("200x300")
        self.title("Калькулятор")
        self.buttons = Widgets()
        self.buttons.buttons.create_buttons()


root = MainWindow()
