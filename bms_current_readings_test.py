import unittest
import math
import bms_current_readings_analyser as bms


class BMSCurrentReadingTest(unittest.TestCase):

    def test_checks_if_input_data_is_valid(self):
        valid_input = [4, 2, 1, 1, 2]
        invalid_inputs = [None, [1, 3, float(math.nan), 7, 9]]
        for invalid_input in invalid_inputs:
            self.assertEqual(bms.is_input_valid(invalid_input), False)
        self.assertEqual(bms.is_input_valid(valid_input), len(valid_input))


if __name__ == '__main__':
    unittest.main()
