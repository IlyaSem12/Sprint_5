import uuid


def generate_email():
    """Функция для генерации email"""
    return f"test_{uuid.uuid4().hex}@yandex.ru"

def generate_product_name():
    """Функция для генерации имени товара"""
    return f"test_product_name_{uuid.uuid4().hex}"