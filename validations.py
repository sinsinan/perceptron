def _validate_int_with_error(value: int, error_message="Expected value to be of type int"):
    if not isinstance(value, int):
        raise Exception(error_message)

def _is_greater_than_zero_with_error(value: int, error_message="Expected value to be greater than zero"):
    if not (value > 0):
        raise Exception(error_message)