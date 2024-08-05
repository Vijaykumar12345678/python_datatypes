'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to convert a list into a nested dictionary of keys.
'''

def list_to_nested_dict(input_list):
    """
    Description:
    This function converts a list into a nested dictionary of keys.
    
    Parameters:
    input_list : list  The list to be converted into a nested dictionary.
    
    Returns:
    dict: A nested dictionary created from the list.
    """
    current_level= {}
    nested_dict = current_level 
    
    
    for key in input_list:
        current_level[key] = {}
        current_level = current_level[key]
        
    return nested_dict

def main():
    """
    This is the main function that defines the sample list,
    calls the list_to_nested_dict function to get the nested dictionary,
    and prints the result.
    """
    
    # Sample list
    sample_list = ['a', 'b', 'c', 'd']
    
    # Convert the list into a nested dictionary
    nested_dict = list_to_nested_dict(sample_list)
    
    # Print the resulting nested dictionary
    print("Nested Dictionary:", nested_dict)

# This block ensures that the main function is called only when the script is run directly
if __name__ == "__main__":
    main()
