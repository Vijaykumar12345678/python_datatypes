'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to count the number of items in a dictionary value that is a list.
'''

def count_items_in_dict_values(dictionary):
    """
    Description:
    This function counts the number of items in dictionary values that are lists.
    
    Parameters:
    dictionary : dict The dictionary with values that may be lists.
    
    Returns:
    dict: A dictionary with the same keys and the count of items in the list values.
    """
    
    count_dict = {}
    
    for key, value in dictionary.items():
        if isinstance(value, list):
            count_dict[key] = len(value)
        else:
            count_dict[key] = 0
    
    return count_dict

def main():
    # data
    sample_dict = {
        'fruits': ['apple', 'banana', 'cherry'],
        'vegetables': ['carrot', 'broccoli'],
        'meat': 'chicken',
        'grains': ['rice', 'wheat', 'barley', 'oats']
    }
    
    result = count_items_in_dict_values(sample_dict)
    print("Count of items in list values:", result)

if __name__ == "__main__":
    main()
