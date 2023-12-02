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