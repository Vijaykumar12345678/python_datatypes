'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: a Python program to get the difference between the two list.
'''

def difference_lists(list1,list2):
    """
    Description:
    This function will print only the elements which are present only in list1 not in list2.
    
    Parameters:
    items_list : list The list of numbers.
    
    Returns:
    list : list the elements which are present in only list1 will return.
    """
    temp3 = []
    for element in list1:
        if element not in list2:
            temp3.append(element)
    return (temp3)

def main():
    # Data
    list1= [1, 2, 3, 4, 5,6,7,8]
    list2=[7,8,9,10,11,12,1]
    result=difference_lists(list1,list2)
    print(result)

  

if __name__ == "__main__":
    main()
