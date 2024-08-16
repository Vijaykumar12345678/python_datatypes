'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to lowercase first n characters in a string.
'''

def lowercase_first_n_chars(input_string, n):
    """
    Description:
    This function converts the first n characters of a string to lowercase.
    
    Parameters:
    input_string : str The string in which to convert characters.
    n : int The number of characters from the beginning to convert to lowercase.
    
    Returns:
    str: The modified string with the first n characters in lowercase.
    """
    
    return input_string[:n].lower() + input_string[n:]

def main():
    # Sample input
    input_string = "Hello World! This is a Test String."
    n = 10
    modified_string = lowercase_first_n_chars(input_string, n)
    print("Original string:", input_string)
    print(f"String with first {n} characters in lowercase:", modified_string)

if __name__ == "__main__":
    main()
