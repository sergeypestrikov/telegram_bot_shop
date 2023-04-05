# Компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, Boolean
from data_base.db_core import Base


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

    def __repr__(self):
        # Метод возвращающий строковое представление объекта
        return self.name