from veh import vehicle

car = vehicle.Car(name='Audi', color='red', sound='beep', wheels=4, consumption=10)
engine = vehicle.Engine('V8', 476)
electric_car = vehicle.ElectricCar(name='Tesla', color='black', sound='beep', wheels=4, consumption=15)
electric_engine = vehicle.ElectricEngine('Model S', 362)


if __name__ == '__main__':
    print(car)
    print(engine)
    print(vars(car))
    print(car.fuel_in_tank())
    print(car.starting_car())
    print(car.drive_through(10))
    print(car.fuel_in_tank())
    print()
    print(electric_car)
    print(electric_engine)
    print(vars(electric_car))
    print(electric_car.fuel_in_tank())
    print(electric_car.starting_car())
    print(electric_car.drive_through(15))
    print(electric_car.fuel_in_tank())
