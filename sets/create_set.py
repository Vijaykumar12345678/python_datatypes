'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to create and display a set.
'''

def create_and_display_set(elements):
    """
    Description:
    This function creates a set from a list of elements and displays it.
    
    Parameters:
    elements : list The list of elements to be converted into a set.
    
    Returns:
    set: The created set.
    """
    created_set = set(elements)
    return created_set

def main():
    # Sample list of elements
    elements = [1, 2, 3, 4, 4, 5, 6, 7, 1, 2, 5]
    created_set = create_and_display_set(elements)
    print("Original list:", elements)
    print("Created set:", created_set)

if __name__ == "__main__":
    main()
