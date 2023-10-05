"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

item1 = Item("Bla", 5000, 15)
item2 = Item("Qwa", 3000, 6)


def test__init__():
    assert item1.name == 'Bla'
    assert item2.price == 3000
    assert item1.quantity == 15
    assert Item.all == [item1, item2]


def test_calculate_total_price():
    assert item1.price * item1.quantity == 75000
    assert item2.price * item2.quantity == 18000


def test_apply_discount():
    assert item1.price * Item.pay_rate == 5000
    assert item2.price * Item.pay_rate == 3000
