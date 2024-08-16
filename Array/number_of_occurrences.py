'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to print the number of occurences of a specified element.

'''
from array import*
def number_of_occurences(numbers,arrays):
    """
    Description:
    This function takes an array as an and print the number of times a element is specified.
    
    Parameters:
    arrays (array): An array of integers.
    number: integer the number to check in the array
    returns:
    the number how many have been repeated.
    """
    repeated=0
    for num in range(0,len(arrays)):
        if numbers==arrays[num]:
            repeated+=1
    return repeated
        
    
def main():
    number=int(input("Enter the number to check in the array:"))
    arrays=array('i',[1,2,3,4,1])
    result=number_of_occurences(number,arrays)
    print(f"The {number} is repeated {result} times")
if __name__=="__main__":
    main()