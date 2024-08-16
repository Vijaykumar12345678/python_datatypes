'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to check whether an element exists within a tuple.
'''

def check_element_in_tuple(input_tuple, element):
    """
    Description:
    This function checks if a given element exists within a tuple.
    
    Parameters:
    input_tuple : tuple
        The tuple to search within.
    element : any
        The element to search for.
    
    Returns:
    bool: True if the element exists in the tuple, False otherwise.
    """
    return element in input_tuple

def main():
    # Data
    sample_tuple = (10, 20, 30, 40, 50)
    element_to_check = 30
    exists = check_element_in_tuple(sample_tuple, element_to_check)
    if exists:
        print(f"Element {element_to_check} exists in the tuple.")
    else:
        print(f"Element {element_to_check} does not exist in the tuple.")

if __name__ == "__main__":
    main()
