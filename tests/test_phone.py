from src.phone import Phone

phone1 = Phone("Nokia", 30000, 20, 2)
phone2 = Phone("Apple", 50000, 30, 1)


def test__init__():
    assert phone1.name == 'Nokia'
    assert phone2.price == 50000
    assert phone1.quantity == 20
    assert phone2.number_of_sim == 1


def test__repr__():
    assert repr(phone1) == "Phone('Nokia', 30000, 20, 2)"
    assert repr(phone2) == "Phone('Apple', 50000, 30, 1)"


def test__str__():
    assert str(phone1) == 'Nokia'
    assert str(phone2) == 'Apple'


def test_number_of_sim():
    phone1.number_of_sim = 3
    phone2.number_of_sim = 2
    assert phone1.number_of_sim == 3
    assert phone2.number_of_sim == 2
