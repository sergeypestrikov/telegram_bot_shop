# Импорт специального типа телеграм бота для создания элементов интерфейса
from telebot.types import KeyboardButton
# Импорт настроек и утилит
from settings import config
# Импорт класс-менеджер для работы с библиотекой
from data_base.dbalchemy import DBManager


class Keyboard:
    """
    Класс Keyboard предназначен для создания и разметки интерфейса бота
    """
    # Инициализация разметки
    def __init__(self):
        self.markup = None
        # Инициализация менеджера для работы с БД
        self.DB = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        """
        Создает и возвращает кнопку по входным параметрам
        """

        return KeyboardButton(config.KEYBOARD[name])