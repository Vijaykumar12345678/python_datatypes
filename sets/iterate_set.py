'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to create and iterate a set.
'''

def create_and_iterate_set(elements):
    """
    Description:
    This function creates a set from a list of elements and displays it.
    
    Parameters:
    elements : list The list of elements to be converted into a set.
    
    Returns:
    set: The created set.
    """
    for element in elements:
        print(element)

def main():
    # Sample list of elements
    elements = {1, 2, 3, 4, 4, 5, 6, 7, 1, 2, 5}
    create_and_iterate_set(elements)
   
if __name__ == "__main__":
    main()
