'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to count the number of character in a string.
'''

def character_frequency(input_string):
    """
    Description:
    This function counts the frequency of each character in a given string.
    
    Parameters:
    input_string : string
        The string whose character frequency is to be counted.
    
    Returns:
    dict: A dictionary with characters as keys and their frequencies as values.
    """
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def main():
    # Sample data
    sample_string = "google.com"
    result = character_frequency(sample_string)
    print(f"Character frequency in '{sample_string}': {result}")

if __name__ == "__main__":
    main()
