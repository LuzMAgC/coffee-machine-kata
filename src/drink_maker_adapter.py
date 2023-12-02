from src.deps.drink_maker import DrinkMaker
from src.drink_maker_interface import DrinkMakerInterface
from src.drinks import Drinks


class DrinkMakerAdapter(DrinkMakerInterface):
    drink_maker: DrinkMaker

    def __init__(self, drink_maker: DrinkMaker):
        self.drink_maker = drink_maker

    def print_message(self, message: str) -> None:
        self.drink_maker.command('M:' + message)

    def make_drink(self, drink: Drinks, sugar: int) -> None:
        sugar_char = ''
        stick_char = ''
        drink_char = 'H'

        if drink == Drinks.COFFEE:
            drink_char = 'C'
        elif drink == Drinks.TEA:
            drink_char = 'T'

        if sugar != 0:
            sugar_char = str(sugar)
            stick_char = '0'

        self.drink_maker.command(drink_char + ':' + sugar_char + ':' + stick_char)
