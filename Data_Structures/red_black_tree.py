import ds_statistics as ds_stats
import unittest

# Implementation of a Red-Black Tree

# Node for Red-Black Tree
class RB_Node:
    def __init__(self, key, color): # Constructor
        self.key = key # Key of the node
        self.left = Nil # Left child
        self.right = Nil # Right child
        self.parent = Nil # Parent of the node
        self.color = color # Color of the node

# Leaf (NIL) node for Red-Black Tree
class NIL_Node:
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.parent = None
        self.color = "Black"

# Global NIL node
Nil = NIL_Node()

# Red-Black Tree
class RB_Tree:
    def __init__(self):
        self.root = Nil 
        self.statistics = ds_stats.Statistics() # Keeps track of the statistics

    # Insert
    def insert(self, key):

        """

        Function to insert a key into the Red-Black Tree.

        Parameters:
            key (int): The key to be inserted.

        """

        steps = 0  # Initialise steps

        # Create a new node and default color it to red
        new_node = RB_Node(key, "Red")

        parent_node = Nil # Keep track of the parent node when inserting
        current_node = self.root # Start searching at the root 

        # Search for the correct position to insert the new node
        while current_node != Nil: # While a nil node is not reached
            steps += 1 # Increment the number of steps
            parent_node = current_node # Update the parent node
            if new_node.key < current_node.key: # If the new node's key is less than the current node's key
                current_node = current_node.left # Move to the left
            else:
                current_node = current_node.right # Move to the right

        # Set the parent of the new node
        new_node.parent = parent_node

        if parent_node == Nil: # If the tree is empty
            self.root = new_node # Set the new node as the root
        elif new_node.key > parent_node.key: # If the new node's key is greater than the parent node's key
            parent_node.right = new_node # Set the new node as the right child
        else:
            parent_node.left = new_node # Set the new node as the left child

        self.fix_insert(new_node) # Fix the tree after insertion

        self.statistics.add_step(steps)


    # Fixing the Red-Black Tree after insertion     
    def fix_insert(self, node):

        """

        Function to fix the Red-Black Tree after insertion.

        Parameters:
            node (RB_Node): The node to start fixing the tree from.

        """

        rotations = 0 # Initialise the number of rotations

        while node.parent.color == "Red" and node != self.root:  # While the parent of the node is red and the node is not the root
            if node.parent == node.parent.parent.left:  # If the parent of the node is a left child
                uncle = node.parent.parent.right  # Get the right uncle of the node
            else: 
                uncle = node.parent.parent.left  # Get the left uncle of the node

            if uncle.color == "Red":  # If the uncle of the node is red
                self.fix_red_uncle(node, uncle)  # Fix the tree
                node = node.parent.parent # Move up the tree
            else: 
                self.fix_black_uncle(node) # Fix the tree
                rotations += 1 # Increment the number of rotations

        self.statistics.add_rotation(rotations) # Add the number of rotations
        self.root.color = "Black"  # Set the root to black


       # Fixing the tree when the uncle of a node is red
    def fix_red_uncle(self, node, uncle):
                
        """
    
        Function to fix the tree when the uncle of a node is red.
    
        Parameters:
            node (RB_Node): The node to fix the tree from.
            uncle (RB_Node): The uncle of the node.
    
        """
    
        node.parent.color = "Black" # Set the parent to black
        uncle.color = "Black" # Set the uncle to black
        node.parent.parent.color = "Red" # Set the grandparent to red

    # Fixing the tree when the uncle of a node is black
    def fix_black_uncle(self, node):
                    
        """

        Function to fix the tree when the uncle of a node is black.

        Parameters:
            node (RB_Node): The node to fix the tree from.

        """

        if node.parent == node.parent.parent.left: # If the parent of the node is a left child
            if node == node.parent.right: # If the node is a right child
                node = node.parent # Move up the tree
                self.left_rotation(node) # Perform a left rotation
            node.parent.color = "Black" # Set the parent to black
            node.parent.parent.color = "Red"  # Set the grandparent to red
            self.right_rotation(node.parent.parent) # Perform a right rotation
        else: 
            if node == node.parent.left: # If the node is a left child
                node = node.parent # Move up the tree
                self.right_rotation(node) # Perform a right rotation
            node.parent.color = "Black" # Set the parent to black
            node.parent.parent.color = "Red" # Set the grandparent to red
            self.left_rotation(node.parent.parent) # Perform a left rotation


    # Rotations
    def left_rotation(self, node):
           
        """
    
        Function to perform a left rotation on a node.
    
        Parameters:
            node (RB_Node): The node to be rotated.
    
        """

        new_root = node.right # The right child becomes the new root of the subtree
        node.right = new_root.left # The left child of the new root becomes the right child of the node

        if new_root.left != Nil: # If the left child of the new root is not nil
            new_root.left.parent = node # Set the parent of the left child of the new root to the node

        new_root.parent = node.parent # Set the parent of the new root to the parent of the node

        if node.parent == Nil: # If the parent of the node is nil
            self.root = new_root # Set the new root as the root of the tree
        elif node == node.parent.left: # If the node is a left child
            node.parent.left = new_root # Set the new root as the left child of the parent
        else: # If the node is a right child
            node.parent.right = new_root # Set the new root as the right child of the parent

        new_root.left = node # The previous root becomes the left child of the new root
        node.parent = new_root # Set the parent of the node to the new root

    def right_rotation(self, node):

        """
    
        Function to perform a right rotation on a node.
    
        Parameters:
            node (RB_Node): The node to be rotated.

        """

        new_root = node.left # The left child becomes the new root of the subtree
        node.left = new_root.right # The right child of the new root becomes the left child of the node

        if new_root.right != Nil: # If the right child of the new root is not nil
            new_root.right.parent = node # Set the parent of the right child of the new root to the node

        new_root.parent = node.parent # Set the parent of the new root to the parent of the node

        if node.parent == Nil: # If the parent of the node is nil
            self.root = new_root # Set the new root as the root of the tree
        elif node == node.parent.right: # If the node is a right child
            node.parent.right = new_root
        else: # If the node is a left child
            node.parent.left = new_root # Set the new root as the left child of the parent

        new_root.right = node # The previous root becomes the right child of the new root
        node.parent = new_root # Set the parent of the node to the new root

    # Utility functions
        
    # Get the height of the tree
    def get_height(self):
            
        """
    
        Function to get the height of the tree.
    
        Returns:
            int: The height of the tree.
    
        """
    
        return self.get_height_recursive(self.root) # Get the height recursively
    
    def get_height_recursive(self, node):

        """
    
        Function to get the height of the tree recursively.
    
        Parameters:
            node (RB_Node): The node to get the height from.
    
        Returns:
            int: The height of the tree.
    
        """
    
        # Base case
        if node == Nil: # If the node is nil,
            return 0 # Return 0
        elif node.left == Nil and node.right == Nil: # If the node is a leaf,
            return 0
        # Recursive case
        else: # Otherwise,
            left_height = self.get_height_recursive(node.left) # Get the height of the left subtree
            right_height = self.get_height_recursive(node.right) # Get the height of the right subtree
            return max(left_height, right_height) + 1 # Return the maximum height of the subtrees plus 1
        
    # Get the number of leaves in the tree
    def get_leaves(self):
            
        """
    
        Function to get the number of leaves in the tree.
    
        Returns:
            int: The number of leaves in the tree.
    
        """
    
        return self.get_leaves_recursive(self.root) # Get the number of leaves recursively
    
    def get_leaves_recursive(self, node):

        """
    
        Function to get the number of leaves in the tree recursively.
    
        Parameters:
            node (RB_Node): The node to get the number of leaves from.
    
        Returns:
            int: The number of leaves in the tree.
    
        """
    
        # Base case
        if node == Nil: # If the node is nil,
            return 0 # Return 0
        elif node.left == Nil and node.right == Nil: # If the node is a leaf,
            return 1 # Return 1
        
        # Recursive case
        else:
            return self.get_leaves_recursive(node.left) + self.get_leaves_recursive(node.right) # Return the sum of the leaves in the left and right subtrees