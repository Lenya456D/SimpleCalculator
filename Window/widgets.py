import tkinter


class Widgets:
    def __init__(self):
        self.buttons = Buttons()


class Buttons:
    __expression = ""
    __is_equal = False

    def __init__(self):
        self.__label = tkinter.Label(text="0", font=("Ariel", 18))
        self.__label.place(x=0, y=0, width=200, height=50)
        button_clear_all = tkinter.Button(text="C", width=50, height=50, command=self.clear_all)
        button_clear_all.place(x=0, y=100, width=50, height=50)
        button_clear = tkinter.Button(text="<=", width=50, height=50, command=self.clear_one_symbol)
        button_clear.place(x=150, y=100, width=50, height=50)

    def create_buttons(self) -> None:
        text_button = (
            ('/', '*'),
            ('7', '8', '9', '-'),
            ('4', '5', '6', '+'),
            ('1', '2', '3', '='),
        )
        x, y = 50, 100
        for row in range(4):
            for col in range(len(text_button[row])):
                tkinter.Button(text=text_button[row][col], width=6, height=3,
                               command=lambda row=row, col=col: Buttons.__callback_button(
                                   data={'label': self.__label, 'number': text_button[row][col]})).place(x=x, y=y,
                                                                                                         width=50,
                                                                                                         height=50)
                x += 50
            x = 0
            y += 50

    def clear_all(self) -> None:
        self.__label['text'] = ""
        Buttons.__expression = ""

    def clear_one_symbol(self) -> None:
        self.__label['text'] = self.__label['text'][:len(self.__label['text']) - 1]
        Buttons.__expression = Buttons.__expression[:len(Buttons.__expression) - 1]

    @staticmethod
    def __callback_button(data: dict) -> None:
        if data['number'] == '=':
            data['label']['text'] = str(eval(Buttons.__expression))
            Buttons.__expression = ""
            Buttons.__is_equal = True
            return

        if data['label']['text'] == '0' or Buttons.__is_equal:
            data['label']['text'] = data['number']
            Buttons.__is_equal = False
        else:
            data['label']['text'] += data['number']

        Buttons.__expression += data['number']
