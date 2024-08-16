'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python script to display user input in upper and lower cases.
'''

def display_upper_lower(user_input):
    """
    Description:
    This function takes a user input string and displays it in upper and lower cases.
    
    Parameters:
    user_input : str
        The input string from the user.
    
    Returns:
    None
    """
    print("Upper case:", user_input.upper())
    print("Lower case:", user_input.lower())

def main():
    # user input
    user_input = input("Enter a string: ")
    display_upper_lower(user_input)

if __name__ == "__main__":
    main()
