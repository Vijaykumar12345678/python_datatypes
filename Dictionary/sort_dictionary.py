'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to sort a dictionary by value in ascending and descending order.
'''

def get_value(item):
    """
    Description"
    Helper function to get the value from a dictionary item (key-value pair).
    
    Parameters:
    item : tuple a tuple representing a key-value pair from the dictionary.
    
    Returns:
    The value part of the key-value pair.
    """
    return item[1]

def sort_dict_by_value(input_dict):
    """
    Description:
    This function sorts a dictionary by its values in both ascending and descending order.
    
    Parameters:
    input_dict (dict): The dictionary to be sorted.
    
    Returns:
    Dictonary with ascending order and descending order.
    """
    
    sorted_items_asc = sorted(input_dict.items(), key=get_value)

    
    
    sorted_items_desc = sorted_items_asc[::-1]
    

    sorted_dict_asc = {k: v for k, v in sorted_items_asc}
    sorted_dict_desc = {k: v for k, v in sorted_items_desc}
    
    return sorted_dict_asc, sorted_dict_desc

def main():
    
    #  dictionary
    sample_dict = {'apple': 10, 'banana': 2, 'cherry': 5, 'date': 7}
    sorted_dict_asc, sorted_dict_desc = sort_dict_by_value(sample_dict)
    
    print(f"Original dictionary: {sample_dict}")
    print(f"Dictionary sorted by value (ascending): {sorted_dict_asc}")
    print(f"Dictionary sorted by value (descending): {sorted_dict_desc}")

if __name__ == "__main__":
    main()
