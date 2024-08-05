'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python function that takes two lists and returns True if they have at least one common member.
'''

def have_common_member(list1, list2):
    """
    Description:
    Checks if two lists have at least one common member.
    
    Parameters:
    list1 : list The first list to compare.
    list2 : list The second list to compare.
    
    Returns:
    bool: True if there is at least one common member, False otherwise.
    """
    for item in list1:
        if item in list2:
            return True
    return False

def main():
    # Data
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 6, 7, 8, 9]
    result = have_common_member(list1, list2)
    print(f"Do the lists have at least one common member: {result}")

if __name__ == "__main__":
    main()
