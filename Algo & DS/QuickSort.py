def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def main():
    """
    Driver code to test the implementation.
    """
    array = [10, 7, 8, 9, 1, 5, 3, 6, 4, 2, 0, 11, 13, 12]
    N = len(array)

    print("Original array:")
    print(*array)

    quick_sort(array, 0, N - 1)

    print("Sorted array:")
    print(*array)


if __name__ == "__main__":
    main()
