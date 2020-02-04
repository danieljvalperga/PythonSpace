arr = [1, 3, 5, 7, 8, 9]

def search(array, value, start, end):
	if start < 0 or end > len(array):
		return "Invalid value start[", start, "] end[", end, "] for array length[", len(array), "]"

	mid=int((start + end)/2)

	print("value[", value, "] mid[", mid, "] arraymid[", array[mid] ,"] start[", start, "] end[", end, "]")

	if array[mid] == value:
		return "Element found!"
	elif (end - start) <= 1:
		return "Element not found!"
	elif array[mid] > value:
		return search(array, value, start, mid-1)
	else:
		return search(array, value, mid+1, end)

#print(search(arr, 5, 0, len(arr)))

