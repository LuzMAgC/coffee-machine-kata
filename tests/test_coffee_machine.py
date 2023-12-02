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

    def test_shows_error_when_no_drink_is_selected(self, drink_maker_adapter_mock):
        # Given
        coffee_machine = CoffeeMachine(drink_maker_adapter_mock)

        # When
        coffee_machine.make_drink()

        # Then
        drink_maker_adapter_mock.print_message.assert_called_once_with('Please select a drink first')
        drink_maker_adapter_mock.make_drink.assert_not_called()

    def test_prepare_drink_with_one_sugar(self, drink_maker_adapter_mock):
        # Given
        coffee_machine = CoffeeMachine(drink_maker_adapter_mock)

        # When
        coffee_machine.set_drink(Drinks.TEA)
        coffee_machine.add_sugar()
        coffee_machine.make_drink()

        # Then
        drink_maker_adapter_mock.make_drink.assert_called_once_with(Drinks.TEA, 1)

    def test_prepare_drink_with_two_sugars(self, drink_maker_adapter_mock):
        # Given
        coffee_machine = CoffeeMachine(drink_maker_adapter_mock)

        # When
        coffee_machine.set_drink(Drinks.TEA)
        coffee_machine.add_sugar()
        coffee_machine.add_sugar()
        coffee_machine.make_drink()

        # Then
        drink_maker_adapter_mock.make_drink.assert_called_once_with(Drinks.TEA, 2)

    def test_prepare_drink_with_no_more_than_two_sugars(self, drink_maker_adapter_mock):
        # Given
        coffee_machine = CoffeeMachine(drink_maker_adapter_mock)

        # When
        coffee_machine.set_drink(Drinks.TEA)
        coffee_machine.add_sugar()
        coffee_machine.add_sugar()
        coffee_machine.add_sugar()
        coffee_machine.add_sugar()
        coffee_machine.make_drink()

        # Then
        drink_maker_adapter_mock.make_drink.assert_called_once_with(Drinks.TEA, 2)

    def test_prepare_drink_with_one_sugar_after_remove_a_sugar_when_two_sugars_added_first(self, drink_maker_adapter_mock):
        # Given
        coffee_machine = CoffeeMachine(drink_maker_adapter_mock)

        # When
        coffee_machine.set_drink(Drinks.TEA)
        coffee_machine.add_sugar()
        coffee_machine.add_sugar()
        coffee_machine.remove_sugar()
        coffee_machine.make_drink()

        # Then
        drink_maker_adapter_mock.make_drink.assert_called_once_with(Drinks.TEA, 1)

    def test_prepare_drink_with_no_sugar_after_remove_two_sugars_when_two_sugars_added_first(self, drink_maker_adapter_mock):
        # Given
        coffee_machine = CoffeeMachine(drink_maker_adapter_mock)

        # When
        coffee_machine.set_drink(Drinks.TEA)
        coffee_machine.add_sugar()
        coffee_machine.add_sugar()
        coffee_machine.remove_sugar()
        coffee_machine.remove_sugar()
        coffee_machine.make_drink()

        # Then
        drink_maker_adapter_mock.make_drink.assert_called_once_with(Drinks.TEA, 0)

    def test_prepare_drink_with_no_less_than_zero_sugar(self, drink_maker_adapter_mock):
        # Given
        coffee_machine = CoffeeMachine(drink_maker_adapter_mock)

        # When
        coffee_machine.set_drink(Drinks.TEA)
        coffee_machine.remove_sugar()
        coffee_machine.remove_sugar()
        coffee_machine.make_drink()

        # Then
        drink_maker_adapter_mock.make_drink.assert_called_once_with(Drinks.TEA, 0)
