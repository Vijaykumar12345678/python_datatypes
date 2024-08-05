'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to split a list based on first character of word.
'''

def split_list_by_first_char(words):
    """
    Description:
    Split a list of words into sublists based on the first character of each word.

    Parameters:
    words : list A list of words to be split.

    Returns:
    dict: A dictionary where the keys are the first characters of the words,
          and the values are lists of words that start with that character.
    """
    result = {}

    for word in words:
        # Get the first character of the word
        first_char = word[0]
        
        # Initialize the list for this character if it doesn't exist
        if first_char not in result:
            result[first_char] = []
        
        # Append the word to the appropriate list
        result[first_char].append(word)

    return result

def main():
    #data
    words = ["apple", "banana", "avocado", "blueberry", "cherry", "apricot"]
    split_words = split_list_by_first_char(words)
    print("Split list by first character:", split_words)
if __name__=="__main__":
    main()