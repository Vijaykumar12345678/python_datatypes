'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to find maximum and minimum values in a set.
'''

def find_max_min(values_set):
    """
    Description :
    
    Finds and returns the maximum and minimum values in a set.
    
    Parameters:
    values_set : set  The set to find the maximum and minimum values in.
    
    Returns:
    int: A integer the maximum and minimum values.
    """
    if not values_set:
        return None, None  
    
    max_value = max(values_set)
    min_value = min(values_set)
    
    return max_value, min_value

def main():
    # Data
    sample_set = {10, 20, 30, 40, 50}
    max_value, min_value = find_max_min(sample_set)
    if max_value is not None and min_value is not None:
        print(f"Maximum Value: {max_value}")
        print(f"Minimum Value: {min_value}")
    else:
        print("The set is empty.")

if __name__ == "__main__":
    main()
