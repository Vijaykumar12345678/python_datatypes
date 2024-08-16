'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to create and add element  a set.
'''
def main():
    # Sample list of elements
    elements = {1, 2, 3, 4, 4, 5, 6, 7, 1, 2, 5}
    number=int(input("Enter the number to add : "))
    elements.add(number)
    print(elements)
if __name__ == "__main__":
    main()
