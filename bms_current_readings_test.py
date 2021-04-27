import unittest
import math
import bms_current_readings_analyser as bms


class BMSCurrentReadingTest(unittest.TestCase):

    def test_checks_if_input_data_is_valid(self):
        valid_input = [4, 2, 1, 1, 2]
        invalid_inputs = [None, float(math.nan), 0]
        for invalid_input in invalid_inputs:
            self.assertEqual(bms.is_input_valid(invalid_input), False)
        self.assertEqual(bms.is_input_valid(valid_input), True)


if __name__ == '__main__':
    unittest.main()
