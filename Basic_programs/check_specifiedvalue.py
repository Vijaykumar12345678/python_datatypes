'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to check the given number is present in the given list or not.

'''
def check(number,list_numbers):
    """
    Description:
    This function will check the given number in the list or not .
    parameters:
    number: integer The which need to be checked
    list_numbers: list The list which having the numbers
    return :
    Bool: the number is present means return true or else false."""
    if number in list_numbers:
        return True
    else:
        return False
def main():
    number=int(input("Enter the number to check in the list:"))
    list_numbers=[1,2,3,4,5,6]
    result=check(number,list_numbers)
    print(result)
if __name__=="__main__":
    main()