"""

    Contains the implementation of the Knuth shuffle algorithm to randomise the order of elements in an array.

"""

import random

# Implements the Knuth shuffle algorithm
def knuth_shuffle(array):

    """

    Implements the Knuth shuffle algorithm to randomise the order of elements in an array.
    
    Parameters:
        array (list): An array of integeres to be shuffled.

    Returns:
        array (list): The shuffled array.

    """

    # Iterate through the array in reverse order
    for i in range(len(array)-1, 0, -1):
        random_index = random.randint(0, i) # Generate a random index between 0 and i
        array[i], array[random_index] = array[random_index], array[i] # Swap the element at the current index with the random element

    return array