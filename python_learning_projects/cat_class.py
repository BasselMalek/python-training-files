class Cat():
    """A class that represents a cat"""

    def __init__(self,color,age,gender,name):
        self.color = color
        self.age = age
        self.gender = gender
        self.name = name
    def roll(self):
        print(self.name.title() + " just rolled !!")
    def introduction(self):
        """Shows all the info about the cat in an introductionary manner"""
        if (self.gender == "male"):
            print(
                "This is my cat " + self.name.title() + ", He has " + self.color
                + " hair and he's " + self.age + " old."
                )
        elif (self.gender == "female"):
            print(
                "This is my cat " + self.name.title() + ", She has" + self.color
                + "hair and she's " + self.age + " old."
                )
my_cat = Cat("white","2 yrs","male","hazulnut")
my_cat.roll()
my_cat.introduction()
