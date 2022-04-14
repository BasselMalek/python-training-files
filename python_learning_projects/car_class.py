class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def odometer_reader(self):
        print("this car has " + str(self.odometer_reading) + " kilometers on it")
    def odometer_updater(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back a odometer")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
print(my_new_car.odometer_reader())
my_new_car.odometer_reading = 100
print(my_new_car.odometer_reader())
