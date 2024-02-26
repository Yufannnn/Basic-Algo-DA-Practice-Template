# Given an array of integers, sort the array into a heap using the heap sort algorithm.
# The heap sort algorithm is a comparison-based sorting algorithm that uses a binary heap data structure.

def heapify(arr, n, i):
    """
    Heapify the subtree rooted at index i.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Sort the array using the heap sort algorithm.
    """
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def main():
    """
    Driver code to test the implementation.
    """
    array = [10, 7, 8, 9, 1, 5, 3, 6, 4, 2, 0, 11, 13, 12]
    N = len(array)

    print("Original array:")
    print(*array)

    heap_sort(array)

    print("Sorted array:")
    print(*array)


if __name__ == "__main__":
    main()
