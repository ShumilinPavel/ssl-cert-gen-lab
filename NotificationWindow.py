from tkinter import *


# Класс уведомления о статусе генерации сертификата
class NotificationWindow:
    def __init__(self, master, status_text):
        self.toplevel = Toplevel(master)
        self.status_text = status_text

        # Конфигурация окна
        self.toplevel.attributes("-toolwindow", 1)
        self.toplevel.geometry('180x100+600+300')

        # Создание элементов окна
        self.__create_message_box()
        self.__create_btn()

        # Компоновка элементов на окне
        self.__pack()

    def __create_message_box(self):
        self.message = Message(self.toplevel, text=self.status_text, width=60)

    def __create_btn(self):
        self.btn = Button(self.toplevel, text='Закрыть', command=self.__close)

    def __close(self):
        self.toplevel.destroy()

    def __pack(self):
        self.message.pack(pady=5, ipadx=5, ipady=5)
        self.btn.pack(pady=5, ipadx=5)
