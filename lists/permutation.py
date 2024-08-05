'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title:  Python program to generate all permutations of a list in Python
'''
def permute(elements):
    """
    Generate all permutations of the given list using recursion.

    parameter:
        elements : The list for which permutations are to be generated.

    Returns:
        list: A list of lists, where each sublist is a permutation of the input list.
    """
    if len(elements) == 0:
        return [[]]
    result = []
    for i in range(len(elements)):
        element = elements[i]
        remaining_list = elements[:i] + elements[i+1:]
        for perm in permute(remaining_list):
            result.append([element] + perm)
    return result

def main():
    sample_list = ['A', 'B', 'C']
    permutations = permute(sample_list)
    for perm in permutations:
        print(perm)
    
if __name__ == "__main__":
    main()
