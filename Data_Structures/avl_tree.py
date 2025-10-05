import ds_statistics as ds_stats
import numpy as np
# Implementation of an AVL Tree

# Node for AVL Tree
class AVL_Node:
    def __init__(self, key): # Constructor
        self.key = key # Key of the node
        self.left = None # Left child
        self.right = None # Right child
        self.height = 1 # Height of the node

# AVL Tree
class AVL_Tree:
    def __init__(self):
        self.root = None
        self.statistics = ds_stats.Statistics()  # Keeps track of the statistics
        self.rotations = 0

    # Function to insert a key into the AVL Tree 
    def insert(self, key):

        """

        Function to insert a key into the AVL Tree.

        Parameters:
            key (int): The key to be inserted.
    
        """

        if self.root is None: # If the tree is empty, create a new node and add the key
            self.root = AVL_Node(key)
            self.statistics.add_step(1) # Add the number of steps
            self.statistics.add_rotation(0) # Add the number of rotations
        else: # If the tree is not empty, call the recursive function to insert the key
            steps = 0 # Initialise the number of steps
            rotations = 0 # Initialise the number of rotations
            self.root, rotations = self.insert_recursive(self.root, key, steps, rotations) 

    def insert_recursive(self, node, key, steps, rotations):

        """

        Recursive function to insert a key into the AVL Tree.

        Parameters:
            node (AVL_Node): The current node being considered.
            key (int): The key to be inserted.
            steps (int): The number of steps taken to reach the current node.
            rotations (int): The number of rotations performed.

        Returns:
            AVL_Node: The new root of the subtree.
            rotations (int): The number of rotations performed.

        """
        
        # Base case
        if node is None: # If the positicccon of the key is found 
            self.statistics.add_step(steps) # Add the number of steps
            self.statistics.add_rotation(self.rotations) # Add the number of rotations
            self.rotations = 0 # Reset the number of rotations
            return AVL_Node(key), rotations # Create a new node with the key
        
        steps += 1 # Increment the number of steps

        if key < node.key: # If the key is less than the current node's key
            node.left, rotations_left = self.insert_recursive(node.left, key, steps, rotations) # Insert it into the left subtree recursively
            rotations += rotations_left
        else: # If the key is greater than the current node's key
            node.right, rotations_right = self.insert_recursive(node.right, key, steps, rotations) # Insert it into the right subtree recursively
            rotations += rotations_right

        # Update the height of the current node
        self.update_height(node)

        # Get the balance factor of the current node
        balance = self.balance_factor(node)

         # Perform rotations if necessary
        if balance > 1: # If the tree is left heavy
            if key < node.left.key: # If the key is less than the key of the left child
                self.rotations += 1 # Increment the number of rotations
                node = self.right_rotation(node) # Perform a right rotation
            elif key > node.left.key: # If the key is greater than the key of the left child
                self.rotations += 1 # Increment the number of rotations
                node = self.left_right_rotation(node) # Perform a left-right rotation
        elif balance < -1: # If the tree is right heavy
            if key > node.right.key: # If the key is greater than the key of the right child
                self.rotations += 1 # Increment the number of rotations
                node =  self.left_rotation(node) # Perform a left rotation
            elif key < node.right.key: # If the key is less than the key of the right child
                self.rotations += 1 # Increment the number of rotations
                node = self.right_left_rotation(node) # Perform a right-left rotation
        return node, rotations # Return the current node and the number of rotations

    # Rotations
    def left_rotation(self, node):
            
        """
    
        Function to perform a left rotation on a node.
    
        Parameters:
            node (AVL_Node): The node to be rotated.
    
        Returns:
            AVL_Node: The new root of the subtree.
    
        """

        new_root = node.right 
        left_node = new_root.left

        new_root.left = node
        node.right = left_node

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))

        return new_root
    
    def right_rotation(self, node):
                
        """
        
        Function to perform a right rotation on a node.
        
        Parameters:
            node (AVL_Node): The node to be rotated.
        
        Returns:
            AVL_Node: The new root of the subtree.
        
        """

        new_root = node.left
        right_node = new_root.right

        new_root.right = node
        node.left = right_node

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))

        return new_root
    
    def left_right_rotation(self, node):

        """

        Function to perform a left-right rotation on a node.

        Parameters:
            node (AVL_Node): The node to be rotated.

        Returns:
            AVL_Node: The new root of the subtree.
        
        """

        # Perform the rotation
        node.left = self.left_rotation(node.left) # Perform a left rotation on the left child
        
        return self.right_rotation(node) # Perform a right rotation on the node

    def right_left_rotation(self, node):

        """

        Function to perform a right-left rotation on a node.

        Parameters:
            node (AVL_Node): The node to be rotated.

        Returns:
            AVL_Node: The new root of the subtree.

        """

        # Perform the rotation
        node.right = self.right_rotation(node.right) # Perform a right rotation on the right child
        
        return self.left_rotation(node) # Perform a left rotation on the node
    
    # Utility functions

    def height(self, node):
        
        """

        Function to get the height of a node.

        Parameters:
            node (AVL_Node): The node whose height is to be found.

        Returns:
            int: The height of the node.
    
        """
        
        if node is None: # If the node is none, the height is 0
            return 0
        
        return node.height # Return the height of the node

    def balance_factor(self, node):

        """
    
        Function to get the height of a node.

        Parameters:
            node (AVL_Node): The node whose height is to be found.

        Returns:
            int: The balance factor of the node.
    
        """
        
        if node is None: # If the node is none, the balance factor is 0
            return 0
        # Return the balance factor of the node
        return self.height(node.left) - self.height(node.right) # Calculate the difference between the height of the left and right subtrees
    
    def update_height(self, node):
            
        """
    
        Function to update the height of a node.
    
        Parameters:
            node (AVL_Node): The node whose height is to be updated.
    
        """
            
        # Update the height of the node
        node.height = 1 + max(self.height(node.left), self.height(node.right)) # The height of the node is 1 plus the maximum height of the left and right subtrees

    def get_leaves(self, node):

        """

        Function to get the number of leaves in the tree.

        Parameters:
            node (AVL_Node): The node to be considered.

        Returns:
            int: The number of leaves in the tree.

        """

        # Base case 1: If the node is None
        if node is None: # If the node is none
            return 0 # There are no leaves, therefore return 0
        
        # Base case 2: If the node is a leaf
        if node.left is None and node.right is None: # If the node is a leaf
            return 1 # Return 1
        
        # Recursively calculate the number of leaves in the left and right subtrees
        return self.get_leaves(node.left) + self.get_leaves(node.right) 