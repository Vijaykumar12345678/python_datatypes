'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to find how many days between the two dates.

'''
from datetime import datetime
def display(date1,date2):
    """
    Description:
    This function will find the number of days between the two dates.
    parameters:
    date1: sring the first date
    date2: string the second date
    
    returns:
    datetime: the difference between two days
    """
    date_format="%Y-%m-%d"
    date1=datetime.strptime(date1,date_format)
    date2=datetime.strptime(date2,date_format)

    number_of_days=abs(date1-date2)
    return number_of_days
def main():
    date1=input("Enter the first date YYYY-MM-DD ")
    date2=input("ENter the second date YYYY-MM-DD")
    result=display(date1,date2)
    print(result)
if __name__=="__main__":
    main()