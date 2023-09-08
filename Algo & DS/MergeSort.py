def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(right, left)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def main():
    # Define a list of unsorted integers
    arr = [12, 11, 13, 5, 6, 7, 9, 10, 3, 2, 1, 1]

    # Call the merge sort function and print the sorted array
    sorted_arr = merge_sort(arr)
    print("Sorted array is:", sorted_arr)

if __name__ == "__main__":
    main()
