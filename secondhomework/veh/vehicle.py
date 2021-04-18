from dataclasses import dataclass


class Vehicle:

    def __init__(self, name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound

    def __str__(self):
        return f'({self.__class__.__name__}) {self.name}'

    def __repr__(self):
        return f'({self.__class__.__name__}) {self.name}'


class Car(Vehicle):
    fuel = 100

    def __init__(self, name, color, sound, wheels, consumption):
        super().__init__(name, color, sound)
        self.wheels = wheels
        self.consumption = consumption

    def fuel_in_tank(self):
        if self.fuel > 100:
            raise Exception('fuel level cannot exceed level 100')
        return f'{self.fuel}L in the tank'

    def starting_car(self):
        self.fuel -= self.consumption
        if self.fuel == 0:
            return 'no fuel in the tank'
        else:
            return f'Сar started up. {self.fuel}L left in the tank'

    def drive_through(self, consumption):
        self.consumption = consumption
        if self.fuel != 0:
            self.fuel -= self.consumption
            return f'you drove {self.consumption} km and spend {self.consumption} fuel'
        else:
            raise Exception('Consumption cannot exceed fuel level')


class ElectricCar(Car):
    charge = 100

    def fuel_in_tank(self):
        if self.charge > 100:
            raise Exception('Charge level cannot exceed level 100')
        return f'{self.charge}% in the battery'

    def starting_car(self):
        self.charge -= self.consumption
        if self.charge == 0:
            return 'no charge in the battery'
        else:
            return f'car started up. {self.charge}% left in the battery'

    def drive_through(self, consumption):
        self.consumption = consumption
        if self.charge != 0:
            self.charge -= self.consumption
            return f'you drove {self.consumption} km and spend {self.consumption} charge'
        else:
            raise Exception('Consumption cannot exceed charge level')


@dataclass
class Engine(Car):
    name: str
    horsepower: int

    def __str__(self):
        return f'({self.__class__.__name__}) {self.name}, {self.horsepower} horsepower'


@dataclass()
class ElectricEngine(Engine):
    name: str
    horsepower: int
