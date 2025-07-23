"""The randomized Quicksort implementation enhances the standard version by selecting a pivot 
at random from the input subarray. It partitions the array into two lists: elements less than 
or equal to the pivot and elements greater than the pivot, excluding the pivot itself. These 
sublists are then sorted recursively using the same randomized strategy. This approach helps 
avoid consistently unbalanced partitions, making the algorithm more efficient on average
 across various input types.
"""


import random

def randomized_quicksort(arr):
    # Base case
    if len(arr) <= 1:
        return arr
    else:
        # Choose a random pivot
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        
        # Partition the array into left and right
        left = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
        right = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]
        
        # Recursively sort and combine
        return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)

# Example usage
if __name__ == "__main__":
    array = [12, 4, 5, 6, 7, 3, 1, 15]
    print("Original array:", array)
    sorted_array = randomized_quicksort(array)
    print("Sorted array:  ", sorted_array)
