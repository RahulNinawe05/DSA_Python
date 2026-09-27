"""
Given two sorted arrays a[] and b[], 
where each array may contain duplicate elements , 
the task is to return the elements in the union of the two arrays in sorted order. 
Union of two arrays can be defined as the set containing 
distinct elements that are present in either of the arrays.
"""
# 1st Approch 
arr1= [1, 2, 3, 4, 5]
arr2= [1, 2, 3,3,4, 6, 7]


def first_approch(arr1,arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    union_set = set1.union(set2)
    result = sorted(union_set)

    return result

# 2nd Approch
def sec_approch(arr1,arr2):

    i , j = 0 , 0
    union_set = []
    last = None

    n = len(arr1)
    m = len(arr2)


    # if both arr lenght is same
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            if last != arr1[i]:
                union_set.append(arr1[i])
                last = arr1[i]

            i+= 1

        elif arr1[i] > arr2[j]:
            if last != arr2[j]:
                union_set.append(arr2[j])
                last = arr2[i]

            j += 1

        else:
            if last!= arr1[i]:
                union_set.append(arr1[i])
                last = arr1[i]


            i+=1
            j+=1

    # if both of one arr length is small 

    while i < n:
        if last != arr1[i]:
            union_set.append(arr1[i])
            last = arr1[i]

        i += 1

    while j < m:
        if last != arr2[j]:
            union_set.append(arr2[j])
            last = arr2[j]

        j += 1

    return union_set


print(first_approch(arr1,arr2))
print(sec_approch(arr1,arr2))