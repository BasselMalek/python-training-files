import unittest
import name_formatter as NF
class TestCaseNF(unittest.TestCase):
    """docstring for TestCaseNF."""

    def test_1(self):
        """Testing first and last names in this function."""
        formatted_name = NF.name_formatter("bassel","walid")
        self.assertEqual(formatted_name, "Bassel Walid")
    def test_2(self):
        """Testing middle names."""
        formatted_name = NF.name_formatter("wolfgang","mozart","amadeus")
        self.assertEqual(formatted_name,"Wolfgang Amadeus Mozart")
unittest.main()
