'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to print count of the letter in the string.
'''
def count_string(input_string):
    """
    Description:
    This function will count the number of charters in the given string
    parameters:
    input_string: string The given string to count the number of characters .
    return:
    Dict: it will number of charcters in the string"""
    counts_letters={}
    for letter in input_string:
        if letter not in counts_letters:
            counts_letters[letter]=1
        else:
            counts_letters[letter]+=1
    return counts_letters
def main():
    input_string="w3resource"
    result=count_string(input_string)
    print(result)
if __name__=="__main__":
    main()