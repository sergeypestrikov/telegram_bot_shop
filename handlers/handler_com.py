# Импорт класса родителя
from handlers.handler import Handler


class HandlerCommands(Handler):
    """
    Класс обрабатывает входящие команды /start и /help и т.п.
    """
    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_start(self, message):
        """
        Метод обрабатывает входящие /start команды
        """
        self.bot.send_message(message.chat.id,
                              f'{message.from_user.first_name}, '
                              f'здравствуйте! Ожидаю Ваших указаний.',
                              reply_markup=self.keyboard.start_menu())

    def handle(self):
        # Обработчик(декоратор) сообщений,
        # обрабатывающий входящие /start команды
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            if message.text == '/start':
                self.pressed_btn_start(message)