#BINARY SEARCH

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr = list(map(int, input("Enter the sorted array elements (space-separated): ").split()))
target = int(input("Enter the element to search: "))
index = binary_search(arr, target)
print(f"Index of {target}: {index}")

#MERGE SORT

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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
arr = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)


#QUICK SORT

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
arr = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
sorted_arr = quick_sort(arr)
print("Sorted Array:", sorted_arr)

# INSERTION SORT

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
insertion_sort(arr)
print("Sorted Array:", arr)

#SORT A LIST OF STRINGS

def sort_list_of_strings(arr):
    return sorted(arr)
arr = input("Enter the list of strings (comma-separated): ").split(',')
sorted_arr = sort_list_of_strings(arr)
print("Sorted List of Strings:", sorted_arr)