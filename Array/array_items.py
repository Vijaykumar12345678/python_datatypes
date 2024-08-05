'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to create a array and display the elements by using indexes.

'''
from array import*
def access_index(arrays):
    """
    Description:
    This function takes an array as an input and prints each element of the array using its index.
    
    Parameters:
    arrays (array): An array of integers.
    returns:
    None
    """
    for number in range(0,len(arrays)):
        print(arrays[number])
def main():
    arrays=array('i',[1,2,3,4,9])
    access_index(arrays)
if __name__=="__main__":
    main()