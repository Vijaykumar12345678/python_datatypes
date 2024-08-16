'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to create an union of sets.
'''

def union_sets(set1, set2):
    """
    Description:
    This function finds the union of two sets using union method.
    
    Parameters:
    set1 : set
        The first set.
    set2 : set
        The second set.
    
    Returns:
    set: A set containing the union of sets using the method.
    """
    union_method = set1.union(set2)
    
    return (union_method)

def main():
    # Sample sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    union_method = union_sets(set1, set2)
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("union of sets using union method:", union_method)

if __name__ == "__main__":
    main()
