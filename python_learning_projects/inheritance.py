class Computer():
    """
    A Class that represents a Computer
    """
    def __init__(self,making,cpu,gpu,ram_type,ram_capacity,storage_type,storage_capacity):
        self.making = making
        self.cpu = cpu
        self.gpu = gpu
        self.ram_type = ram_type
        self.ram_capacity = ram_capacity
        self.storage_type = storage_type
        self.storage_capacity = storage_capacity
    def check_on_building_status(self):
        if (self.making == "custom-built"):
            self.maker = "none"
        elif (self.making == "pre-built"):
            maker = input("What's the PC builder did you use to build your PC ? ")
            self.maker = maker
    def describe_pc(self):
        if (self.maker == "none"):
            print("This is my custom-built pc with " + self.cpu + " powering it" +
                " with a " + self.gpu + " as it's gpu and it has " + str(self.ram_capacity)
                + "gigs of " + self.ram_type + " RAM with " + str(self.storage_capacity)
                + "TB of " + self.storage_type + " storage")
        else:
            print("This is my " + self.maker + " pc with " + self.cpu + " powering it" +
                " with a " + self.gpu + " as it's gpu and it has " + str(self.ram_capacity)
                + "gigs of " + self.ram_type + " RAM with " + str(self.storage_capacity)
                + "TB of " + self.storage_type + " storage")
my_computer = Computer("custom-built","I9-9900K","RTX 2080","DDR4",32,"SSD",1)
my_computer.check_on_building_status()
my_computer.describe_pc()
class Laptop(Computer):
    def __init__(self,cpu,gpu,ram_type,ram_capacity,storage_type,storage_capacity,battery):
        super().__init__(self,cpu,gpu,ram_type,ram_capacity,storage_type,storage_capacity)
        self.battery = battery
    def describe_laptop(self):
        print("This is my laptop with " + self.cpu + " powering it" +
            " with a " + self.gpu + " as it's gpu and it has " + str(self.ram_capacity)
            + "gigs of " + self.ram_type + " RAM with " + str(self.storage_capacity)
            + "TB of " + self.storage_type + " storage")
my_laptop = Laptop("I5-5200U","AMD R9 375","DDR3",8,"HDD",1,20000)
my_laptop.describe_laptop()
print(my_laptop.battery)
