
'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to find the repeated items.
'''
def find_repeated_items(input_tuple):
    """
    Description:
    This function finds and returns the repeated items in a tuple.
    
    Parameters:
    input_tuple : tuple The tuple to search for repeated items.
    
    Returns:
    dict: A dictionary with items as keys and their counts as values for repeated items.
    """
    item_count = {}
    
    for item in input_tuple:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    
    repeated_items = {item: count for item, count in item_count.items() if count > 1}
    
    return repeated_items

def main():
    #data
    sample_tuple = (1, 2, 3, 4, 2, 5, 6, 1, 7, 8, 9, 1)
    repeated_items = find_repeated_items(sample_tuple)
    print("Repeated Items and their counts:", repeated_items)
   


if __name__ == "__main__":
    main()
