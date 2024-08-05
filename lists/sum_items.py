'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to sum all the items in a list.
'''

def sum_list_items(items_list):
    """
    Description:
    Sums all the items in a list.
    
    Parameters:
    items_list : list The list of numbers to sum.
    
    Returns:
    int : int The sum of all the items in the list.
    """
    sums=0
    for number in items_list:
        sums+=number
    return  sums

def main():
    # Data
    sample_list = [1, 2, 3, 4, 5]
    total_sum = sum_list_items(sample_list)
    print(f"The sum of all items in the list is: {total_sum}")

if __name__ == "__main__":
    main()
