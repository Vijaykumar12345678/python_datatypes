'''

@Author:Vijay Kumar M N
@Date: 2024-08-2
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-2
@Title : python program to plot the histogram.

'''
import matplotlib.pyplot as plt

def plot(list_numbers):
    """
    Description:
    This function will plot the histogram
    Parameters:
    list_numbers:list the numbers which is to plot
    return:
    graph"""
    plt.title("Histogram")
    plt.hist(list_numbers)
    plt.show() 
def main():
    list_numbers= [100,150,125,200]
    plot(list_numbers)
if __name__=="__main__":
    main()