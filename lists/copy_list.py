'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to clone or copy a list.
'''

def clone_list(original_list):
    """
    Description:
    Clones or copies a list.
    
    Parameters:
    original_list : list The list to be cloned or copied.
    
    Returns:
    list: A new list that is a copy of the original list.
    """
    return original_list[:]

def main():
    # Sample list
    sample_list = [1, 2, 3, 4, 5]
    
    cloned_list = clone_list(sample_list)
    
    print("Original list:", sample_list)
    print("Cloned list:", cloned_list)

if __name__ == "__main__":
    main()
