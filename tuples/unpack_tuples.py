'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to unpack a tuple into several variables.
'''

def unpack_tuple(sample_tuple):
    """
    Description:
    This function unpacks a tuple into several variables and prints them.
    
    Parameters:
    sample_tuple : tuple The tuple to unpack.
    """
    
    (var1, var2, var3, var4, var5, var6) = sample_tuple
    
    print("Unpacked Variables:")
    print(f"var1: {var1}")
    print(f"var2: {var2}")
    print(f"var3: {var3}")
    print(f"var4: {var4}")
    print(f"var5: {var5}")
    print(f"var6: {var6}")

def main():
    #data
    sample_tuple = ('red', 'black', 'blue', 10, 3.14, False)
    
    unpack_tuple(sample_tuple)

if __name__ == "__main__":
    main()
