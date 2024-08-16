'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to find out the number of cpus are using.

'''
import multiprocessing
def cpu_count():
    """
    Description:
    This Function will print the number of cpus using
    Parameters:
    returns: """

    print(multiprocessing.cpu_count())
def main():
    cpu_count()
if __name__=="__main__":
    main()