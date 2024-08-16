'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to check if multiple keys exist in a dictionary.
'''

def check_keys_exist(dictionary, keys):
    """
    Description:
    This function checks if all specified keys exist in a dictionary.
    
    Parameters:
    dictionary : dict The dictionary to check.
    keys :list  The list of keys to check for existence in the dictionary.
    
    Returns:
    bool: True if all keys exist in the dictionary, False otherwise.
    """
    
    return all(key in dictionary for key in keys)

def main():
    # data
    sample_dict = {
        'name': 'Alice',
        'age': 25,
        'city': 'New York',
        'occupation': 'Engineer'
    }
    keys_to_check = ['name', 'age', 'city']
    
    result = check_keys_exist(sample_dict, keys_to_check)
    
    print(f"Do all keys {keys_to_check} exist in the dictionary? {result}")

if __name__ == "__main__":
    main()
