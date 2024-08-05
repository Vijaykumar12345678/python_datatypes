'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to print all unique values in a list of dictionaries.
'''

def get_unique_values(dict_list):
    """
    Description:
    This function extracts all unique values from a list of dictionaries.
    
    Parameters:
    dict_list : list  A list of dictionaries.
    
    Returns:
    set: A set of unique values from the dictionaries.
    """
    
    unique_values = set()
    for dictionary in dict_list:
        for value in dictionary.values():
            unique_values.add(value)
    return unique_values

def main():
    
    
    # Sample data
    sample_data = [
        {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
        {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}
    ]
    
    unique_values = get_unique_values(sample_data)
    print("Unique Values:", unique_values)
if __name__ == "__main__":
    main()
