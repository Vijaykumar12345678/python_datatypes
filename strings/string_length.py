'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to calculate the length of a string.
'''

def calculate_string_length(input_string):
    """
    Description:
    This function calculates and returns the length of a given string.
    
    Parameters:
    input_string : str
        The string whose length is to be calculated.
    
    Returns:
    int: The length of the string.
    """
    return len(input_string)

def main():
    # Data
    sample_string = "Hello, World!"
    string_length = calculate_string_length(sample_string)
    print(f"The length of the string '{sample_string}' is: {string_length}")

if __name__ == "__main__":
    main()
