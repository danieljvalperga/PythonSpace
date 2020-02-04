from BinarySearch import search

arr1 = [1, 3, 5, 7, 8, 9]
arr2 = [1, 2, 3, 4, 5, 7, 8, 9]


print(search(arr1, 5, 0, len(arr1)))
print(search(arr1, 6, 0, len(arr1)))
print(search(arr2, 5, 0, len(arr2)))
print(search(arr2, 6, 0, len(arr2)))
