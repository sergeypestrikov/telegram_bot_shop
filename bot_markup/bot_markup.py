# Импорт специального типа телеграм бота для создания элементов интерфейса
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
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
        if name == "AMOUNT_ORDERS":
            config.KEYBOARD["AMOUNT_ORDERS"] = "{} {} {}".format(step + 1, ' из ', str(
                    self.DB.count_rows_order()))

        if name == "AMOUNT_PRODUCT":
            config.KEYBOARD["AMOUNT_PRODUCT"] = "{}".format(quantity)

        return KeyboardButton(config.KEYBOARD[name])

    def start_menu(self):
        """
        Создает разметку кнопок в основном меню и возвращает разметку
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('CHOOSE_GOODS')
        itm_btn_2 = self.set_btn('INFO')
        itm_btn_3 = self.set_btn('SETTINGS')
        # Расположение кнопок в меню
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    def info_menu(self):
        """
        Создает разметку кнопок в меню 'О магазине'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # Расположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    def settings_menu(self):
        """
        Создает разметку кнопок в меню 'Настройки'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # Расположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    @staticmethod
    def remove_menu():
        """
        Удаляет меню
        """
        return ReplyKeyboardRemove()

    def category_menu(self):
        """
        Создает и возвращает разметку в меню категорий товаров
        """
        self.markup = ReplyKeyboardMarkup(True, True, row_width=1)
        self.markup.add(self.set_btn('PROTEIN'))
        self.markup.add(self.set_btn('GYM'))
        self.markup.add(self.set_btn('POOL'))
        self.markup.add(self.set_btn('TRAINING'))
        self.markup.row(self.set_btn('<<'), self.set_btn('ORDER'))
        return self.markup

    @staticmethod
    def set_inline_btn(name):
        """
        Создает и возвращает инлайн-кнопку по входным параметрам
        """
        return InlineKeyboardButton(str(name), callback_data=str(name.id))

    def set_select_category(self, category):
        """
        Создает и возвращает разметку инлайн-кнопок
        в выбранной категории товара
        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        # Подгрузка данных инлайн-кнопок из БД
        # в соответствии с категорией товара
        for itm in self.DB.select_all_products_category(category):
            self.markup.add(self.set_inline_btn(itm))

        return self.markup

    def orders_menu(self, step, quantity):
        """
        Создает разметку кнопок в заказе товара и возвращает разметку
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('X', step, quantity)
        itm_btn_2 = self.set_btn('DOWN', step, quantity)
        itm_btn_3 = self.set_btn('AMOUNT_PRODUCT', step, quantity)
        itm_btn_4 = self.set_btn('UP', step, quantity)

        itm_btn_5 = self.set_btn('BACK_STEP', step, quantity)
        itm_btn_6 = self.set_btn('AMOUNT_ORDERS', step, quantity)
        itm_btn_7 = self.set_btn('NEXT_STEP', step, quantity)
        itm_btn_8 = self.set_btn('APPLY', step, quantity)
        itm_btn_9 = self.set_btn('<<', step, quantity)
        # Расположение кнопок в меню
        self.markup.row(itm_btn_1, itm_btn_2, itm_btn_3, itm_btn_4)
        self.markup.row(itm_btn_5, itm_btn_6, itm_btn_7)
        self.markup.row(itm_btn_9, itm_btn_8)

        return self.markup