class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f'brand : {self.brand}, model : {self.model}')

class electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def display_battery(self):
        print(f'battery capacity : {self.battery_capacity} kwh')

class electricCar(vehicle, electric):
    def __init__(self, brand, model, battery_capacity, range_per_charge):
        vehicle.__init__(self, brand, model)
        electric.__init__(self, battery_capacity)
        self.range_per_charge = range_per_charge

    def info(self):
        vehicle.info(self)
        print(f'range per charge : {self.range_per_charge} km')

jesko = electricCar('jesko', 'model 2', 1600, 531)
jesko.info()
jesko.display_battery()