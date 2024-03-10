import pytest



class TestCar:

    # def setup_method(self):
    #     print('\nsetup_method was run')
    #
    # def teardown_method(self):
    #     print('\nteardown_method was run')

    def test_get_miles_limit(self, get_new_car, get_miles_limit):
        assert get_new_car.miles_limit == get_miles_limit

    def test_car_initial_state(self, get_new_car, get_miles_limit):
        assert get_new_car.miles_limit == get_miles_limit
        assert not get_new_car.engine_started

    @pytest.mark.engine
    def test_start_engine(self, get_new_car):
        assert get_new_car.start_engine() == "Engine started."
        assert get_new_car.engine_started

    @pytest.mark.engine
    def test_start_engine_already_running(self, get_new_car):
        get_new_car.start_engine()
        assert get_new_car.start_engine() == "Engine is already running."

    @pytest.mark.engine
    def test_stop_engine(self, get_new_car):
        get_new_car.start_engine()
        assert get_new_car.stop_engine() == "Engine stopped."
        assert not get_new_car.engine_started

    @pytest.mark.engine
    def test_stop_engine_already_off(self, get_new_car):
        assert get_new_car.stop_engine() == "Engine is already off."

    @pytest.mark.drive
    def test_drive_when_engine_off(self, get_new_car):
        assert get_new_car.drive(50) == "Cannot drive. Engine is off."

    @pytest.mark.drive
    def test_drive_when_engine_on(self, get_new_car):
        get_new_car.start_engine()
        assert get_new_car.drive(50) == "Driving 50 miles."
        assert get_new_car.miles_limit == 50

    @pytest.mark.drive
    def test_drive_over_miles_limit(self, get_new_car):
        get_new_car.start_engine()
        assert get_new_car.drive(150) == "The miles limit has been exceeded"
        assert get_new_car.miles_limit == 100

    @pytest.mark.drive
    def test_drive_when_engine_off_and_then_started(self, get_new_car):
        get_new_car.stop_engine()
        assert get_new_car.drive(50) == "Cannot drive. Engine is off."
        assert get_new_car.start_engine() == "Engine started."
        assert get_new_car.drive(50) == "Driving 50 miles."
        assert get_new_car.miles_limit == 50

    @pytest.mark.drive
    @pytest.mark.parametrize("miles_to_drive, expected_result", [
        (50, "Driving 50 miles."),
        (150, "The miles limit has been exceeded"),
        (100, "Driving 100 miles."),
    ])
    def test_drive(self, get_new_car, miles_to_drive, expected_result):
        get_new_car.start_engine()
        assert get_new_car.drive(miles_to_drive) == expected_result

    def test_invalid_Attribute(self, get_new_car):
        with pytest.raises(AttributeError):
            self.get_new_car.stop_engine('sdss')
