class Vehicle:
    def __init__(self, name, model):
        self._name = name  # self.__name is private attr
        self._model = model  # self.__model is private attr
        self._speed = 0

    def get_name(self):
        return self._name

    def set_name(self, name):
        # If you have rules to name, then they should be here.? data integrity
        self._name = name

    def get_speed(self):
        return f"Vehicle Speed is {self._speed}"
