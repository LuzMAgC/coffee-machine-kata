import pytest
from src.drink_maker_adapter import DrinkMakerAdapter
from src.drinks import Drinks


class TestDrinkMakerAdapter:

    @pytest.fixture
    def drink_maker_mock(self, mocker):
        return mocker.MagicMock()

    def test_call_command_h_given_chocolate_without_sugar(self, drink_maker_mock):
        # Given
        drink_maker_adapter = DrinkMakerAdapter(drink_maker_mock)

        # When
        drink_maker_adapter.make_drink(Drinks.CHOCOLATE, 0)

        # Then
        drink_maker_mock.command.assert_called_once_with('H::')

    def test_call_command_c_given_coffee_without_sugar(self, drink_maker_mock):
        # Given
        drink_maker_adapter = DrinkMakerAdapter(drink_maker_mock)

        # When
        drink_maker_adapter.make_drink(Drinks.COFFEE, 0)

        # Then
        drink_maker_mock.command.assert_called_once_with('C::')

    def test_call_command_t_given_tea_without_sugar(self, drink_maker_mock):
        # Given
        drink_maker_adapter = DrinkMakerAdapter(drink_maker_mock)

        # When
        drink_maker_adapter.make_drink(Drinks.TEA, 0)

        # Then
        drink_maker_mock.command.assert_called_once_with('T::')

    def test_call_command_t10_given_tea_with_one_sugar(self, drink_maker_mock):
        # Given
        drink_maker_adapter = DrinkMakerAdapter(drink_maker_mock)

        # When
        drink_maker_adapter.make_drink(Drinks.TEA, 1)

        # Then
        drink_maker_mock.command.assert_called_once_with('T:1:0')

    def test_call_command_t20_given_tea_with_two_sugars(self, drink_maker_mock):
        # Given
        drink_maker_adapter = DrinkMakerAdapter(drink_maker_mock)

        # When
        drink_maker_adapter.make_drink(Drinks.TEA, 2)

        # Then
        drink_maker_mock.command.assert_called_once_with('T:2:0')
