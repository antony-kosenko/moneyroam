
def clear_none_values(parameters: dict) -> dict:
    """ Takes Dict as parameter and returns the same type of iterable filtering out None values. """
    # removing keys with values equal to 'None'
    not_none_variables_list = {key: value for key, value in parameters.items() if value is not None}
    return not_none_variables_list
