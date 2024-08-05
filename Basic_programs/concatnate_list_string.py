'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to convert list into string.

'''
def concatenate_list_string(elements):
    """
    Description;
    This function will convert list into string.
    parameters:
    elemenths: List Its containing the elements 
    return:
    string will return
    """
    string=" ".join(elements)
    print(string)
def main():
    elements=["python","aws","hadoop","ML Basics"]
    concatenate_list_string(elements)
if __name__=="__main__":
    main()