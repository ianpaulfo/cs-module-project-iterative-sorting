def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr) ):
        if arr[i] == target:
          return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    if len(arr) == 0:
        return -1 # array empty
    
    low = 0
    high = len(arr)-1
    while high > low:
      midpoint = (high + low) // 2
      if arr[midpoint] == target:
          return midpoint
      elif arr[midpoint] < target:
          low = midpoint
      elif arr[midpoint] > target:
        high = midpoint
  # TO-DO: add missing code

    return -1  # not found
