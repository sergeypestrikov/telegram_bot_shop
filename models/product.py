# Компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
# Импорт модуля для связки таблиц
from sqlalchemy.orm import relationship, backref
# Импорт модели Категория для связки моделей
from models.category import Category
from data_base.db_core import Base


class Product(Base):
    """
    Класс для создания таблицы "Товар",
    основан на декларативном стиле SQLAlchemy
    """
    # Название таблицы
    __tablename__ = 'product'

    # Поля таблицы
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    brand = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    is_active = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id'))
    # Для каскадного удаления данных из таблицы
    category = relationship(
        Category,
        backref=backref('product',
                        uselist=True,
                        cascade='delete, all'))

    def __str__(self):
        return f'{self.name} {self.brand} {self.price}'


