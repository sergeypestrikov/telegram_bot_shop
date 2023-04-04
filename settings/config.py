import os
# Импорт модуля emoji для отображения эмоджи
from emoji import emojize

# Токен - выдается при регистрации приложения
TOKEN = '6012497798:AAH_QIFfdMOkNkFyF1pZtPBi4om9VFjhDio'
# Название БД
NAME_DB = 'product.sqlite'
# Версия приложения
VERSION = '0.0.1'
# Автор приложения
AUTHOR = 'Berber'

# Родительская директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Путь до базы данных
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

# Кнопки управления
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize('⚙️ Настройки'),
    'SEMIPRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Оформить заказ',
    'COPY': '©️'
}

# id категорий продуктов
CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICE_CREAM': 3,
}

# Названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help",
}