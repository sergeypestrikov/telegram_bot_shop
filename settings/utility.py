# Конвертация списка с p[(5,),(8,),...] на [5,8,...]
def _convert(list_convert):

    return [itm[0] for itm in list_convert]


# Cчитает общую сумму заказа и возвращает результат
def total_coast(list_quantity, list_price):

    order_total_cost = 0

    for ind, itm in enumerate(list_price):
        order_total_cost += list_quantity[ind]*list_price[ind]

        return order_total_cost


# Cчитает  общее количество заказанной единицы товара и возвращает результат
def total_quantity(list_quantity):

    order_total_quantity = 0

    for itm in list_quantity:
        order_total_quantity += itm

        return order_total_quantity


def get_total_coast(DB):
    """
    Возвращает общую стоимость товара
    """
    # Получаем список всех product_id заказа
    all_product_id = DB.select_all_product_id()
    # Получаем список стоимость по всем позициям заказа в виде обычного списка
    all_price = [DB.select_single_product_price(itm) for itm in all_product_id]
    # Получаем список количества по всем позициям заказа в виде обычного списка
    all_quantity = [DB.select_order_quantity(itm) for itm in all_product_id]
    # Возвращает общую стоимость товара
    return total_coast(all_quantity,all_price)


def get_total_quantity(DB):
    """
    Возвращает общее количество заказанной единицы товара
    """
    # Получаем список все product_id заказа
    all_product_id = DB.select_all_product_id()
    # Получаем список количества по всем позициям заказа в виде обычного списка
    all_quantity = [DB.select_order_quantity(itm) for itm in all_product_id]
    # Возвращает количество товарных позиций
    return total_quantity(all_quantity)
