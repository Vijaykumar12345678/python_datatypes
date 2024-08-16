'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to replace all occurrences of the first character in a string with '$', except the first character itself.
'''

def replace_char(input_string):
    """
    Description:
    This function replaces all occurrences of the first character in a string with '$', except the first character itself.
    
    Parameters:
    input_string : str
        The string to be modified.
    
    Returns:
    str: The modified string with the specified replacements.
    """
    first_char = input_string[0]
    modified_string = first_char + input_string[1:].replace(first_char, '$')
    return modified_string

def main():
    # Sample data
    sample_string = "restart"
    
    # Modify the string
    result = replace_char(sample_string)
    
    # Print the result
    print(f"Original String: '{sample_string}'")
    print(f"Modified String: '{result}'")

if __name__ == "__main__":
    main()
