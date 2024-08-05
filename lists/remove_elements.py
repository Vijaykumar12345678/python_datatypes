'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to print a specified list after removing the 0th, 4th and
5th elements.
'''
def remove_elements(sample_list):
    """
    Description:
    This function will remove the elements which specified index in the list and prints
    parameter:
    sample_list:list Its containing a list of elements
    returns:
    None"""
    
    del sample_list[5]  
    del sample_list[4]  
    del sample_list[0] 
    
   
    print(sample_list)
def main():
    # Sample list
    sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    remove_elements(sample_list)

if __name__ == "__main__":
    main()
