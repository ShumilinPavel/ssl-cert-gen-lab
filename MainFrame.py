from tkinter import *
from GUI import GUI_WIDTH, GUI_HEIGHT


# Класс основного экрана с выбором сертификата для создания
class MainFrame:
    def __init__(self, gui):
        self.master = gui.master
        self.gui = gui

        self.frame = Frame(self.master, width=200, height=200)

        # Создание элементов экрана
        self.__create_title()
        self.__create_radio_buttons()
        self.__create_nav_buttons()

        # Компоновка элементов на экране
        self.__grid()

    def show(self):
        self.frame.grid()
        self.master.geometry('{0}x{1}'.format(GUI_WIDTH, GUI_HEIGHT))

    def __create_title(self):
        self.lbl_title = Label(self.frame, text='Выберите тип сертификата')

    def __create_radio_buttons(self):
        self.radio_checked_var = BooleanVar()
        self.radio_checked_var.set(0)

        self.radio_self_signed_ssl = Radiobutton(self.frame, text='Самоподписанный',
                                                 variable=self.radio_checked_var, value=0)
        self.radio_signed_ssl = Radiobutton(self.frame, text='Подписанный',
                                            variable=self.radio_checked_var, value=1)

    def __create_nav_buttons(self):
        self.btn_back = Button(self.frame, text='Назад')
        self.btn_back['state'] = 'disable'

        self.btn_next = Button(self.frame, text='Далее', command=self.__next)

    def __next(self):
        self.frame.grid_remove()
        # Показ следующего экрана в зависимости от выбранного сертификата для создания
        if self.radio_checked_var.get() == 0:
            self.gui.self_signed_ssl_frame.show()
        elif self.radio_checked_var.get() == 1:
            self.gui.signed_ssl_frame.show()

    def __grid(self):
        self.lbl_title.grid(row=0, column=0, columnspan=2, padx=25, pady=25, sticky='nsew')
        self.radio_self_signed_ssl.grid(row=1, column=0, columnspan=2, sticky='w')
        self.radio_signed_ssl.grid(row=2, column=0, columnspan=2, sticky='w')
        self.btn_back.grid(row=3, column=0, pady=15, padx=5, sticky='nsew')
        self.btn_next.grid(row=3, column=1, pady=15, sticky='nsew')
