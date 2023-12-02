import pytest

from src.coffee_machine import CoffeeMachine
from src.deps.drink_maker import DrinkMaker
from src.drink_maker_adapter import DrinkMakerAdapter
from src.drinks import Drinks


class TestIntegration:
    @pytest.fixture
    def drink_maker_mock(self, mocker):
        return mocker.MagicMock()

    def test_drink_integration(self, drink_maker_mock):
        # Given
        coffee_machine = CoffeeMachine(DrinkMakerAdapter(drink_maker_mock))

        # When
        coffee_machine.set_drink(Drinks.CHOCOLATE)
        coffee_machine.add_sugar()
        coffee_machine.add_sugar()
        coffee_machine.make_drink()

        # Then
        drink_maker_mock.command.assert_called_once_with('H:2:0')

    def test_error_integration(self, drink_maker_mock):
        # Given
        coffee_machine = CoffeeMachine(DrinkMakerAdapter(drink_maker_mock))

        # When
        coffee_machine.make_drink()

        # Then
        drink_maker_mock.command.assert_called_once_with('M:Please select a drink first')

    def test_full_integration(self):
        # Given
        coffee_machine = CoffeeMachine(DrinkMakerAdapter(DrinkMaker()))

        # When
        coffee_machine.set_drink(Drinks.COFFEE)
        coffee_machine.add_sugar()
        coffee_machine.make_drink()
