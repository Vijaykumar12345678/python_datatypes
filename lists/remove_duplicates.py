'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to remove the duplicates in a list.
'''

def remove_duplicate(items_list):
    """
    Description:
    remove the duplicate items in a list.
    
    Parameters:
    items_list : list The list of numbers.
    
    Returns:
    list : list To remove the duplicates items in the list.
    """
    unique=[]
    for number in items_list:
        if number not in unique:
            unique+=[number] 
    return  unique

def main():
    # Data
    sample_list = [1, 2, 3, 4, 5,2,1]
    unique_elements = remove_duplicate(sample_list)
    print(f"The unique of all items in the list is: {unique_elements}")

if __name__ == "__main__":
    main()
