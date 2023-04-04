# Компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, Boolean
# Класс-конструктор для работы с декларативным стилем SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

# Инициализация декларативного стиля
Base = declarative_base()


class Category(Base):
    """
    Класс-модель для описания таблицы "Категория товара",
    основан на декларативном стиле SQLAlchemy
    """
    # Название таблицы
    __tablename__ = 'category'

    # Поля таблицы
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    is_active = Column(Boolean)

    def __str__(self):
        # Метод возвращающий строковое представление класса
        return self.name