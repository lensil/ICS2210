import numpy as np

# Calcaulates statistics for AVL trees, RBT and Skip lists
class Statistics:
    def __init__(self):
        # Data dictionary to store the statistics
        self.data = {
            "steps": [], # Number of steps for insertion
            "rotations": [], # Number of rotations for insertion (AVL Trees and RBT)
            "height": None, # Height of the tree (AVL Trees and RBT)
            "leaves": None, # Number of leaves in the tree (AVL Trees and RBT)
            "promotions": [], # Number of promotions for insertion (Skip Lists)
            "levels": None, # Number of levels in the Skip List
        }

    # Calculate the statistics  
    def calc_stats(self, data):

        """
        
        Helper function to calculate the statistics for a given list of data.

        Parameters:
            data (list): The list of data for which statistics are to be calculated.
        
        """

        if data:  # Checks if the list is not empty
            return { # If the list is not empty
                "min": np.min(data), # Calculate the minimum value
                "max": np.max(data), # Calculate the maximum value
                "avg": np.mean(data), # Calculate the average value
                "median": np.median(data), # Calculate the median value
                "std": np.std(data, ddof=1)  # Calculate the standard deviation
            }
        else: # If the list is empty
            return { # Return None as a default value
                "min": None,
                "max": None,
                "avg": None,
                "median": None,
                "std": None
            }

    def calculate_statistics(self):

        """

        Function to calculate the statistics for the data collected.

        Returns:
            dict: The statistics calculated.

        """
        stats = {}  # Dictionary to store the statistics
    
        stats["steps"] = self.calc_stats(self.data["steps"]) # Calculate the statistics for the number of steps
        stats["rotations"] = self.calc_stats(self.data["rotations"]) # Calculate the statistics for the number of rotations
        stats["promotions"] = self.calc_stats(self.data["promotions"]) # Calculate the statistics for the number of promotions

        stats["height"] = self.data["height"] # Get the height of the tree
        stats["leaves"] = self.data["leaves"] # Get the number of leaves in the tree
        stats["levels"] = self.data["levels"] # Get the number of levels in the Skip List

        return stats
    
    # Utility functions
        
    # Add the number of steps
    def add_step(self, step):

        """

        Function to add the number of steps to the statistics.

        Parameters:
            step (int): The number of steps to be added.
        
        """

        self.data["steps"].append(step) # Append the number of steps to the list

    # Add the number of rotations
    def add_rotation(self, rotation):
        """

        Function to add the number of rotations to the statistics.

        Parameters:
            rotation (int): The number of rotations to be added.

        """

        self.data["rotations"].append(rotation) # Add one rotation

    # Set the height of the tree
    def set_height(self, height):

        """

        Function to set the height of the tree in the statistics.

        Parameters:
            height (int): The height of the tree.

        """

        self.data["height"] = height # Set the height

    # Set the number of leaves
    def set_leaves(self, leaves):

        """

        Function to set the number of leaves in the tree in the statistics.

        Parameters:
            leaves (int): The number of leaves in the tree.

        """

        self.data["leaves"] = leaves # Set the number of leaves

    # Add the number of promotions
    def add_promotion(self, promotion):

        """

        Function to add the number of promotions to the statistics.

        Parameters:
            promotion (int): The number of promotions to be added.

        """

        self.data["promotions"].append(promotion) # Add one promotion

    # Set the number of levels
    def set_levels(self, levels):

        """

        Function to set the number of levels in the Skip List in the statistics.

        Parameters:
            levels (int): The number of levels in the Skip List.

        """

        self.data["levels"] = levels # Set the number of levels

    # Reset the statistics
    def reset(self):

        """

        Function to reset the statistics.

        """

        self.data = {
            "steps": [],
            "rotations": [],
            "height": None,
            "leaves": None,
            "promotions": [],
            "levels": None,
        }