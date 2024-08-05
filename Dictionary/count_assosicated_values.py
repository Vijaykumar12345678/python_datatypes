'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to count the values associated with a key in a list of dictionaries.
'''

def count_successful_entries(data, key):
    """
    Description:
    This function counts the number of dictionaries in a list that have a specific key with a value of True.
    
    Parameters:
    data : list A list of dictionaries.
    key : string The key to check in the dictionaries.
    
    Returns:
    int: The count of dictionaries where the specified key has a value of True.
    """
    
    count = 0
    for entry in data:
        if key in entry and entry[key] == True:
            count += 1
    return count

def main():
    
    sample_data = [
        {'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'},
        {'id': 3, 'success': True, 'name': 'Alex'}
    ]
    
    key = 'success'
    
    success_count = count_successful_entries(sample_data, key)
    
    print(f"Count of dictionaries with {key} as True: {success_count}")

if __name__ == "__main__":
    main()
