'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to print unique words from a comma-separated sequence in sorted order.
'''

def get_unique_sorted_words(words):
    """
    Description:
    This function takes a comma-separated sequence of words, removes duplicates,
    and returns the unique words in sorted form.
    
    Parameters:
    words : str
        The input string containing comma-separated words.
    
    Returns:
    list: A list of unique words sorted alphanumerically.
    """
    word_list = words.split(',')
    unique_words = sorted(set(word_list))
    return unique_words

def main():
    # Sample input
    input_words = "red, white, black, red, green, black"
    unique_sorted_words = get_unique_sorted_words(input_words)
    print("Unique sorted words:", ', '.join(unique_sorted_words))

if __name__ == "__main__":
    main()
