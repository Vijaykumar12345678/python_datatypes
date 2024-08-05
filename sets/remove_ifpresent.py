'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to create and remove element  if its present in a set.
'''
def remove_element(elements,number):
    """
    Description:
    This function will remove if element is present in set.
    parameters:
    elements: set containing a set of elements.
    number: int the number to delete
    return :
    set:new set of elements.
    """
    if number in elements:
        elements.remove(number)
    else:
        return f"The number {number} is not present in the set "
    return f"The number {number} and removed and new set is {elements}"
def main():
    # Sample list of elements
    elements = {1, 2, 3, 4, 4, 5, 6, 7, 1, 2, 5}
    number=int(input("Enter the number to remove : "))
    result=remove_element(elements,number)
    print(result)
if __name__ == "__main__":
    main()
