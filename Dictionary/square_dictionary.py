'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to generate the number and its square.
'''

def square_dict(number):
    """
    Description:
    This function generates a dictionary with numbers from 1 to n and their squares.
    
    Parameters:
    n : integer the number till where u want to generate.
    
    Returns:
    dict: A dictionary where the keys are numbers from 1 to n and the values are their squares.
    """
    
    square_dict = {}
    for x in range(1, number + 1):
        square_dict[x] = x * x
    return square_dict

def main():
    
    # user input 
    number = int(input("Enter a number: "))
    result_dict = square_dict(number)
    
    print("Generated dictionary:", result_dict)
if __name__ == "__main__":
    main()
