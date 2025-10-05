# Implementation of a Skip List
import random
import ds_statistics as ds_stats

class Skip_Node:
    # Node for Skip List
    def __init__(self, key, level): # Constructor
        self.key = key # Key of the node
        self.level = level # Level of the node
        self.forward = [None] * (level + 1) # Forward pointers for the node

class Skip_List:
    # Skip List class
    def __init__(self, max_level, probability):
        self.max_level = max_level # Maximum level of the Skip List
        self.probability = probability # Probability of a node having a higher level
        self.level = 0 # Current level of the Skip List
        self.head = Skip_Node(None, self.max_level) # Head node of the Skip List
        self.statistics = ds_stats.Statistics() # Keeps track of the statistics

    # Insertion
    def insert(self, key):

        """

        Function to insert a key-value pair into the Skip List.

        Parameters:
            key (int): The key to be inserted.

        """

        steps = 1 # Initialise the number of steps
        promotions = 0 # Initialise the number of promotions

         # Create an array to hold pointers to the nodes that need to be updated at each level
        update = [None] * (self.max_level + 1)
        current = self.head
    
        # Start from the highest level of the Skip List and move downwards
        for i in range(self.level, -1, -1):
            # Move forward while the next node's key is less than the key to be inserted
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
                steps += 1
            update[i] = current  # Remember the node at this level
    
        # Move to the level 0 node before the position where the new node will be inserted
        current = current.forward[0]

    
        # If the current node is the end of the list or its key is not equal to the key to be inserted,
        # then we can proceed with the insertion
        if current is None or current.key != key: 
            # Determine the level for the new node and the number of promotions
            new_level, promotions = self.random_level()

        
            # If the new node's level is greater than the current level of the list,
            # Update the list level and the update array with the head node
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1): 
                    update[i] = self.head
                self.level = new_level
        
            # Create the new node
            new_node = Skip_Node(key, new_level)
        
            # Insert the new node and update the forward pointers
            for i in range(new_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

        # Update the statistics
        self.statistics.add_step(steps)
        self.statistics.add_promotion(promotions)
        
    # Utility functions
    def random_level(self):

        """

        Function to generate a random level for a node.

        Returns:
            int: Random level for the node.
        
        """

        level = 0 # Count the level of the node
        promotions = 0 # Count the number of promotions
        while random.random() < self.probability and level < self.max_level:
            level += 1
            promotions += 1
        return level, promotions