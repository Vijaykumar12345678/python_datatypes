'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: a python program to check whether two lists are circularly identical.
'''

def are_circularly_identical(list1, list2):
    """
    Description:
    Check if two lists are circularly identical.

    parameter:
        list1 : The first list to compare.
        list2 : The second list to compare.

    Returns:
        bool: True if the lists are circularly identical, False otherwise.
    """
    if len(list1) != len(list2):
        return False
    
    # Concatenate lst1 with itself to cover all rotations
    doubled_lst1 = list1 + list1
    
    # Check if lst2 is a sublist of the doubled_lst1
    for i in range(len(list2)):
        if doubled_lst1[i:i + len(list2)] == list2:
            return True

    return False

def main():     
    #data
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 1, 2]
    
    if are_circularly_identical(list1, list2):
        print("The lists are circularly identical.")
    else:
        print("The lists are not circularly identical.")

if __name__ == "__main__":
    main()
