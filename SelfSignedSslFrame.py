from tkinter import *
from CertificateGenerator import *
from NotificationWindow import *

# Задание размеров экрана создания самоподписанного сертификата
SS_FRAME_WIDTH = 600
SS_FRAME_HEIGHT = 300
SS_ENTRY_WIDTH = 70


# Класс экрана с настройкой параметров для создания самоподписанного сертификата
class SelfSignedSslFrame:
    def __init__(self, gui):
        self.master = gui.master
        self.gui = gui

        self.frame = Frame(self.master, width=SS_FRAME_WIDTH, height=SS_FRAME_HEIGHT)
        self.option_boxes = []

        # Пары подпись и начальные значения параметров сертификата
        option_texts = {'Country': 'RU', 'State or province': 'Russia', 'Locality': 'Chelyabinsk',
                        'Organization': 'ke1601spi89', 'Organization unit': 'ke1601spi89',
                        'Common name': 'ke1601spi89', 'Key file name': 'app.key', 'Cert file name': 'app.crt',
                        'Cert dir': 'D:\\SUSU\\Practice\\Безопасность информационных систем\\ssl_generation\\cert'}

        # Создание элементов экрана
        for (lbl_text, entry_text) in option_texts.items():
            self.__create_option_box(lbl_text, entry_text)
        self.__create_nav_buttons()

        # Компоновка элементов на экране
        self.__grid()

    def show(self):
        self.frame.grid()
        self.master.geometry('{0}x{1}'.format(SS_FRAME_WIDTH, SS_FRAME_HEIGHT))

    # Создание опций, состоящих из метки с именем параметра и строки для ввода его значения
    def __create_option_box(self, lbl_text, entry_default_text):
        lbl_option = Label(self.frame, text=lbl_text)
        entry_option = Entry(self.frame, width=SS_ENTRY_WIDTH)
        entry_option.insert(0, entry_default_text)
        self.option_boxes.append((lbl_option, entry_option))

    def __create_nav_buttons(self):
        self.btn_frame = Frame(self.frame)
        self.btn_back = Button(self.btn_frame, text='Назад', command=self.__back, width=20)
        self.btn_confirm = Button(self.btn_frame, text='OK', command=self.__generate_certificate, width=20)

    # Возврат на главный экран
    def __back(self):
        self.frame.grid_remove()
        self.gui.main_frame.show()

    def __generate_certificate(self):
        params = self.__get_params()
        # Создание экземпляра генератора сертификатов
        cert_gen = CertificateGenerator(params)
        success = cert_gen.create_self_signed_cert()
        # Уведомление о статусе генерации сертификата
        if success:
            NotificationWindow(self.frame, 'Успех')
        else:
            NotificationWindow(self.frame, 'Ошибка')

    # Формирование словаря с параметрами в формате, необходимом для создания сертификата
    def __get_params(self):
        params = {}
        for (label, entry) in self.option_boxes:
            value = entry.get()
            label_text = label['text']
            if label_text == 'Country':
                params['C'] = value
            elif label_text == 'State or province':
                params['ST'] = value
            elif label_text == 'Locality':
                params['L'] = value
            elif label_text == 'Organization':
                params['O'] = value
            elif label_text == 'Organization unit':
                params['OU'] = value
            elif label_text == 'Common name':
                params['CN'] = value
            else:
                params[label_text] = value
        return params

    def __grid(self):
        row_id = 0
        for (lbl, entry) in self.option_boxes:
            lbl.grid(row=row_id, column=0, pady=2.5, padx=5)
            entry.grid(row=row_id, column=1, pady=2.5)
            row_id += 1

        self.btn_frame.grid(row=row_id, column=0, columnspan=2, pady=10)
        self.btn_back.grid(row=0, column=0, padx=10)
        self.btn_confirm.grid(row=0, column=1)
