from abc import abstractmethod
from src.drinks import Drinks


class DrinkMakerAdapter:
    @abstractmethod
    def make_drink(self, drink: Drinks, sugar: int) -> None:
        pass

    def print_message(self, message: str) -> None:
        pass
