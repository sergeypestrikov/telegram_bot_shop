# Импорт библиотеки abc для реализации абстрактных классов
import abc
# Импорт разметку клавиатуры и клавиш
from bot_markup.bot_markup import Keyboard
# импортируем класс-менеджер для работы с библиотекой
from data_base.dbalchemy import DBManager


# Метакласс обработчиков
class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        # Получаем объект бота
        self.bot = bot
        # Инициализация разметки кнопок
        self.keyboard = Keyboard()
        # Инициализация менеджера для работы с БД
        self.BD = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass
