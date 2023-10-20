from src.item import Item


class MixinLang:
    def __init__(self, language='EN'):
        self.__language = language

    @property
    def language(self):
        return f"{self.__language}"

    def change_lang(self):
        if self.language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(Item, MixinLang):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
