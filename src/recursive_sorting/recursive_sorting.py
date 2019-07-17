# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO
    
    # merged_arr = arrA + arrB

    a_index = 0
    b_index = 0 

    while a_index < len(arrA) and b_index < len(arrB):
        if arrA[a_index] <= arrB[b_index]:
            merged_arr.append(arrA[a_index])
            a_index += 1
        else: 
            merged_arr.append(arrB[b_index])
            b_index += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):
    # # TO-DO
    if len(arr) < 2:
        return arr

    midpoint = int(len(arr)/2)
    print(midpoint)
    arr1 = arr[ : midpoint]
    print(f'Array 1 : {arr1}' )
    arr2 = arr[midpoint : ]
    print(f'Array 2 : {arr2}')

    # arr1 = []
    # arr2 = []

    # for i in range(0, len(arr)-1):
    #     if arr[i] < arr[int(len(arr)/2)]: 
    #         arr1.append(arr[i])
    #     else:
    #         arr2.append(arr[i])

    merge(merge_sort(arr1), merge_sort(arr2))

    return arr
    
# merge_sort([1,2,3,9,7,6,4,5])


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
