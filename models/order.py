# Компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, DateTime, Integer, ForeignKey
# Импорт модуля для связки таблиц
from sqlalchemy.orm import relationship, backref
# Класс-конструктор для работы с декларативным стилем SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
# Импорт модели продуктов для связки моделей
from models.product import Product


# Инициализация декларативного стиля
Base = declarative_base()


class Order(Base):
    """
    Класс для создания таблицы "Заказ",
    основан на декларативном стиле SQLAlchemy
    """
    # Название таблицы
    __tablename__ = 'order'

    # Поля таблицы
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    data = Column(DateTime)
    product_id = Column(Integer, ForeignKey('product.id'))
    user_id = Column(Integer)

    # Для каскадного удаления данных из таблицы
    products = relationship(
        Product,
        backref=backref('order',
                        uselist=True,
                        cascade='delete,all'))

    def __str__(self):
        return f'{self.quantity} {self.data}'
