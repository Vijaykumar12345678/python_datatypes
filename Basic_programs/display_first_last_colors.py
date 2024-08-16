'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to display first and last color in the list.

'''
def display_first_last_color(colors_list):
    """
    Description:
    This function takes a list of colors and prints the first and last colors in the list.
    
    Parameters:
    colors_list : list a list of color names as strings.
    
    Returns:
    First_color and Last_color """
    
    print(f"First Color is {colors_list[0]}")
    print(f"Last Color is {colors_list[-1]}")

def main():
    colors_list = ["Red", "Green", "White", "Black"]
    
    display_first_last_color(colors_list)

if __name__ == "__main__":
    main()
