import unittest
import math
import bms_current_readings_analyser as bms


class BMSCurrentReadingTest(unittest.TestCase):

    def test_if_input_data_check_yields_valid_or_invalid(self):
        valid_input = [4, 2, 1, 1, 2]
        invalid_inputs = [None, [1, 3, float(math.nan), 7, 9]]
        for invalid_input in invalid_inputs:
            self.assertEqual((bms.is_input_valid(invalid_input)), 'INVALID_INPUT')
        self.assertEqual((bms.is_input_valid(valid_input)), 'VALID_INPUT')

## Failing Test

    def test_yields_ranges_for_input_current_readings(self):
        current_readings = [3, 3, 5, 4, 10, 11, 12]
        expected_ranges = [{3: 5}, {10: 12}]
        self.assertEqual((bms.find_ranges_in_current_readings(current_readings)), expected_ranges)


if __name__ == '__main__':
    unittest.main()
