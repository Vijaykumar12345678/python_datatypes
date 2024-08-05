'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to display the calendar.

'''
import calendar
def display_year_month(year,month):
    """
    Description:
    This function takes the year and month as a arguments and prints the calendar of that particular month
    
    parameters:
    year : integer The year which calendar have to display
    month: integer The month which calendar have to display
    returns:
    calendar"""
    return calendar.month(year,month)
def main():
    year=int(input("Enter the Year: "))
    month=int(input("Enter the Month: "))
    result=display_year_month(year,month)
    print(result)
if __name__=="__main__":
    main()