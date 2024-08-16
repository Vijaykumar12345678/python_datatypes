'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to access the envirnoment variable.

'''
import os
def envirnoment_variable(inputs):
    """
    Description: 
    This function display the evirnomental variable
    parameter:
    inputs: string the user will going to enter which command have to run
    Return :
    None"""
    print(os.environ[inputs])
def main():
    check=input("Enter the Variable name: ")
    envirnoment_variable(check)
if __name__=="__main__":
    main()