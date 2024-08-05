'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to demonstarte the symmetric difference.
'''

def get_set_input(prompt):
    """
    This function prompts the user to input a set of integers.
    :param prompt: The prompt message to display.
    :return: A set of integers.
    """
    return set(map(int, input(prompt).split()))

def symmetric_difference(set1, set2):
    """
    This function returns the symmetric difference of two sets.
    :param set1: The first set.
    :param set2: The second set.
    :return: The symmetric difference of set1 and set2.
    """
    return set1.symmetric_difference(set2)

def main():
  
    set1 = get_set_input("Enter the first set of integers (space-separated): ")
    set2 = get_set_input("Enter the second set of integers (space-separated): ")
    
    sym_diff = symmetric_difference(set1, set2)
    
    print("The symmetric difference is:", sym_diff)

if __name__ == "__main__":
    main()
