class Car():
    def displacement(self):
        print("displacement with 4 wheels")


class Motocycle ():
    def displacement(self):
        print("displacement with 2 wheels")


class Truck ():
    def displacement(self):
        print("displacement with 6 wheels")


def vehicledisplacement(vehicle):
    vehicle.displacement()


mivehicle = Motocycle()

vehicledisplacement(mivehicle)
