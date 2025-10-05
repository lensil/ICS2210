"""

Main file for insert in data structures and collected the statistics.

"""

from knuth_shuffle import knuth_shuffle
from avl_tree import AVL_Tree
from red_black_tree import RB_Tree
from skip_list import Skip_List
import numpy as np
import math

# Creating an array of integers starting from 1 and ending at 50000
array_1 = np.arange(1, 5001)
array_1 = knuth_shuffle(array_1) # Shuffle the array using the Knuth shuffle algorithm

# Inserting the shuffled array into the AVL tree
avl_tree = AVL_Tree()
for key in array_1:
    avl_tree.insert(key)
avl_tree.statistics.reset() # Reset the statistics

# Inserting the shuffled array into the Red-Black tree
rb_tree = RB_Tree()
for key in array_1:
    rb_tree.insert(key)
rb_tree.statistics.reset() # Reset the statistics

# Inserting the shuffled array into the Skip List
skip_list = Skip_List(math.ceil(math.log2(6000)), 0.5)
for key in array_1:
    skip_list.insert(key)
skip_list.statistics.reset() # Reset the statistics

# Creating an array of 1000 random integers in the range of 0 to 100,000
array_2 = np.random.randint(0, 10001, 1000)

# Inserting the random array into the AVL tree
for key in array_2:
    avl_tree.insert(key)
avl_tree.statistics.set_height(avl_tree.root.height) # Set the height of the AVL tree
avl_tree.statistics.set_leaves(avl_tree.get_leaves(avl_tree.root)) # Set the number of leaves in the AVL tree
avl_statistics = avl_tree.statistics.calculate_statistics() # Calculate the statistics of the AVL tree

# Display the statistics of the AVL tree
print("AVL Tree Statistics:")
print("Height:", avl_statistics["height"])
print("Leaves:", avl_statistics["leaves"])
print("Steps:", avl_statistics["steps"])
print("Rotations:", avl_statistics["rotations"])

# Inserting the random array into the Red-Black tree
for key in array_2:
    rb_tree.insert(key)
rb_tree.statistics.set_height(rb_tree.get_height()) # Set the height of the Red-Black tree
rb_tree.statistics.set_leaves(rb_tree.get_leaves()) # Set the number of leaves in the Red-Black tree
rbt_statistics = rb_tree.statistics.calculate_statistics() # Calculate the statistics of the Red-Black tree

# Display the statistics of the Red-Black tree
print("\nRed-Black Tree Statistics:")
print("Height:", rbt_statistics["height"])
print("Leaves:", rbt_statistics["leaves"])
print("Steps:", rbt_statistics["steps"])
print("Rotations:", rbt_statistics["rotations"])

# Inserting the random array into the Skip List
for key in array_2:
    skip_list.insert(key)
skip_list.statistics.set_levels(skip_list.head.level) # Set the number of levels in the Skip List
skip_list_statistics = skip_list.statistics.calculate_statistics() # Calculate the statistics of the Skip List

# Display the statistics of the Skip List
print("\nSkip List Statistics:")
print("Levels:", skip_list_statistics["levels"])
print("Steps:", skip_list_statistics["steps"])
print("Promotions:", skip_list_statistics["promotions"])