import pytest

from car import Car


@pytest.fixture(autouse=True)
def car():
    car_obj = Car("red", 130, 10, 4)
    return car_obj


def test_is_sound_horn_beep_beep(car):
    assert car.get_sound() == 'Beep Beep'


def test_stop_engine_is_working_or_not(car):
    car.accelerate()  # 10
    car.stop_engine()  # set to 0
    car.accelerate()  # 10
    car.accelerate()  # 20

    assert car.get_current_speed() == 20


def test_current_speed_is_set_to_zero_when_current_speed_is_less_than_friction_value(car):
    car.accelerate()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()

    assert car.get_current_speed() == 0


def test_current_speed_is_decreasing_by_friction_value_when_applying_brake(car):
    car.accelerate()
    car.apply_brakes()
    assert car.get_current_speed() == 6


def test_acceleration_cannot_increase_more_than_max_speed(car):
    # Here we also covers the get max speed ,engine status and current speed
    for i in range(1, 14):
        car.accelerate()
    car.accelerate()  # 14 cann't increase more than max speed
    assert car.get_current_speed() == 130


def test_is_current_speed_increasing_when_accelerating(car):
    car.accelerate()
    car.accelerate()
    assert car.get_current_speed() == 20
