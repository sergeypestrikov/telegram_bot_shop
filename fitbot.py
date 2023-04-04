# Импорт функции создания объекта бота
from telebot import TeleBot
# Импорт основных настроек проекта
from settings import config
# Импорт главного класса-обработчика бота
from handlers.handler_main import HandlerMain


class FitBot:
    """
    Основной класс телеграмм бота (сервер), в основе которого
    используется библиотека pyTelegramBotAPI
    """
    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):
        """
        Инициализация бота
        """
        # Получаем токен
        self.token = config.TOKEN
        # Инициализация бота на основе зарегистрированного токена
        self.bot = TeleBot(self.token)
        # Инициализация обработчика событий
        self.handler = HandlerMain(self.bot)

    def start(self):
        """
        Метод для старта обработчика событий
        """
        self.handler.handle()

    def run_bot(self):
        """
        Метод запускает основные события сервера
        """
        # Обработчик событий
        self.start()
        # Служит для запуска бота (работа в режиме нон-стоп)
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    bot = FitBot()
    bot.run_bot()