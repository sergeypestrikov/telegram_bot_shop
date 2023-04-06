import os
# Импорт модуля emoji для отображения эмоджи
from emoji import emojize

# Токен - выдается при регистрации приложения
TOKEN = '6012497798:AAH_QIFfdMOkNkFyF1pZtPBi4om9VFjhDio'
# Название БД
NAME_DB = 'product.db'
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
    'PROTEIN': emojize(':cut_of_meat: Спортивное питание'),
    'GYM': emojize(':person_lifting_weights: Товары для зала'),
    'POOL': emojize(':woman_swimming: Товары для бассейна'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLY': '✅ Оформить заказ',
    'COPY': '©️'
}

# id категорий продуктов
CATEGORY = {
    'PROTEIN': 1,
    'GYM': 2,
    'POOL': 3,
}

# Названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help",
}