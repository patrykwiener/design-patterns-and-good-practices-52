class Computer:

    def __init__(self, brand, model):
        self._brand = brand
        self._model = model

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            raise TypeError('Invalid brand type.')

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value


class Inventory:
    def search_inventory(self, computers: list[Computer]):
        pass


computer1 = Computer('Dell', 'XPS 15')
computer2 = Computer('Dell', 'XPS 13')
computer3 = Computer('Apple', 'M1')

computers = [
    computer1,
    computer2,
    computer3,
]

result = Inventory().search_inventory(computers=computers)

# Tak nie chcemy
# computer._brand = 'Ala ma kota'
# print(computer._brand)

print(computer.brand)
computer.brand = 'Apple'
print(computer.brand)

computer.search_inventory()
