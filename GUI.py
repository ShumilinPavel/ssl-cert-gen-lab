from tkinter import *
from MainFrame import *
from SelfSignedSslFrame import *
from SignedSslFrame import *

# Задание размеров основного окна приложения
GUI_WIDTH = 300
GUI_HEIGHT = 200


# Класс GUI, ссылающийся на остальные экраны
class GUI:
    def __init__(self, master):
        self.master = master

        # Конфигурация основного окна приложения
        master.title("Создание сертификата")
        master.geometry("{0}x{1}+400+200".format(GUI_WIDTH, GUI_HEIGHT))
        master.grid_columnconfigure(0, weight=1)

        # Инициализация и отображение главного экрана с выбором необходимого сертификата для создания
        self.main_frame = MainFrame(self)
        self.main_frame.show()

        # Инициализация экранов создания сертификатов
        self.self_signed_ssl_frame = SelfSignedSslFrame(self)
        self.signed_ssl_frame = SignedSslFrame(self)


if __name__ == '__main__':
    root = Tk()
    gui = GUI(root)
    root.mainloop()
