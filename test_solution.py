import unittest
from Solution import check_filename

class SolutionTestCase(unittest.TestCase):
    """Tests for `Solution.py`."""

    def test_is_check_filename(self):
        """ Is file has a correct extension '.csv' ? """
        self.assertTrue(check_filename('sample.csv'))

    def test_is_check_filename_False(self):
        """ Is file has a correct extension '.csv' ? """
        self.assertFalse(check_filename('sample.txt'))
        
if __name__ == '__main__':
    unittest.main()
