'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to get a list, sorted in increasing order by the last element in each tuple .
'''

def sort_by_last_element(tuples_list):
    """
    Description:
    Sorts a list of tuples in increasing order by the last element in each tuple.
    
    Parameters:
    tuples_list : list  The list of tuples to sort.
    
    Returns:
    list: The sorted list of tuples.
    """
    def get_last_element(tuple_item):
        return tuple_item[-1]
    
    return sorted(tuples_list, key=get_last_element)

def main():
    # Sample list of tuples
    sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    sorted_list = sort_by_last_element(sample_list)
    print(f"The sorted list of tuples is: {sorted_list}")

if __name__ == "__main__":
    main()
