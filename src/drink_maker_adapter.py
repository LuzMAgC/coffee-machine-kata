from abc import abstractmethod
from src.drinks import Drinks


class DrinkMakerAdapter:
    @abstractmethod
    def make_drink(self, drink: Drinks, sugar: int):
        pass
