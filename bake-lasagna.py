EXPECTED_BAKE_TIME = 40
"""This constant returns indicates the indicated cooking time."""

def bake_time_remaining(elapsed_bake_time):
    """Calculates the cooking time remaining.

    :param elapsed_bake_time: int - the elapsed bake time.
    :return: int - total remaining time.

    This function takes two integers representing expected bake time and the
    elapsed bake time and calculates the remaining bake time.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time    
bake_time_remaining(30)


time_in_minutes = 2
def preparation_time_in_minutes(number_of_layers):
    """Calculates the preparation time in minutes for each lasagna layer.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int * total time preparation of each layer of lasagna.

    This function takes two integers representing the number of lasagna layers and the time in minutes of prep each layer and calculates the total time preparation of layers (in minutes).
    """
    return time_in_minutes * number_of_layers
preparation_time_in_minutes(2)


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculates the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return (time_in_minutes * number_of_layers) + elapsed_bake_time
