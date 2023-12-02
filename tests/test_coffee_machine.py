import pytest
from src.coffee_machine import CoffeeMachine
from src.drinks import Drinks


class TestCoffeeMachine:

    @pytest.fixture
    def drink_maker_adapter_mock(self, mocker):
        return mocker.MagicMock()

    def test_prepare_chocolate_without_sugar(self, drink_maker_adapter_mock):
        # Given
        coffee_machine = CoffeeMachine(drink_maker_adapter_mock)

        # When
        coffee_machine.set_drink(Drinks.CHOCOLATE)
        coffee_machine.make_drink()

        # Then
        drink_maker_adapter_mock.make_drink.assert_called_once_with(Drinks.CHOCOLATE, 0)

    def test_prepare_coffee_without_sugar(self, drink_maker_adapter_mock):
        # Given
        coffee_machine = CoffeeMachine(drink_maker_adapter_mock)

        # When
        coffee_machine.set_drink(Drinks.COFFEE)
        coffee_machine.make_drink()

        # Then
        drink_maker_adapter_mock.make_drink.assert_called_once_with(Drinks.COFFEE, 0)

    def test_prepare_tea_without_sugar(self, drink_maker_adapter_mock):
        # Given
        coffee_machine = CoffeeMachine(drink_maker_adapter_mock)

        # When
        coffee_machine.set_drink(Drinks.TEA)
        coffee_machine.make_drink()

        # Then
        drink_maker_adapter_mock.make_drink.assert_called_once_with(Drinks.TEA, 0)
