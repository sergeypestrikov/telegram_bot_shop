# Импорт класса-родителя
from handlers.handler import Handler
# Импорт сообщения пользователю
from settings.message import MESSAGES


class HandlerInlineQuery(Handler):
    """
    Класс обрабатывает входящие сообщения
    при нажатии на инлайн-кнопки
    """
    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_product(self, call, code):
        """
        Обрабатывает входящие запросы при нажатии inline-кнопок товара
        """
        # Создание записи с БД по факту заказа
        self.DB._add_orders(1, code, 1)

        self.bot.answer_callback_query(
            call.id, MESSAGES['product_order'].format(
                self.DB.select_single_product_name(code),
                self.DB.select_single_product_brand(code),
                self.DB.select_single_product_price(code),
                self.DB.select_single_product_quantity(code)),
            show_alert=True)

    def handle(self):
        # Обработчик(декоратор) запросов при нажатии на кнопки товара
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            code = call.data
            if code.isdigit():
                code = int(code)

            self.pressed_btn_product(call, code)