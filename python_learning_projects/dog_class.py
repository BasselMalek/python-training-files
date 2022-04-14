class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " sat down!")
    def roll_over(self):
        print(self.name.title() + "rolled over!")
