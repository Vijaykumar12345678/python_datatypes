'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to display the elements where which are present only in set1 not in set2.

'''
def color1_notpresent_color2(color1,color2):
    """Description:
    This function will cdisplay only the elements which are present in set1 and not in set2 
    parameters:
    color1 :set its containing the colors
    color2: set its containing the colors
    return:
    set """
    colors=set()
    for color in color1:
        if color not in color2:
            colors.add(color)
    return colors
def main():
    color1=set({"white","red","black"})
    color2=set({"green","red"})
    result=color1_notpresent_color2(color1,color2)
    print(f"The colors are only present in color1 set {result}")
if __name__=="__main__":
    main()