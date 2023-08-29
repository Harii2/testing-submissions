class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        if max_speed <= 0:
            raise ValueError("Invalid value for max_speed")
        self._color = color
        self._max_speed = max_speed
        self._acceleration = acceleration
        self._tyre_friction = tyre_friction
        self._is_started = False
        self._current_speed = 0
        self._sound = "Beep Beep"

    def get_color(self):
        return self._color

    def set_color(self, x):
        self._color = x

    def get_max_speed(self):
        return self._max_speed

    def set_max_speed(self, max_speed):
        self._max_speed = max_speed

    def get_acceleration(self):
        return self._acceleration

    def set_acceleration(self, acceleration):
        self._acceleration = acceleration

    def get_tyre_friction(self):
        return self._tyre_friction

    def set_tyre_friction(self, friction):
        self._tyre_friction = friction

    def get_is_started(self):
        return self._is_started

    def set_is_started(self, is_started):
        self._is_started = is_started

    def get_current_speed(self):
        return self._current_speed

    def set_current_speed(self, speed):
        self._current_speed = speed

    def start_engine(self):
        self.set_is_started(True)

    def get_sound(self):
        return self._sound

    def is_engine_started(self):
        return self.get_is_started()

    #
    def accelerate(self):
        if not self.get_is_started():
            self.set_is_started(True)
        if self.get_current_speed() + self.get_acceleration() < self.get_max_speed():
            self.set_current_speed(self.get_current_speed() + self.get_acceleration())
        else:
            self.set_current_speed(self.get_max_speed())

    def apply_brakes(self):
        if self.get_current_speed() > self.get_tyre_friction():
            self.set_current_speed(self.get_current_speed() - self.get_tyre_friction())
        else:
            self.set_current_speed(0)

    def stop_engine(self):
        self.set_current_speed(0)
        self.set_is_started(False)

    def sound_horn(self):
        return self._sound

