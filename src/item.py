import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity+other.quantity
        else:
            raise ValueError

    @property
    def name(self):
        return f"{self.__name}"

    @name.setter
    def name(self, value: str):
        if len(value) <= 10:
            self.__name = value
        else:
            self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, file: str):
        cls.all = []
        with open(file, newline='', encoding='cp1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cls.all.append(cls(row['name'], row['price'], row['quantity']))

    @staticmethod
    def string_to_number(string_number):
        return int(float(string_number))
