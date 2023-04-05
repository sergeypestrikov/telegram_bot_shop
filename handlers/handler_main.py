# Импорт класса HandlerCommands - обработка команд
from handlers.handler_com import HandlerCommands
# Обработка нажатия на кнопки и иные сообщения
from handlers.handler_all_text import HandlerAllText


# Будет принимать объект бота, выполнять инициализацию и запуск всех обработчиков
class HandlerMain:
    """
    Класс-компоновщик
    """
    def __init__(self, bot):
        # Получаем нашего бота
        self.bot = bot
        # Здесь будет инициализация обработчиков
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_all_text = HandlerAllText(self.bot)

    def handle(self):
        # А здесь будет запуск обработчиков
        self.handler_commands.handle()
        self.handler_all_text.handle()