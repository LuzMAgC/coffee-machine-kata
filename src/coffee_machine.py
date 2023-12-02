from src.drink_maker_adapter import DrinkMakerAdapter
from src.drinks import Drinks


class CoffeeMachine:
    drink_maker_adapter: DrinkMakerAdapter

    def __init__(self, drink_maker_adapter: DrinkMakerAdapter):
        self.drink_maker_adapter = drink_maker_adapter

    def set_drink(self, drink: Drinks):
        pass

    def make_drink(self):
        self.drink_maker_adapter.make_drink(Drinks.CHOCOLATE, 0)
