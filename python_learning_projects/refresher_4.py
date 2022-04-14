import refresher_3 as E
import unittest
class InputerTest(unittest.TestCase):
    """docstring for InputerTest."""

    def test(self):
        name = E.inputer()
        self.assertEqual(name, "Bassel")

unittest.main()
