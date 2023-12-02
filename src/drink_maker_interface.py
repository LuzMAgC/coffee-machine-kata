from abc import abstractmethod
from src.drinks import Drinks


class DrinkMakerInterface:
    @abstractmethod
    def make_drink(self, drink: Drinks, sugar: int) -> None:
        pass

    @abstractmethod
    def print_message(self, message: str) -> None:
        pass
