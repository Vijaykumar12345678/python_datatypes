'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python function to find the length of the longest word in a list of words.
'''

def longest_word_length(words_list):
    """
    Description:
    This function takes a list of words and returns the length of the longest word.
    
    Parameters:
    words_list : list
        The list of words to be checked.
    
    Returns:
    int: The length of the longest word.
    """
    
    max_length = 0
    for word in words_list:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

def main():
    # Sample data
    words_list = ["apple", "banana", "cherry", "blueberry", "kiwi"]
    longest_length = longest_word_length(words_list)
    print(f"The length of the longest word in the list is: {longest_length}")

if __name__ == "__main__":
    main()
