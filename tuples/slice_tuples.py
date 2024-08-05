'''
@Author: Vijay Kumar M N
@Date: 2024-08-05
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-05
@Title: Python program to slice a tuple.
'''

def slice_tuple(input_tuple, start, stop, step):
    """
    Description:
    This function slices a tuple based on the provided start, stop, and step indices.
    
    Parameters:
    input_tuple : tuple
        The tuple to be sliced.
    start : int
        The starting index of the slice.
    stop : int
        The ending index of the slice (exclusive).
    step : int
        The step size of the slice.
    
    Returns:
    tuple: The sliced tuple.
    """
    return input_tuple[start:stop:step]

def main():
    # Data
    sample_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90)
    start_index = 2
    stop_index = 7
    step_size = 2
    
    sliced_tuple = slice_tuple(sample_tuple, start_index, stop_index, step_size)
    print("Original Tuple:", sample_tuple)
    print(f"Sliced Tuple from index {start_index} to {stop_index} with step {step_size}:", sliced_tuple)

if __name__ == "__main__":
    main()
    