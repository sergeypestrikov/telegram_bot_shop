# Путь до БД
from os import path
from datetime import datetime

# Подключение к БД
from sqlalchemy import create_engine
# Операции с БД выполняются через сессию (нужно создать класс сессии)
from sqlalchemy.orm import sessionmaker
from data_base.db_core import Base

from settings import config, utility
from models.product import Product
from models.order import Order
from settings import utility


# Метакласс контролирующий DB Manager и его объекты
# который выполняет постоянную проверку подключения к БД и если соединения нет, он его делает
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

    # Работа с заказом
    def _add_orders(self, quantity, product_id, user_id):
        """
        Метод заполнения заказа
        """
        # Получаем список всех product_id
        all_id_product = self.select_all_product_id()
        # Если данные есть в списке, обновляем таблицы заказа и продуктов
        if product_id in all_id_product:
            quantity_order = self.select_order_quantity(product_id)
            quantity_order += 1
            self.update_order_value(product_id, 'quantity', quantity_order)

            quantity_product = self.select_single_product_quantity(product_id)
            quantity_product -= 1
            self.update_product_value(product_id, 'quantity', quantity_product)
            return
        # Если данных нет, создается новый объект заказа
        else:
            order = Order(quantity=quantity, product_id=product_id, user_id=user_id, data=datetime.now())
            quantity_product = self.select_single_product_quantity(product_id)
            quantity_product -= 1
            self.update_product_value(product_id, 'quantity', quantity_product)

        self._session.add(order)
        self._session.commit()
        self.close()

    # Конвертация списка с p[(5,),(8,),...] на [5,8,...]
    def select_all_product_id(self):
        """
        Возвращает все id товара в заказе
        """
        result = self._session.query(Order.product_id).all()
        self.close()
        # Конвертация результата выборки в вид типа [1, 3, 5...]
        return utility._convert(result)

    def select_order_quantity(self, product_id):
        """
        Возвращает кол-во товара в заказе
        """
        result = self._session.query(Order.quantity).filter_by(product_id=product_id).one()
        self.close()
        return result.quantity

    def select_single_product_quantity(self, row_num):
        """
        Возвращает количество товара на складе
        в соответствии с номером товара - row_num
        Этот номер определяется при выборе товара в интерфейсе
        """
        result = self._session.query(Product.quantity).filter_by(id=row_num).one()
        self.close()
        return result.quantity

    def update_product_value(self, row_num, name, value):
        """
        Обновляет кол-во товара на складе
        в соответствии с номером товара row_num
        """
        self._session.query(Product).filter_by(id=row_num).update({name: value})
        self._session.commit()
        self.close()

    def update_order_value(self, product_id, name, value):
        """
        Обновляет данные указанной позиции заказа
        в соответствии с номером товара row_num
        """
        self._session.query(Order).filter_by(product_id=product_id).update({name: value})
        self._session.commit()
        self.close()

    def select_single_product_name(self, row_num):
        """
        Возвращает название товара
        в соответствии с номером товара row_num
        """
        result = self._session.query(Product.name).filter_by(id=row_num).one()
        self.close()
        return result.name

    def select_single_product_brand(self, row_num):
        """
        Возвращает торговую марку (бренд) товара
        в соответствии с номером товара row_num
        """
        result = self._session.query(Product.brand).filter_by(id=row_num).one()
        self.close()
        return result.brand

    def select_single_product_price(self, row_num):
        """
        Возвращает цену товара
        в соответствии с номером товара row_num
        """
        result = self._session.query(Product.price).filter_by(id=row_num).one()
        self.close()
        return result.price

    def count_rows_order(self):
        """
        Возвращает кол-во позиций в заказе
        """
        result = self._session.query(Order).count()
        self.close()
        return result

    def delete_order(self, product_id):
        """
        Удаляет данные указанной строки заказа
        """
        self._session.query(Order).filter_by(product_id=product_id).delete()
        self._session.commit()
        self.close()

    def delete_all_order(self):
        """
        Удаляет данные всего заказа
        """
        all_id_orders = self.select_all_order_id()

        for itm in all_id_orders:
            self._session.query(Order).filter_by(id=itm).delete()
            self._session.commit()
        self.close()

    def select_all_order_id(self):
        """
        Возвращает все id заказа
        """
        result = self._session.query(Order.id).all()
        self.close()
        return utility._convert(result)