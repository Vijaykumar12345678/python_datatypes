'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to concatenate two dictionary.

'''
def concatenate(dictionary1,dictionary2,dictionary3):
    new__dictionary={}
    for dictionaries in(dictionary1,dictionary2,dictionary3):
        new__dictionary.update(dictionaries)
    return new__dictionary
def main():
    dictionary1={1:10,2:20}
    dictionary2={3:30,4:40}
    dictionary3={5:50,6:60}
    result=concatenate(dictionary1,dictionary2,dictionary3)
    print(f"The new dictionary is {result}")
if __name__=="__main__":
    main()
    