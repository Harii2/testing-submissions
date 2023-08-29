import pytest

from truck import Truck


@pytest.fixture(autouse=True)
def truck():
    truck_obj = Truck("red", 130, 10, 4, 1000)
    return truck_obj


def test_unloading(truck):
    with pytest.raises(ValueError):
        assert truck.unload(-1)

    truck.accelerate()
    with pytest.raises(Exception):
        assert truck.unload(1000)

    truck.stop_engine()
    truck.set_current_load(400)
    truck.unload(300)
    assert truck.get_current_load() == 100


def test_loading(truck):
    with pytest.raises(ValueError):
        assert truck.load(-1)

    truck.accelerate()
    with pytest.raises(Exception):
        assert truck.load(1000)

    truck.stop_engine()

    with pytest.raises(Exception):
        truck.load(200)
        truck.load(600)
        truck.load(201)
    assert truck.get_current_load() == 800


def test_is_sound_horn_beep_beep(truck):
    assert truck.get_sound() == 'Honk Honk'


def test_stop_engine_is_working_or_not(truck):
    truck.accelerate()  # 10
    truck.stop_engine()  # set to 0
    truck.accelerate()  # 10
    truck.accelerate()  # 20

    assert truck.get_current_speed() == 20


def test_current_speed_is_set_to_zero_when_current_speed_is_less_than_friction_value(truck):
    truck.accelerate()
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()

    assert truck.get_current_speed() == 0


def test_current_speed_is_decreasing_by_friction_value_when_applying_brake(truck):
    truck.accelerate()
    truck.apply_brakes()
    assert truck.get_current_speed() == 6


def test_acceleration_cannot_increase_more_than_max_speed(truck):
    # Here we also covers the get max speed ,engine status and current speed
    for i in range(1, 14):
        truck.accelerate()
    truck.accelerate()  # 14 cann't increase more than max speed
    assert truck.get_current_speed() == 130


def test_is_current_speed_increasing_when_accelerating(truck):
    truck.accelerate()
    truck.accelerate()
    assert truck.get_current_speed() == 20
