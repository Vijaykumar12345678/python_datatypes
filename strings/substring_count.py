'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to count occurrences of a substring in a string.
'''

def count_substring_occurrences(main_string, substring):
    """
    Description:
    This function counts the number of occurrences of a substring in a given string.
    
    Parameters:
    main_string : str The string to search within.
    substring : str The substring whose occurrences are to be counted.
    
    Returns:
    int: The number of occurrences of the substring in the main string.
    """
    return main_string.count(substring)

def main():
    # Sample input
    main_string = "This is a test string. This string is for testing."
    substring = "string"
    occurrences = count_substring_occurrences(main_string, substring)
    print(f"The substring '{substring}' occurs {occurrences} times in the main string.")

if __name__ == "__main__":
    main()
