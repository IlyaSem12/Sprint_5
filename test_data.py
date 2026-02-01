from dataclasses import dataclass

@dataclass
class RegistrationPageData:
    """Датакласс c данными для регистрации"""
    password: str = '123123123'
    wrong_email: str = '!wrong_email123Dzfvcxcv'


@dataclass
class LoginPageData:
    """Датакласс c данными логина"""
    password: str = '123123123'

@dataclass
class CreatingAdPageData:
    """Датакласс c данными для объявлений"""
    description: str = 'Отличный выбор для тех, кто ценит уникальные, кинематографичные сюжетные игры, которые часто доводятся до совершенства.'
    price: int = 506225