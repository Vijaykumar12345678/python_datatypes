'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to add 'ing' or 'ly' to a string based on certain conditions.
'''

def add_suffix(input_string):
    """
    Description:
    This function adds 'ing' at the end of the given string if its length is at least 3.
    If the string already ends with 'ing', it adds 'ly' instead.
    If the string length is less than 3, it leaves the string unchanged.
    
    Parameters:
    input_string : str
        The string to be modified.
    
    Returns:
    str: The modified string with the specified suffix.
    """
    if len(input_string) >= 3:
        if input_string.endswith('ing'):
            return input_string + 'ly'
        else:
            return input_string + 'ing'
    else:
        return input_string

def main():
    # Sample data
    sample_strings = ['abc', 'string', 'go', 'run', 'playing']
    for sample_string in sample_strings:
        result = add_suffix(sample_string)
        print(f"Original String: '{sample_string}' -> Modified String: '{result}'")

if __name__ == "__main__":
    main()
