'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: a Python program to append to a list.
'''

def append_lists(list1,list2):
    """
    Description:
    This function will append the list1 and list2.
    
    Parameters:
    list1 : list The list of numbers.
    list2: list the list of numbers.
    Returns:
    list : list the elements which are present in only list1 will return.
    """
    list1.append(list2)
    return list1

def main():
    # Data
    list1= [1, 2, 3, 4, 5,6,7,8]
    list2=[7,8,9,10,11,12,1]
    result=append_lists(list1,list2)
    print(result)

  

if __name__ == "__main__":
    main()
