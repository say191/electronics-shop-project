"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

item1 = Item("Bla", 5000, 15)
item2 = Item("Qwa", 3000, 6)
item3 = Item('Pass', 4000, 10)


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
    Item.instantiate_from_csv('../electronics-shop-project/src/items.csv')
    assert len(Item.all) == 5
    assert Item.all[0].price == '100'
    assert Item.all[1].quantity == '3'


def test_repr():
    assert repr(item3) == "Item('Pass', 4000, 10)"


def test_str():
    assert str(item3) == "Pass"
