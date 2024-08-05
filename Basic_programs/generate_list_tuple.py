'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to convert to list and tuple.

'''
def generate_list_tuple(input_numbers):
    """
    Description:
    This function takes a string of comma-separated numbers, 
    and generates both a list and a tuple containing those numbers.
    
    Parameters:
    input_numbers : string a string of comma-separated numbers.
    Return:
    List
    Tuple
    """
    
    List = input_numbers.split(',')
    tuples = tuple(List)
    print("List: ", List)
    print("Tuple: ", tuples)

def main():
    #user input
    input_numbers = input("Enter a sequence of comma-separated numbers: ")
    generate_list_tuple(input_numbers)

if __name__ == "__main__":
    main()
