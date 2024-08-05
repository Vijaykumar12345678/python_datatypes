'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to count the number of strings where the string length is 2 or more and the first and last character are the same.
'''

def count_matching_strings(strings_list):
    """
    Description:
    Counts the number of strings where the string length is 2 or more and the first and last character are the same.
    
    Parameters:
    strings_list : list  The list of strings to check.
    
    Returns:
    int: The count of strings meeting the criteria.
    """
    count = 0
    for string in strings_list:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

def main():
    # data
    sample_list = ['abc', 'xyz', 'aba', '1221']
    result = count_matching_strings(sample_list)
    print(f"The number of strings where the string length is 2 or more and the first and last character are the same is: {result}")

if __name__ == "__main__":
    main()
