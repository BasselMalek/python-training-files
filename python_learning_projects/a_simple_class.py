class Robot():

    def __init__(self,model,name,led_color,x_position,y_position):
        self.model = model
        self.name = name
        self.led_color = led_color
        self.x_position = x_position
        self.y_position = y_position


    def move(self,direction,distance):
        if (direction == "X"):
            self.x_position = self.x_position + distance
        elif (direction == "Y"):
            self.y_position = self.y_position + distance
        print(
            self.name + " has moved " + str(distance) + " units in the " +
             direction + " direction."
             )

    def change_led_color(self,new_color):
        if (new_color == "black"):
            print("You can't set an LED to black.")
        else:
            self.led_color = new_color
