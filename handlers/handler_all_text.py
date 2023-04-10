# Импорт ответа пользователю
from settings.message import MESSAGES
from settings import config, utility
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

    def pressed_btn_order(self, message):
        """
        Обрабатывает входящие текстовые сообщения от нажатия на кнопку 'Заказ'.
        """
        # Обнуление данных шага
        self.step = 0
        # Получение списка всех товаров в заказе
        count = self.DB.select_all_product_id()
        # Получение количества по каждой позиции товара в заказе
        quantity = self.DB.select_order_quantity(count[self.step])

        # Отправка ответа пользователю
        self.send_message_order(count[self.step], quantity, message)

    def send_message_order(self, product_id, quantity, message):
        """
        Отправляет ответ пользователю при выполнении различных действий
        """
        self.bot.send_message(message.chat.id, MESSAGES['order_number'].format(
            self.step + 1), parse_mode="HTML")
        self.bot.send_message(message.chat.id,
                              MESSAGES['order'].
                              format(self.DB.select_single_product_name(
                                  product_id),
                                  self.DB.select_single_product_brand(
                                      product_id),
                                  self.DB.select_single_product_price(
                                      product_id),
                                  self.DB.select_order_quantity(
                                      product_id)),
                              parse_mode="HTML",
                              reply_markup=self.keyboard.orders_menu(
                                  self.step, quantity))

    def pressed_btn_up(self, message):
        """
        Обработка нажатия кнопки увеличения
        количества определенного товара в заказе
        """
        # Получаем список всех товаров в заказе
        count = self.DB.select_all_product_id()
        # Получаем количество конкретной позиции в заказе
        quantity_order = self.DB.select_order_quantity(count[self.step])
        # Получаем количество конкретной позиции
        quantity_product = self.DB.select_single_product_quantity(count[self.step])
        # Если товар есть
        if quantity_product > 0:
            quantity_order += 1
            quantity_product -= 1
            # Вносим изменения в БД orders
            self.DB.update_order_value(count[self.step], 'quantity', quantity_order)
            # Вносим изменения в БД product
            self.DB.update_product_value(count[self.step], 'quantity', quantity_product)
        # Отправляем ответ пользователю
        self.send_message_order(count[self.step], quantity_order, message)

    def pressed_btn_down(self, message):
        """
        Обработка нажатия кнопки уменьшения
        количества определенного товара в заказе
        """
        # Список всех товаров в заказе
        count = self.DB.select_all_product_id()
        # Получаем количество конкретной позиции в заказе
        quantity_order = self.DB.select_order_quantity(count[self.step])
        # Получаем количество конкретной позиции
        quantity_product = self.DB.select_single_product_quantity(count[self.step])
        # Если товар в заказе есть
        if quantity_order > 0:
            quantity_order -= 1
            quantity_product += 1
            # Вносим изменения в БД orders
            self.DB.update_order_value(count[self.step], 'quantity', quantity_order)
            # Вносим изменения в БД product
            self.DB.update_product_value(count[self.step], 'quantity', quantity_product)
        # Отправляем ответ пользователю
        self.send_message_order(count[self.step], quantity_order, message)

    def pressed_btn_x(self, message):
        """
        Обработка нажатия кнопки удаления
        товарной позиции заказа
        """
        # Получаем список всех product_id заказа
        count = self.DB.select_all_product_id()
        # Если список не пуст
        if count.__len__() > 0:
            # Получаем количество конкретной позиции в заказе
            quantity_order = self.DB.select_order_quantity(count[self.step])
            # Получаем количество товара к конкретной
            # Позиции заказа для возврата в product
            quantity_product = self.DB.select_single_product_quantity(count[self.step])
            quantity_product += quantity_order
            # Вносим изменения в БД orders
            self.DB.delete_order(count[self.step])
            # Вносим изменения в БД product
            self.DB.update_product_value(count[self.step], 'quantity', quantity_product)
            # Уменьшаем шаг
            self.step -= 1

        count = self.DB.select_all_product_id()
        # Если список не пуст
        if count.__len__() > 0:
            quantity_order = self.DB.select_order_quantity(count[self.step])
            # Отправляем пользователю сообщение
            self.send_message_order(count[self.step], quantity_order, message)

        else:
            # Если товара нет в заказе отправляем сообщение
            self.bot.send_message(message.chat.id, MESSAGES['no_orders'], parse_mode="HTML",
                                  reply_markup=self.keyboard.category_menu())

    def pressed_btn_back_step(self, message):
        """
        Обработка нажатия кнопки перемещения
        к более ранним товарным позициям заказа
        """
        # Уменьшаем шаг пока шаг не будет равен "0"
        if self.step > 0:
            self.step -= 1
        # Получаем список всех товаров в заказе
        count = self.DB.select_all_product_id()
        quantity = self.DB.select_order_quantity(count[self.step])

        # Отправляем ответ пользователю
        self.send_message_order(count[self.step], quantity, message)

    def pressed_btn_next_step(self, message):
        """
        Обработка нажатия кнопки перемещения
        к более поздним товарным позициям заказа
        """
        # Увеличиваем шаг пока шаг не будет равен количеству строк
        # полей заказа с расчетом цены деления начиная с "0"
        if self.step < self.DB.count_rows_order() - 1:
            self.step += 1
        # Получаем список всех товаров в заказе
        count = self.DB.select_all_product_id()
        # Получаем количество конкретного товара в соответствие с шагом выборки
        quantity = self.DB.select_order_quantity(count[self.step])
        # Отправляем ответ пользователю
        self.send_message_order(count[self.step], quantity, message)

    def pressed_btn_apply(self, message):
        """
        Обрабатывает входящие текстовые сообщения
        при нажатии на кнопку 'Оформить заказ'.
        """
        # Отправляем ответ пользователю
        self.bot.send_message(message.chat.id,
                              MESSAGES['apply'].format(
                                  utility.get_total_coast(self.DB),

                                  utility.get_total_quantity(self.DB)),
                              parse_mode="HTML",
                              reply_markup=self.keyboard.category_menu())
        # отчищаем данные с заказа
        self.DB.delete_all_order()

    def handle(self):
        # Обработчик(декоратор) сообщений,
        # обрабатывающий входящие текстовые сообщения при нажатии кнопок
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            # ********** МЕНЮ ********** #
            if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                self.pressed_btn_category(message)

            if message.text == config.KEYBOARD['INFO']:
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD['SETTINGS']:
                self.pressed_btn_settings(message)

            if message.text == config.KEYBOARD['<<']:
                self.pressed_btn_back(message)

            if message.text == config.KEYBOARD['ORDER']:
                # Если есть заказ
                if self.DB.count_rows_order() > 0:
                    self.pressed_btn_order(message)
                else:
                    self.bot.send_message(message.chat.id, MESSAGES['no_orders'], parse_mode="HTML", reply_markup=self.keyboards.category_menu())

            # ********** МЕНЮ категории товаров ******
            if message.text == config.KEYBOARD['PROTEIN']:
                self.pressed_btn_product(message, 'PROTEIN')

            if message.text == config.KEYBOARD['GYM']:
                self.pressed_btn_product(message, 'GYM')

            if message.text == config.KEYBOARD['POOL']:
                self.pressed_btn_product(message, 'POOL')

            if message.text == config.KEYBOARD['TRAINING']:
                self.pressed_btn_product(message, 'TRAINING')

            # ********** МЕНЮ заказа **********

            if message.text == config.KEYBOARD['UP']:
                self.pressed_btn_up(message)

            if message.text == config.KEYBOARD['DOWN']:
                self.pressed_btn_down(message)

            if message.text == config.KEYBOARD['X']:
                self.pressed_btn_x(message)

            if message.text == config.KEYBOARD['BACK_STEP']:
                self.pressed_btn_back_step(message)

            if message.text == config.KEYBOARD['NEXT_STEP']:
                self.pressed_btn_next_step(message)

            if message.text == config.KEYBOARD['APPLY']:
                self.pressed_btn_apply(message)
            # Иные нажатия и ввод данных пользователем
            else:
                self.bot.send_message(message.chat.id, message.text)