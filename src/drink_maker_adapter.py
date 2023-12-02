from src.deps.drink_maker import DrinkMaker
from src.drink_maker_interface import DrinkMakerInterface
from src.drinks import Drinks


class DrinkMakerAdapter(DrinkMakerInterface):
    drink_maker: DrinkMaker

    def __init__(self, drink_maker: DrinkMaker):
        self.drink_maker = drink_maker

    def print_message(self, message: str) -> None:
        pass

    def make_drink(self, drink: Drinks, sugar: int) -> None:
        if drink == Drinks.COFFEE:
            self.drink_maker.command('C::')
            return
        elif drink == Drinks.TEA:
            self.drink_maker.command('T::')
            return
        self.drink_maker.command('H::')
