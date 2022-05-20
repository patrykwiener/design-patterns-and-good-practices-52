from abc import ABC, abstractmethod


class ProductActionsInterface(ABC):
    @abstractmethod
    def show_reviews(self):
        pass


class PhysicalProductActionInterface(ProductActionsInterface, ABC):
    @abstractmethod
    def find_in_outlet(self):
        pass


class DigitalProductActionInterface(ProductActionsInterface, ABC):
    @abstractmethod
    def try_for_seven_days(self):
        pass


class ComputerActionsUI(PhysicalProductActionInterface):
    def find_in_outlet(self):
        pass

    def show_reviews(self):
        pass


class SoftwareActionsUI(DigitalProductActionInterface):
    def try_for_seven_days(self):
        pass

    def show_reviews(self):
        pass
