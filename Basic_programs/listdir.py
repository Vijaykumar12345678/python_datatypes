'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to display all the files in the directories.

'''
import os
def list_directories(inputs):
    """
    Description: 
    This function display the all the files in the file
    parameter:
    inputs: list containing the all the files.
    Return :
    None"""
    print(os.listdir(inputs))
def main():
    check=input("Enter the folder path : ")
    list_directories(check)
if __name__=="__main__":
    main()