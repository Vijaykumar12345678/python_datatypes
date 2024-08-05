'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to reverse the first name and last name.

'''
def reverse_name(first_name,last_name):
    """
    Description:
     This function reverse the first name and last name and prints
     parameters:
     first_name: string The the name  which entered by user as first name
     last_name: string The the name  which entered by user as last name 
     Return :
     String format where last name and first name"""
    return last_name+ " " + first_name
def main():
    first_name=input("Enter the First Name: ")
    last_name=input("Enter the Last Name: ")
    reversed_names=reverse_name(first_name,last_name)
    print(f"The reversed name is {reversed_names}")
if __name__=="__main__":
    main()