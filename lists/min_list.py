'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to find the minimmum element in a list.
'''

def min_list_items(items_list):
    """
    Description:
    minimum element  in a list.
    
    Parameters:
    items_list : list The list of numbers to sum.
    
    Returns:
    int : int The minimum element in the list.
    """
    
    return  min(items_list)

def main():
    # Data
    sample_list = [1, 2, 3, 4, 5,0]
    min_element = min_list_items(sample_list)
    print(f"The minimum element in the list is: {min_element}")

if __name__ == "__main__":
    main()
