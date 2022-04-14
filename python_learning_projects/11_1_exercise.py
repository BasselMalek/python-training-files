import unittest
import city_functions as CF
class TestCities(unittest.TestCase):
    def test_1(self):
        formatted_city = CF.country_maker("Newyork","USA")
        self.assertEqual(formatted_city,"Newyork,Usa")
unittest.main()
