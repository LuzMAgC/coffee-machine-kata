from src.drink_maker_adapter import DrinkMakerAdapter
from src.drinks import Drinks


class CoffeeMachine:
    drink_maker_adapter: DrinkMakerAdapter
    drink: Drinks = None

    def __init__(self, drink_maker_adapter: DrinkMakerAdapter):
        self.drink_maker_adapter = drink_maker_adapter

    def set_drink(self, drink: Drinks) -> None:
        self.drink = drink

    def make_drink(self) -> None:
        if self.drink == Drinks.CHOCOLATE:
            self.drink_maker_adapter.make_drink(Drinks.CHOCOLATE, 0)
            return
        self.drink_maker_adapter.make_drink(Drinks.COFFEE, 0)
