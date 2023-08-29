import pytest
from race_car import RaceCar


@pytest.fixture(autouse=True)
def racecar():
    racecar_obj = RaceCar("red", 130, 10, 4)
    return racecar_obj


def test_is_added_acceleration_cant_added_more_than_max_speed(racecar):
    for i in range(1, 14):
        racecar.accelerate()
    racecar.apply_brakes()
    racecar.accelerate()
    assert racecar.get_current_speed() == 130
    assert racecar.get_nitro_points() == 10

    racecar.apply_brakes()
    racecar.apply_brakes()
    racecar.apply_brakes()
    racecar.apply_brakes()
    racecar.apply_brakes()

    assert racecar.get_nitro_points() == 60
    assert racecar.get_current_speed() == 110

    racecar.accelerate()

    assert racecar.get_current_speed() == 123
    assert racecar.get_nitro_points() == 50

    racecar.accelerate()

    assert racecar.get_current_speed() == 130
    assert racecar.get_nitro_points() == 50


def test_is_added_acceleration_added_when_nitro_points_availabe(racecar):
    for i in range(1, 9):
        racecar.accelerate()

    racecar.apply_brakes()

    racecar.accelerate()
    assert racecar.get_current_speed() == 89


def test_is_nitro_points_getting_added(racecar):
    for i in range(1, 9):
        racecar.accelerate()

    racecar.apply_brakes()

    assert racecar.get_nitro_points() == 10


def test_is_sound_horn_beep_beep(racecar):
    assert racecar.get_sound() == 'Peep Peep\nBeep Beep'


def test_stop_engine_is_working_or_not(racecar):
    racecar.accelerate()  # 10
    racecar.stop_engine()  # set to 0
    racecar.accelerate()  # 10
    racecar.accelerate()  # 20

    assert racecar.get_current_speed() == 20


def test_current_speed_is_set_to_zero_when_current_speed_is_less_than_friction_value(racecar):
    racecar.accelerate()
    racecar.apply_brakes()
    racecar.apply_brakes()
    racecar.apply_brakes()

    assert racecar.get_current_speed() == 0


def test_current_speed_is_decreasing_by_friction_value_when_applying_brake(racecar):
    racecar.accelerate()
    racecar.apply_brakes()
    assert racecar.get_current_speed() == 6


def test_acceleration_cannot_increase_more_than_max_speed(racecar):
    # Here we also covers the get max speed ,engine status and current speed
    for i in range(1, 14):
        racecar.accelerate()
    racecar.accelerate()  # 14 cann't increase more than max speed
    assert racecar.get_current_speed() == 130


def test_is_current_speed_increasing_when_accelerating(racecar):
    racecar.accelerate()
    racecar.accelerate()
    assert racecar.get_current_speed() == 20
