# Путь до БД
from os import path

# Подключение к БД
from sqlalchemy import create_engine
# Операции с БД выполняются через сессию (нужно создать класс сессии)
from sqlalchemy.orm import sessionmaker
from data_base.db_core import Base

from settings import config
from models.product import Product


# Метакласс контролирующий DB Manager и его объекты
# Выполняет постоянную проверку подключения к БД и если соединения нет, он его делает
class Singleton(type):
    """
    Паттерн Singleton предоставляет механизм создания одного
    и только одного объекта класса,
    и предоставление ему глобальной точки доступа.
    """
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class DBManager(metaclass=Singleton):
    """
    Класс-менеджер для работы с БД
    """
    def __init__(self):
        """
        Инициализация сессии и подключение к БД
        """
        self.engine = create_engine(config.DATABASE)
        session = sessionmaker(bind=self.engine)
        self._session = session()
        if not path.isfile(config.DATABASE):
            Base.metadata.create_all(self.engine)

    def select_all_products_category(self, category):
        """
        Возвращает все товары категории
        """
        result = self._session.query(Product).filter_by(category_id=category).all()
        self.close()
        return result

    def close(self):
        """
        Закрытие сессии
        """
        self._session.close()
