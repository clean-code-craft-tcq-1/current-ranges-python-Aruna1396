import numpy as np


def is_NaN_in_input(input_readings):
    input_sum = np.sum(input_readings)
    if np.isnan(input_sum):
        return True
    else:
        return False


def is_input_valid(input_readings):
    if input_readings is not None and is_NaN_in_input(input_readings) is False:
        return 'VALID_INPUT'
    else:
        return 'INVALID_INPUT'
