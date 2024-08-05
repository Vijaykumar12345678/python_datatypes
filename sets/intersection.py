'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to create an intersection of sets.
'''

def intersect_sets(set1, set2):
    """
    Description:
    This function finds the intersection of two sets  intersection() method.
    
    Parameters:
    set1 : set
        The first set.
    set2 : set
        The second set.
    
    Returns:
    ser: A set containing the intersection of sets using  method.
    """
    intersection_using_method = set1.intersection(set2)
    
    return (intersection_using_method)

def main():
    # Sample sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    intersection_method = intersect_sets(set1, set2)
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Intersection using intersection method:", intersection_method)

if __name__ == "__main__":
    main()
