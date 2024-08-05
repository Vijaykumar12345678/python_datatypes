'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to check file is present or not.

'''
import os

def check_file_exists(file_path):
    """
    Description:
    This function checks whether a file exists at the given file path.
    
    Parameters:
    file_path : string The path to the file to check.
    
    Returns:
    bool: True if the file exists, False otherwise.
    """
    
    return os.path.isfile(file_path)

def main():
    #user input
    file_path = input("Enter the path to the file: ")
    
   
    if check_file_exists(file_path):
        print(f"The file '{file_path}' exists.")
    else:
        print(f"The file '{file_path}' does not exist.")

if __name__ == "__main__":
    main()
