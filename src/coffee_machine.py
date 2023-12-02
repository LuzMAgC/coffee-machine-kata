from src.drink_maker_adapter import DrinkMakerAdapter
from src.drinks import Drinks


class CoffeeMachine:
    drink_maker_adapter: DrinkMakerAdapter
    drink: Drinks = None
    sugar: int = 0

    def __init__(self, drink_maker_adapter: DrinkMakerAdapter):
        self.drink_maker_adapter = drink_maker_adapter

    def set_drink(self, drink: Drinks) -> None:
        self.drink = drink

    def make_drink(self) -> None:
        if self.drink is None:
            self.drink_maker_adapter.print_message('Please select a drink first')
            return
        self.drink_maker_adapter.make_drink(self.drink, self.sugar)

    def add_sugar(self) -> None:
        self.sugar = 1
