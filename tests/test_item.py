"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item
from src.phone import Phone
import os

item1 = Item("Bla", 5000, 15)
item2 = Item("Qwa", 3000, 6)
item3 = Item('Pass', 4000, 10)
phone1 = Phone("Nokia", 30000, 20, 2)


def test__init__():
    assert item1.name == 'Bla'
    assert item2.price == 3000
    assert item1.quantity == 15


def test_calculate_total_price():
    assert item1.price * item1.quantity == 75000
    assert item2.price * item2.quantity == 18000


def test_apply_discount():
    assert item1.price * Item.pay_rate == 5000
    assert item2.price * Item.pay_rate == 3000


def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('10.4') == 10


def test_name():
    item1.name = 'blablablablabla'
    assert item1.name == 'blablablab'
    item2.name = 'haha'
    assert item2.name == 'haha'


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert item1.all[0].price == '100'
    assert item1.all[1].quantity == '3'


def test__repr__():
    assert repr(item3) == "Item('Pass', 4000, 10)"


def test__str__():
    assert str(item3) == "Pass"


def test__add__():
    assert phone1 + item1 == 35
    assert item2 + phone1 == 26


def test_instantiate_from_csv_error():
    Item.path = 'haha'
    assert Item.instantiate_from_csv() == 'Отсутствует файл item.csv'


def test_instantiate_from_csv_damaged():
    Item.path = os.path.join(os.path.dirname('src'), 'items_damaged.csv')
    assert Item.instantiate_from_csv() == 'Отсутствует файл item.csv'
