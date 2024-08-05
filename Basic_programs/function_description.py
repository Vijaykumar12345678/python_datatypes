'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to display the function description of the built-in functions.

'''
def print_docs(func_name):
    """
    Description:
    This function takes the name of a built-in Python function as a string,
    and prints its name along with its documentation string (docstring).
    
    Parameters:
    func_name (str): The name of the built-in function as a string.
    
    Returns:
    If func_name is "abs", the function will print:
    abs() -> abs(number, /)
    Return the absolute value of the argument.
    """
    
    func = getattr(__builtins__, func_name, None)
    
    if func and callable(func):
        print(f"{func_name}() -> {func.__doc__}")
    else:
        print(f"{func_name} is not a built-in function.")

def main():
    # user input
    func_name = input("Enter the built-in function to know: ")
    print_docs(func_name)

if __name__ == "__main__":
    main()

