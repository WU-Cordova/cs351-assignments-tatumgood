import pytest
import copy

from car import Car, Color, Make, Model

class TestCopyMethods:
    @pytest.fixture
    def cars_list(self) -> list[Car]:
        cars: list[Car] = []
        cars.append(Car(vin='123', color=Color.RED, make=Make.TOYOTA, model=Model.CAMRY))
        cars.append(Car(vin='456', color=Color.RED, make=Make.FORD, model=Model.FOCUS))
        cars.append(Car(vin='789', color=Color.RED, make=Make.HONDA, model=Model.CIVIC))
        return cars

    @pytest.fixture
    def numbers_list(self) -> list[int]:
        numbers: list[int] = [0] * 10
        for i in range(10):
            numbers[i] = i
        return numbers   
    
    def test_car_shallow_copy(self):
        # Arrange (set up your test data)
        car = Car(vin='123', color=Color.RED, make=Make.TOYOTA, model=Model.CAMRY)

        # Act (perform the action you want to test)
        car_shallow_copy = car
        car_shallow_copy.color = Color.GREEN

        # Assert (check that the test is passing)
        assert car.color == Color.GREEN

    def test_car_deep_copy(self):
        # Arrange (set up your test data)
        car = Car(vin='123', color=Color.RED, make=Make.TOYOTA, model=Model.CAMRY)

        # Act (perform the action you want to test)
        car_deep_copy = copy.deepcopy(car) #import copy
        car_deep_copy.color = Color.GREEN

        # Assert (check that the test is passing)
        assert car.color == Color.RED

    def test_car_deep_copy_with_object_reference(self):
        # Arrange (set up your test data)
        car = Car(vin='123', color=Color.RED, make=Make.TOYOTA, model=Model.CAMRY)

        # Act (perform the action you want to test)
        car_deep_copy = copy.deepcopy(car)

        # Assert (check that the test is passing)
        assert car is not car_deep_copy

    def test_car_list_shallow_copy(self, cars_list: list[Car]):
        # Arrange (set up your test data)
        cars_shallow_copy = cars_list # can also say: cars_shallow_copy = cars_list.copy()

        # Act (perform the action you want to test)
        cars_shallow_copy[0].color = Color.GREEN

        # Assert (check that the test is passing)
        assert cars_list[0].color == Color.GREEN


    def test_car_list_deep_copy(self, cars_list: list[Car]):
        # Arrange (set up your test data)
        cars_deep_copy = copy.deepcopy(cars_list)

        # Act (perform the action you want to test)
        cars_deep_copy[0].color = Color.GREEN

        # Assert (check that the test is passing)
        assert cars_list[0].color == Color.RED
    
    def test_numbers_list_copy_should_make_shallow_copies(self, numbers_list: list[int]):
        # Arrange (set up your test data)
        numbers_copy = numbers_list

        # Act (perform the action you want to test)
        numbers_copy[0] = 100

        # Assert (check that the test is passing)
        assert numbers_list[0] == 100

    def test_numbers_list_deep_copy(self, numbers_list: list[int]):
        # Arrange (set up your test data)
        numbers_copy = copy.deepcopy(numbers_list)

        # Act (perform the action you want to test)
        numbers_copy[0] = 100

        # Assert (check that the test is passing)
        assert numbers_list[0] == 0
    
    def test_slice_cars_list_should_make_shallow_copies_of_complex_objects(self, cars_list: list[Car]):
        # Arrange (set up your test data)
        cars_copy = cars_list[:]

        # Act (perform the action you want to test)
        cars_copy[0].color = Color.GREEN

        # Assert (check that the test is passing)
        assert cars_list[0].color == Color.GREEN

    def test_slice_numbers_list_should_make_shallow_copies(self, numbers_list: list[int]):
        # Arrange (set up your test data)
        numbers_copy = numbers_list[:]

        # Act (perform the action you want to test)
        numbers_copy[0] = 100

        # Assert (check that the test is passing)
        assert numbers_list[0] == 0