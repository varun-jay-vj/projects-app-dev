def binary_search(arr, val, start, end):
   # Find the position to insert `val` using binary search
   if start == end:
       return start if arr[start] > val else start + 1
   if start > end:
       return start
   mid = (start + end) // 2
   if arr[mid] < val:
       return binary_search(arr, val, mid + 1, end)
   elif arr[mid] > val:
       return binary_search(arr, val, start, mid - 1)
   else:
       return mid
def binary_insertion_sort(arr):
   for i in range(1, len(arr)):
       val = arr[i]
       pos = binary_search(arr, val, 0, i - 1)
       # Insert `val` at the correct position
       arr = arr[:pos] + [val] + arr[pos:i] + arr[i+1:]
   return arr
# Example usage
arr = [37, 23, 0, 17, 12, 72, 31]
sorted_arr = binary_insertion_sort(arr)
print("Sorted array:", sorted_arr)
