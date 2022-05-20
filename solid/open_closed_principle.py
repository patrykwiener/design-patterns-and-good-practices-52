from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def get_discount(self):
        pass


class EasterDiscount(Discount):
    _EASTER_DISCOUNT = '30%'

    def get_discount(self):
        return f'{self._EASTER_DISCOUNT} on Easter'


class BlackFridayDiscount(Discount):
    _BLACK_FRIDAY_DISCOUNT = '50%'

    def get_discount(self):
        return f'{self._BLACK_FRIDAY_DISCOUNT} on Black Friday'


class MothersDayDiscount(Discount):
    _MOTHERS_DAY_DISCOUNT = '65%'

    def get_discount(self):
        return f'{self._MOTHERS_DAY_DISCOUNT} on Mothers Day'


class NewYearDiscount(Discount):
    _NEW_YEAR_DISCOUNT = '15%'

    def get_discount(self):
        return f'{self._NEW_YEAR_DISCOUNT} on New Year'


class DiscountManager:
    def process_discount(self, discount: Discount):
        discount.get_discount()


black_friday = BlackFridayDiscount()
easter = EasterDiscount()

manager = DiscountManager()
manager.process_discount(discount=easter)
manager.process_discount(discount=black_friday)
