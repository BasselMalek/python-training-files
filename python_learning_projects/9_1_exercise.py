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
my_restaurant = Restaurant("papa smith's","trash")
print(my_restaurant.restaurant_name.title())
print(my_restaurant.cuisine_type.title())
my_restaurant.descibe_restaurant()
my_restaurant.open_restaurant()
