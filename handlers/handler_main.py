# Импорт класса HandlerCommands - обработка команд
from handlers.handler_com import HandlerCommands
# Обработка нажатия на кнопки и иные сообщения
from handlers.handler_all_text import HandlerAllText
# Импорт класса HandlerInlineQuery обработки нажатия на кнопки инлайн
from handlers.handler_inline_query import HandlerInlineQuery


# Будет принимать объект бота, выполнять инициализацию и запуск всех обработчиков
class HandlerMain:
    """
    Класс-компоновщик
    """
    def __init__(self, bot):
        # Получаем нашего бота
        self.bot = bot
        # Здесь происходит инициализация обработчиков
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_all_text = HandlerAllText(self.bot)
        self.handler_inline_query = HandlerInlineQuery(self.bot)

    def handle(self):
        # А здесь происходит запуск обработчиков
        self.handler_commands.handle()
        self.handler_all_text.handle()
        self.handler_inline_query.handle()