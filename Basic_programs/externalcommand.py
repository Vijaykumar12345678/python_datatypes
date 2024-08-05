'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to display the external commands.

'''
import os
def check_external_command(inputs):
    """
    Description: 
    This function display the exteranl command in the program to display
    parameter:
    inputs: string the user will going to enter which command have to run
    Return :
    None"""
    os.system(inputs)
def main():
    check=input("Enter the external command: ")
    check_external_command(check)
if __name__=="__main__":
    main()