'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to reverse a string.
'''

def strings_reverse(input_string):
    """
    Description:
    This function reverse a  string.
    
    Parameters:
    input_string : str The string which has to be reversed.
    
    Returns:
    string: The reversed of the string.
    """
    return input_string[::-1]
def main():
    # Data
    sample_string = "Hello, World!"
    string_reverse = strings_reverse(sample_string)
    print(f"The reverse of a string {string_reverse}")

if __name__ == "__main__":
    main()
