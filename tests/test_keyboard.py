from src.keyboard import Keyboard

key = Keyboard('Bla', 3000, 10)


def test__init__():
    assert key.name == 'Bla'
    assert key.price == 3000
    assert key.quantity == 10
    assert key.language == 'EN'


def test__str__():
    assert str(key) == 'Bla'


def test__repr__():
    assert repr(key) == "Keyboard('Bla', 3000, 10)"


def test_change_lang():
    key.change_lang()
    assert key.language == 'RU'
