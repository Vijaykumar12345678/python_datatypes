'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to multiplies all the items in a list.
'''

def multplies_list_items(items_list):
    """
    Description:
    multiplies all the items in a list.
    
    Parameters:
    items_list : list The list of numbers to multiply.
    
    Returns:
    list : list The multiplies of all the items in the list.
    """
    multiplies=[]
    for number in items_list:
        number=number*number
        multiplies+=[number]
    return  multiplies

def main():
    # Data
    sample_list = [1, 2, 3, 4, 5]
    multiplies_sum = multplies_list_items(sample_list)
    print(f"The multiplies of all items in the list is: {multiplies_sum}")

if __name__ == "__main__":
    main()
