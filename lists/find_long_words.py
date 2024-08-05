'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to find the list of words that are longer than n from a given list of words.
'''

def find_long_words(words_list, n):
    """
    Description:
    Finds and returns words longer than a specified length from a given list of words.
    
    Parameters:
    words_list : The list of words to search.
    n : integer The length threshold.
    
    Returns:
    list: A list of words longer than the specified length.
    """
    long_words = [word for word in words_list if len(word) > n]
    return long_words

def main():
    # Data
    sample_words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    
    n = int(input("Enter the length where whose words are longer than that: "))
    long_words = find_long_words(sample_words, n)
    
    print(f"Words longer than {n} characters:", long_words)

if __name__ == "__main__":
    main()
