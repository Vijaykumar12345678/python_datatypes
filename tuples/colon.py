
'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to create colon of  a tuple.
'''

def main():
    """
    Description:
    This main function demonstrates the use of deepcopy with tuples containing mutable elements.
    It creates a tuple, makes a deep copy of it, modifies the copy, and prints both the original and the modified tuples.
    """
    tuplex = ("HELLO", 5, [], True)
    
    print("Original Tuple:", tuplex)
    
    
    tuplex[2].append(50)
    
    print("Modified  Copy Tuple:", tuplex)
    
    print("Original Tuple after modification of the copy:", tuplex)

if __name__ == "__main__":
    main()
