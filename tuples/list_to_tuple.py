'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to convert a list to a tuple.
'''

def list_to_tuple(input_list):
    """
    Description:
    This function converts a list to a tuple.
    
    Parameters:
    input_list : list
        The list to be converted to a tuple.
    
    Returns:
    tuple: The converted tuple.
    """
    return tuple(input_list)

def main():
    # Data
    sample_list = [10, 20, 30, 40, 50]
    result_tuple = list_to_tuple(sample_list)
    print("Original List:", sample_list)
    print("Converted Tuple:", result_tuple)

if __name__ == "__main__":
    main()
