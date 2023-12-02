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
        if sugar == 1:
            self.drink_maker.command('T:1:0')
            return

        drink_char = 'H'

        if drink == Drinks.COFFEE:
            drink_char = 'C'
        elif drink == Drinks.TEA:
            drink_char = 'T'

        self.drink_maker.command(drink_char + '::')
