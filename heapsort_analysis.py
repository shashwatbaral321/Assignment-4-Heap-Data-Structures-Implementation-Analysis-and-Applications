import time
import random
import sys
import copy

# Set higher recursion depth for deep sorts
sys.setrecursionlimit(200000)

# --- Algorithm 1: Heapsort (Max-Heap) ---

def heapify(arr, n, i):
    """
    Maintains the max-heap property for a subtree rooted at index i.
    n is the size of the heap.
    """
    largest = i      # Initialize largest as root
    left = 2 * i + 1   # left child
    right = 2 * i + 2  # right child

    # See if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap them
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def build_max_heap(arr, n):
    """
    Builds a max-heap from an unsorted array.
    This is an O(n) operation.
    """
    # Start from the last non-leaf node and heapify up to the root
    start_index = n // 2 - 1
    for i in range(start_index, -1, -1):
        heapify(arr, n, i)

def heapsort(arr):
    """
    Main function to perform Heapsort in-place.
    """
    n = len(arr)

    # 1. Build a max-heap from the array
    build_max_heap(arr, n)

    # 2. One by one extract elements
    # Move current root (max element) to the end
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        
        # Call heapify on the reduced heap (size i)
        heapify(arr, i, 0)

# --- Algorithm 2: Randomized Quicksort (for comparison) ---
# (From previous assignment)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def random_partition(arr, low, high):
    rand_pivot_index = random.randint(low, high)
    arr[rand_pivot_index], arr[high] = arr[high], arr[rand_pivot_index]
    return partition(arr, low, high)

def _randomized_quicksort(arr, low, high):
    if low < high:
        pi = random_partition(arr, low, high)
        _randomized_quicksort(arr, low, pi - 1)
        _randomized_quicksort(arr, pi + 1, high)

def randomized_quicksort(arr):
    _randomized_quicksort(arr, 0, len(arr) - 1)

# --- Algorithm 3: Mergesort (for comparison) ---

def mergesort(arr):
    """
    Sorts an array using Mergesort.
    Note: This is NOT in-place (O(n) space).
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergesort(left_half)
        mergesort(right_half)

        i = j = k = 0
        
        # Merge the two sorted halves back into arr
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# --- Empirical Comparison ---

def run_experiment(sort_function, array, name):
    """
    Times a sorting function on a copy of the given array.
    """
    arr_copy = copy.deepcopy(array)
    
    start_time = time.perf_counter()
    try:
        sort_function(arr_copy)
    except RecursionError:
        print(f"Failed: {name} - RecursionError")
        return
    end_time = time.perf_counter()
    
    print(f"Finished: {name}")
    print(f"  -> Time taken: {end_time - start_time: .6f} seconds")

if __name__ == "__main__":
    N = 100000  # Array size

    print(f"--- Running Sorting Algorithm Comparison (n={N}) ---")

    # 1. Randomly generated array
    random_arr = [random.randint(0, N * 10) for _ in range(N)]
    
    # 2. Already sorted array
    sorted_arr = list(range(N))
    
    # 3. Reverse-sorted array
    reverse_sorted_arr = list(range(N, 0, -1))

    # --- Run Experiments ---
    
    print("\n[Test 1: Random Array]")
    run_experiment(heapsort, random_arr, "Heapsort")
    run_experiment(randomized_quicksort, random_arr, "Randomized Quicksort")
    run_experiment(mergesort, random_arr, "Mergesort")

    print("\n[Test 2: Sorted Array]")
    run_experiment(heapsort, sorted_arr, "Heapsort")
    run_experiment(randomized_quicksort, sorted_arr, "Randomized Quicksort")
    run_experiment(mergesort, sorted_arr, "Mergesort")

    print("\n[Test 3: Reverse-Sorted Array]")
    run_experiment(heapsort, reverse_sorted_arr, "Heapsort")
    run_experiment(randomized_quicksort, reverse_sorted_arr, "Randomized Quicksort")
    run_experiment(mergesort, reverse_sorted_arr, "Mergesort")
