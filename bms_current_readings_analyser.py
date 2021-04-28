import numpy as np


def check_NaN_in_input(input_readings):
    input_sum = np.sum(input_readings)
    if np.isnan(input_sum):
        return True
    else:
        return False


def is_input_valid(input_readings):
    if input_readings is not None and check_NaN_in_input(input_readings) is False:
        return len(input_readings)
    else:
        return False
