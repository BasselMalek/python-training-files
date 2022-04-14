import refresher_1 as M
import unittest
class JumpTestCase(unittest.TestCase):
    """Test for the 'Jump' function"""

    def test_1(self):
        height = M.jump(1,"M")
        self.assertEqual(height, 1)
unittest.main()
