'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to print a dictionary in table format.
'''

def print_dict_table(dictionary):
    """
    Description:
    This function prints a dictionary in a table format.
    
    Parameters:
    dictionary : dict The dictionary to be printed.
    Return:
    None
    """
    

    key_width = max(len(str(key)) for key in dictionary.keys())
    value_width = max(len(str(value)) for value in dictionary.values())
    
 
    for key, value in dictionary.items():
        print(f"{str(key).ljust(key_width)} | {str(value).ljust(value_width)}")

def main():
    
    
    # Sample dictionary
    sample_dict = {
        'Name': 'Alice',
        'Age': 25,
        'City': 'New York',
        'Occupation': 'Engineer'
    }
    
    print_dict_table(sample_dict)

if __name__ == "__main__":
    main()
