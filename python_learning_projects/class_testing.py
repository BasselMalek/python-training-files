import unittest
from a_simple_class import Robot

class Testing_Robot(unittest.TestCase):

    def setUp(self):
        self.test_bot = Robot("EVO 17","TestBot","Red",0,0)

    def test_move(self):
        self.test_bot.move("X",40)
        self.assertEqual(self.test_bot.x_position, 40)

    def test_change_led_color(self):
        self.test_bot.change_led_color("blue")
        self.assertEqual(self.test_bot.led_color, "blue")

unittest.main()
