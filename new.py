import random
import time

def get_first(data):
    return data[6]
if __name__ == '__main__':
    data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
    print(get_first(data))

def search(nums,target):
    start = 0
    end = len(nums) -1
    
    while start <= end:
        mid = start + (end-start)//2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid +1
        else:
            return mid
    raise ValueError("Target not in the list.")

def binary_search(data, value):
    
    left, right =0, len(data) - 1
    while left <= right:
        middle = (left+right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data [middle]:
            left = middle+1
        else: return middle
    raise ValueError ("Value is not in the list.")

def linear_search(data,value):
    for i in range(len(data)):
        if data[i] == value:
            return i
    raise ValueError ("Value is not in the list.")

if __name__ == '__main__':
    linear_time_arr = []
    binary_time_arr = []
    for i in range (10):
        nums = [random.randint(0, 10000000 + i*500000) for _ in range(10000000 + i*500000)]
        target = random.choice(nums)
        
        #print(f"Random Array: {nums}")
        #print(f"Target = {target}")
        dummy = sorted(nums)
        start_time = time.time()
        result_binary = binary_search(dummy, target)
        end_time = time.time()
        execution_time_binary = end_time - start_time
        print(f"Index of {target} = {result_binary}")
        print(f"Execution time for binary search: {execution_time:.10f} seconds" )
        
        start_time = time.time()
        result_linear = linear_search(nums, target)
        end_time = time.time()
        execution_time_linear = end_time - start_time
        print(f"Execution time for linear search: {execution_time:.10f} seconds" )
        linear_time_arr.append(execution_time_linear)
        binary_time_arr.append(execution_time_binary)
    
    
    
def merge(arr, l, m, r):

    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
  
if __name__ == '__main__':
    nums = [random.randint(0, 10) for _ in range(10)]
    n = len(nums)
    print("Given array is")
    for i in range(n):
        print("%d" % nums[i],end=" ")
    
    mergeSort(nums, 0, n-1)
    print("\n\nSorted array is")
    for i in range(n):
        print("%d" % nums[i],end=" ")

#Heap Algorithm for generating permutation
def heap_permutation(nums, n):
    if n==1:
        print(nums)
        return
    
    for i in range(n):
        heap_permutation(nums, n-1)
        if n%2 == 0:
            nums[i], nums[n-1] = nums[n-1], nums[i]
        else:
            nums[0], nums[n-1] = nums[n-1], nums[0]
            
if __name__ == '__main__':
    nums = [1, 2, 3]
    start_time = time.time()
    heap_permutation(nums, len(nums))
    end_time = time.time()
    print(f"Execution time for heap permutation= {end_time - start_time}")