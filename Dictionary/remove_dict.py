'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to remove key to the dictionary.

'''

def add_key(sample_dict):
    """
    Description:
    this function will remove key and value to the  existing dictionary
    parameter:
    sample_dict : dictionary a set of keys and values
    returns:
    New dictionary with  remove key and value pair """
    key_name=int(input("Enter the key name to remove: "))

    del sample_dict[key_name]
    return sample_dict
def main():
    sample_dict={0:10,1:20,2:30,3:40,4:50}
    result=add_key(sample_dict)
    print(f"The new dictionary is : {result}")
if __name__=="__main__":
    main()