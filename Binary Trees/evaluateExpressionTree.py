# This is an input class. Do not edit.  
class BinaryTree:  
    """  
    Represents a node in a binary tree.  

    Attributes:  
        value (int or float): The value stored in the node, which could represent  
            either a number or an operator (for expression trees).  
        left (BinaryTree, optional): The left child node. Defaults to None.  
        right (BinaryTree, optional): The right child node. Defaults to None.  

    Methods:  
        __init__(value, left=None, right=None): Initializes a new instance of  
            the BinaryTree class.  
    """  

    def __init__(self, value, left=None, right=None):  
        """  
        Initializes a new BinaryTree node with a specified value, and optional  
        left and right children.  

        Parameters:  
            value (int or float): The value or operator that this node represents.  
            left (BinaryTree, optional): The left child of this node, another  
                BinaryTree instance. Defaults to None.  
            right (BinaryTree, optional): The right child of this node, another  
                BinaryTree instance. Defaults to None.  
        """  
        self.value = value  
        self.left = left  
        self.right = right  


def evaluateExpressionTree(tree):  
    """  
    Evaluates a binary expression tree.  

    A binary expression tree is a binary tree where each leaf node represents  
    a numerical operand and each internal node represents an operator. The  
    operators are represented by specific integer values as follows:  
    - -1: Addition  
    - -2: Subtraction  
    - -3: Division  
    - Any other integer: Multiplication  

    This function recursively evaluates the expression represented by the  
    binary tree and returns the computed result.  

    Parameters:  
        tree (BinaryTree): The root node of the binary expression tree to be  
        evaluated.  

    Returns:  
        int or float: The result of evaluating the expression tree.  

    Raises:  
        ZeroDivisionError: If a division by zero is encountered during the  
        evaluation process.  
    """  
    if tree.left is None and tree.right is None:  
        return tree.value  
    left_val = evaluateExpressionTree(tree.left)  
    right_val = evaluateExpressionTree(tree.right)  
    if tree.value == -1:  
        return left_val + right_val  
    elif tree.value == -2:  
        return left_val - right_val  
    elif tree.value == -3:  
        if right_val == 0:  
            raise ZeroDivisionError("Division by zero encountered in expression tree.")  
        return int(left_val / right_val)  
    else:  
        return left_val * right_val