'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to display formatted text with specified width.
'''

import textwrap

def format_text(input_text, width):
    """
    Description:
    This function formats the input text to a specified width.
    
    Parameters:
    input_text : str The text to be formatted.
    width : int The width to format the text to.
    
    Returns:
    str: The formatted text.
    """
    return textwrap.fill(input_text, width)

def main():
    # Sample input text
    sample_text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                   "Vestibulum et ligula in nunc bibendum fringilla a eu lectus. "
                   "Sed sit amet libero non ligula suscipit suscipit. "
                   "Praesent sodales sem sit amet lorem malesuada tincidunt.")
    width = 50
    formatted_text = format_text(sample_text, width)
    print(formatted_text)

if __name__ == "__main__":
    main()
