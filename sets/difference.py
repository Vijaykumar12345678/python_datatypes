'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to create an difference of sets.
'''

def difference_sets(set1, set2):
    """
    Description:
    This function finds the difference of two sets using difference method.
    
    Parameters:
    set1 : set
        The first set.
    set2 : set
        The second set.
    
    Returns:
    set: A set containing the difference of sets using the method.
    """
    difference_method = set1.difference(set2)
    
    return (difference_method)

def main():
    # Sample sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    difference_method = difference_sets(set1, set2)
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("difference of sets using difference method:", difference_method)

if __name__ == "__main__":
    main()
