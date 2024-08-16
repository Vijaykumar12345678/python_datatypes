'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to get the last part of a string before a specified character.
'''

def get_last_part_before_character(input_string, character):
    """
    Description:
    This function returns the last part of a string before a specified character.
    
    Parameters:
    input_string : str
        The string from which to extract the last part.
    character : str
        The character before which to extract the last part of the string.
    
    Returns:
    str: The last part of the string before the specified character.
    """
    return input_string.split(character)[0]

def main():
    # Sample input
    input_string1 = "https://www.w3resource.com/python-exercises"
    input_string2 = "https://www.w3resource.com/python"
    character = '-'
    
    # Get the last part before the specified character
    result1 = get_last_part_before_character(input_string1, character)
    result2 = get_last_part_before_character(input_string2, character)
    
    print(f"Original string: {input_string1}\nLast part before '{character}': {result1}\n")
    print(f"Original string: {input_string2}\nLast part before '{character}': {result2}\n")

if __name__ == "__main__":
    main()
