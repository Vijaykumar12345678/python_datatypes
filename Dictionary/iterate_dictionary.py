'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to iterate by using for loop.

'''
def iterate_forloop(dictionary):
    for key,value in dictionary.items():
        print(f"{key}: {value}")
def main():
    dictionary= {'apple': 10, 'banana': 2, 'cherry': 5, 'date': 7}
    iterate_forloop(dictionary)
if __name__=="__main__":
    main()