'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to demonstrate the use of frozensets.
'''

def frozenset_operations(frozenset1,frozenset2):
    """
    Description:
    Demonstrates the use of frozensets, including creating frozensets,
    performing set operations, and checking immutability.
    Parameters:
    frozenset1: set The elements in the set1
    frozenset2: set The elements in the set2
    Return :
    None
    
    """

    
    # Display frozensets
    print("Frozenset 1:", frozenset1)
    print("Frozenset 2:", frozenset2)
    
    # Perform set operations
    union_result = frozenset1 | frozenset2
    intersection_result = frozenset1 & frozenset2
    difference_result = frozenset1 - frozenset2
    
    # Display results of set operations
    print("Union:", union_result)
    print("Intersection:", intersection_result)
    print("Difference:", difference_result)
    
    # Demonstrate immutability
    # Frozensets cannot be modified, so attempting to update will not work
    updated_frozenset1 = frozenset1.union([9])
    if updated_frozenset1 != frozenset1:
        print("Frozenset cannot be modified directly. New set created instead.")
        print("Updated frozenset1:", updated_frozenset1)
    else:
        print("Frozenset1 remains unchanged as frozensets are immutable.")

def main():
    # Call the function to demonstrate frozenset operations
        # Create two frozensets
    frozenset1 = frozenset([1, 2, 3, 4, 5])
    frozenset2 = frozenset([4, 5, 6, 7, 8])
    frozenset_operations(frozenset1,frozenset2)

if __name__ == "__main__":
    main()
