# Импорт ответа пользователю
from settings.message import MESSAGES
from settings import config
# Импорт класса-родителя
from handlers.handler import Handler


class HandlerAllText(Handler):
    """
    Класс обрабатывает входящие текстовые сообщения от нажатия на кнопки
    """

    def __init__(self, bot):
        super().__init__(bot)
        # Шаг в заказе
        self.step = 0

    def pressed_btn_category(self, message):
        """
        Обработка события нажатия на кнопку 'Выбрать товар'.
        Это выбор категории товаров
        """
        # Получаем смену меню с основного на категорийное
        self.bot.send_message(message.chat.id, 'Каталог категорий товаров',
                              reply_markup=self.keyboard.remove_menu())
        self.bot.send_message(message.chat.id, 'Выберите категорию товара',
                              reply_markup=self.keyboard.category_menu())

    def pressed_btn_info(self, message):
        """
        Обрабатывает входящие текстовые сообщения
        при нажатии на кнопку 'О магазине'.
        """
        self.bot.send_message(message.chat.id, MESSAGES['trading_store'],
                              parse_mode="HTML",
                              reply_markup=self.keyboard.info_menu())

    def pressed_btn_settings(self, message):
        """
        Обрабатывает входящие текстовые сообщения
        при нажатии на кнопку 'Настройки'
        """
        self.bot.send_message(message.chat.id, MESSAGES['settings'],
                              parse_mode="HTML",
                              reply_markup=self.keyboard.settings_menu())

    def pressed_btn_back(self, message):
        """
        Обрабатывает входящие текстовые сообщения
        при нажатии на кнопку 'Назад'
        """
        self.bot.send_message(message.chat.id, "Вы вернулись назад",
                              reply_markup=self.keyboard.start_menu())

    def pressed_btn_product(self, message, product):
        """
        Обработка события нажатия на кнопку 'Выбрать товар'.
        Выбор товара из категории
        """
        self.bot.send_message(message.chat.id, 'Категория' + config.KEYBOARD[product],
                              reply_markup=self.keyboard.set_select_category(config.CATEGORY[product]))
        self.bot.send_message(message.chat.id, 'Ok', reply_markup=self.keyboard.category_menu())

    def handle(self):
        # Обработчик(декоратор) сообщений,
        # обрабатывающий входящие текстовые сообщения при нажатии кнопок
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            # ********** меню ********** #
            if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                self.pressed_btn_category(message)

            if message.text == config.KEYBOARD['INFO']:
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD['SETTINGS']:
                self.pressed_btn_settings(message)

            if message.text == config.KEYBOARD['<<']:
                self.pressed_btn_back(message)

            # ********** меню (категории товара, ПФ, Бакалея, Мороженое)******
            if message.text == config.KEYBOARD['PROTEIN']:
                self.pressed_btn_product(message, 'PROTEIN')

            if message.text == config.KEYBOARD['GYM']:
                self.pressed_btn_product(message, 'GYM')

            if message.text == config.KEYBOARD['POOL']:
                self.pressed_btn_product(message, 'POOL')