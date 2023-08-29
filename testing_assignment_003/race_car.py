from testing_assignment_001.car import Car


class RaceCar(Car):
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self._sound = "Peep Peep\nBeep Beep"
        self._nitro_points = 0

    def get_nitro_points(self):
        return self._nitro_points

    def set_nitro_points(self, points):
        self._nitro_points = points

    def apply_brakes(self):
        if (self.get_max_speed() / 2) < self.get_current_speed():
            self.set_nitro_points(self.get_nitro_points() + 10)
        super().apply_brakes()

    def accelerate(self):
        super().accelerate()
        if self.get_nitro_points() > 0 and self.get_current_speed() < self.get_max_speed():
            added_acceleration = round(self.get_acceleration() * 0.3)
            if self.get_current_speed() + added_acceleration >= self.get_max_speed():
                self.set_current_speed(self.get_max_speed())
            else:
                self.set_current_speed(self.get_current_speed() + added_acceleration)

            self.set_nitro_points(self.get_nitro_points() - 10)
