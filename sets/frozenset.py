'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to demonstrate the use of frozensets.
'''

def main():
    # Create two frozensets
    frozenset1 = frozenset([1, 2, 3, 4, 5])
    frozenset2 = frozenset([4, 5, 6, 7, 8])
    
    # Display frozensets
    print("Frozenset 1:", frozenset1)
    print("Frozenset 2:", frozenset2)
    
    union_result = frozenset1 | frozenset2
    intersection_result = frozenset1 & frozenset2
    difference_result = frozenset1 - frozenset2
    
    # Display results of set operations
    print("Union:", union_result)
    print("Intersection:", intersection_result)
    print("Difference:", difference_result)
    
    print("Attempting to add an element to frozenset1:")
    if frozenset1 != frozenset1.union([9]):
        print("Modification not allowed. Frozensets are immutable.")
    else:
        frozenset1 = frozenset1.union([9])
        print("Updated frozenset1:", frozenset1)

if __name__ == "__main__":
    main()
