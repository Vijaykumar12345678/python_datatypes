'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to reverse a tuple.
'''

def slice_tuple(input_tuple):
    """
    Description:
    This function will reverse a tuple.
    
    Parameters:
    input_tuple : tuple
        The tuple to be reversed.
    
    Returns:
    tuple: The sliced tuple.
    """
    return input_tuple[::-1]

def main():
    # Data
    sample_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90)
    
    
    sliced_tuple = slice_tuple(sample_tuple)
    print(f"The reversed tuple is{sliced_tuple}")

if __name__ == "__main__":
    main()
    