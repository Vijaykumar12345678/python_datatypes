'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to remove the first occurence in the array.

'''
from array import*
def remove_first_occurences(numbers,arrays):
    """
    Description:
    This function will remove the first occurences in the array.
    
    Parameters:
    arrays (array): An array of integers.
    number: integer the number to remove in the first occurence in the array
    returns:
    print the array.
    """
    

    arrays.remove(numbers)
    return str(arrays)
    
        
    
def main():
    number=int(input("Enter the number to remove first occurence in the array:"))
    arrays=array('i',[1,2,3,4,1])
    result=remove_first_occurences(number,arrays)
    print(result)
if __name__=="__main__":
    main()