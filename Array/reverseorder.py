'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to reverse the array.

'''
from array import*
def reverse_order(arrays):
    """
    Description:
    This function takes an array as an and print in the reverse order.
    
    Parameters:
    arrays (array): An array of integers.
    returns:
     array
    """
    i=len(arrays)-1
    while i>=0:
        print(arrays[i])
        i-=1
def main():
    arrays=array('i',[1,2,3,4,9])
    reverse_order(arrays)
if __name__=="__main__":
    main()