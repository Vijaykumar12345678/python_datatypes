
'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: a Python program to find common items from two lists.
'''
def find_common_items(list1, list2):
    """
    Find common items between two lists.

    Parameters:
    list1 : list The first list of items.
    list2 : list The second list of items.

    Returns:
    list: A list containing the items that are common to both list1 and list2.
    """
    common_items = []
    
    for item in list1:
        if item in list2 and item not in common_items:
            common_items.append(item)
    
    return common_items

def main():
    # data
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]

    common_items = find_common_items(list1, list2)
    print("Common items:", common_items)
if __name__=="__main__":
    main()