'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to remove an item from a tuple.
'''

def remove_item_from_tuple(input_tuple, item_to_remove):
    """
    Description:
    This function removes a specified item from a tuple.
    
    Parameters:
    input_tuple : tuple
        The tuple from which an item will be removed.
    item_to_remove : any
        The item to be removed from the tuple.
    
    Returns:
    tuple: The tuple after removing the specified item.
    """
    
    temp_list = list(input_tuple)
    
    if item_to_remove in temp_list:
        temp_list.remove(item_to_remove)
    
   
    return tuple(temp_list)

def main():
    # Data
    sample_tuple = (10, 20, 30, 40, 50)
    item_to_remove = 30
    updated_tuple = remove_item_from_tuple(sample_tuple, item_to_remove)
    
    
    print("Original Tuple:", sample_tuple)
    print("Updated Tuple after removing", item_to_remove, ":", updated_tuple)

if __name__ == "__main__":
    main()
