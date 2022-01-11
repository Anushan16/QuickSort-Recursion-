def qSort(arr):
  # This is the base case for our recursive call 
  if len(arr) < 2:
    return arr
  else:
    # set a pivot
    pivot = arr[0]
    # an array that includes all numbers less than pivot
    lessThanPivot = [i for i in arr[1:] if i < pivot]
    # an array that includes all numbers more than pivot
    moreThanPivot = [e for e in arr[1:] if e > pivot]
    # Recursive call with initial qSort function and appropriate partition of the set, concatenating the two sub sets with the pivot for the final result
    return qSort(lessThanPivot) + [pivot] + qSort(moreThanPivot)


  


print(qSort([2,4,6,8,9,5,3]))