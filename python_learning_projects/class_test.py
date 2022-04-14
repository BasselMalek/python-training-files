class Restaurant():
    """A Class For A Restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def descibe_restaurant(self):
        print(
            "This is " + self.restaurant_name.title() +
            ", the great restaurant known for it's great " +
            self.cuisine_type.title() + " food"
            )
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open")

input_1 = input("what's the restaurant's name ? ")
input_2 = input("what type of cuisine does the restaurant offer ? ")
my_restaurant =Restaurant(input_1,input_2)
my_restaurant.descibe_restaurant()
