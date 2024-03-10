import pytest
from car_class.car import Car


@pytest.fixture
def get_new_car2():
    expected_model = 'X5'
    expected_brand = 'BMW'
    expected_miles_limit = 300
    return Car(expected_brand, expected_model, expected_miles_limit)


@pytest.fixture(scope='module', autouse=False)
def get_model():
    return 'X6'


@pytest.fixture(scope='module', autouse=False)
def get_brand():
    return 'BMW'


@pytest.fixture(scope='module', autouse=False)
def get_miles_limit():
    return 100


@pytest.fixture(scope='module', autouse=False)  # by default (scope='function', autouse=False)
def get_new_car(get_brand, get_model, get_miles_limit):
    return Car(brand=get_brand, model=get_model, miles_limit=get_miles_limit)


@pytest.fixture(scope='function', autouse=True)
def clear_history_miles_to_drive(get_new_car, get_miles_limit): #running before test
    yield
    print('clear_miles_to_drive') #running after test
    get_new_car.clear_miles_to_drive(get_miles_limit)
