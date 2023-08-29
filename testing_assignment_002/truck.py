from testing_assignment_001.car import Car


class Truck(Car):
    def __init__(self, color, max_speed, acceleration, tyre_friction, max_cargo_weight):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self._max_cargo_weight = max_cargo_weight
        self._sound = "Honk Honk"
        self._current_load = 0

    def get_max_cargo_weight(self):
        return self._max_cargo_weight

    def set_max_cargo_weight(self, max_weight):
        self._max_cargo_weight = max_weight

    def get_current_load(self):
        return self._current_load

    def set_current_load(self, load):
        self._current_load = load

    def load(self, cargo_weight):
        if self.get_is_started():
            raise Exception("Cannot load during a motion")
        if cargo_weight < 0:
            raise ValueError("Invalid value for cargo_weight")

        if cargo_weight + self.get_current_load() > self.get_max_cargo_weight():
            raise Exception("Cannot load cargo more than max limit : {}".format(cargo_weight))
        self.set_current_load(self.get_current_load() + cargo_weight)

    def unload(self, cargo_weight):
        if self.get_is_started():
            raise Exception("Cannot load during a motion")
        if cargo_weight < 0:
            raise ValueError("Invalid value for cargo_weight")
        self.set_current_load(self.get_current_load() - cargo_weight)
