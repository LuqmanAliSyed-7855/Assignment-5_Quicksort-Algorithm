"""Quicksort is an implementation of a sort which applies recursion to partition an array in 
reference to the last element as the pivot. It divides the array into two sub-lists containing 
elements less than or equal to the pivot and greater than the pivot, respectively. These sublists 
are further sorted in the same manner recursively. The last sorted list is acquired as the 
concatenation of the sorted left sub-list, pivot, and the sorted right sub-list."""


# Quicksort Implementation in Python

def quicksort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose the pivot 
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x <= pivot]  
        right = [x for x in arr[:-1] if x > pivot]   

        # Recursively apply quicksort and combine results
        return quicksort(left) + [pivot] + quicksort(right)

# Example usage
if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    print("Original array:", array)
    sorted_array = quicksort(array)
    print("Sorted array:  ", sorted_array)


