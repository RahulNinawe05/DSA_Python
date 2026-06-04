# ============================================================
#                   DSA - ARRAYS IN PYTHON
# ============================================================
# What is an Array?
#   - An array is a group of elements stored together.
#   - In Python, we use a LIST as an array.
#   - It can store different types: int, str, float, bool, etc.
#   - Each element has a position called INDEX (starts from 0).
#
# Index Example:
#   arr = [10, 20, 30, 40, 50]
#          0    1   2   3   4   <-- Index numbers
# ============================================================


# -----------------------------------------------
# 1. CREATING AN ARRAY (List)
# -----------------------------------------------
arr = [1, 2, 4, "Rahul", 34.45, True]
#      0  1  2     3       4      5    <-- Index

print("Original Array:", arr)
# Output: [1, 2, 4, 'Rahul', 34.45, True]


# -----------------------------------------------
# 2. ACCESS ELEMENT BY INDEX
# -----------------------------------------------
# Use arr[index] to get any element.

print("Element at index 3:", arr[3])
# Output: Rahul


# -----------------------------------------------
# 3. UPDATE AN ELEMENT
# -----------------------------------------------
# Change any element using its index.

arr[3] = "Ninawe"        # Replace "Rahul" with "Ninawe"
print("After Update     :", arr)
# Output: [1, 2, 4, 'Ninawe', 34.45, True]


# -----------------------------------------------
# 4. APPEND - Add element at the END
# -----------------------------------------------
# append() always adds the new element at the LAST position.

arr.append(999)
print("After Append     :", arr)
# Output: [1, 2, 4, 'Ninawe', 34.45, True, 999]


# -----------------------------------------------
# 5. INSERT - Add element at a SPECIFIC position
# -----------------------------------------------
# Syntax: arr.insert(index, value)
# Elements after that index shift to the right.

arr.insert(2, 3333)      # Insert 3333 at index 2
print("After Insert     :", arr)
# Output: [1, 2, 3333, 4, 'Ninawe', 34.45, True, 999]


# -----------------------------------------------
# 6. POP - Remove element (by index)
# -----------------------------------------------
# arr.pop()    --> removes LAST element
# arr.pop(i)   --> removes element at index i
# pop() also RETURNS the removed element.

arr.pop()                # Removes last element (999)
print("After pop()      :", arr)

arr.pop(0)               # Removes element at index 0 (which is 1)
print("After pop(0)     :", arr)


# -----------------------------------------------
# 7. REMOVE - Remove by VALUE
# -----------------------------------------------
# remove(value) finds the FIRST match of that value and removes it.
# Note: Gives an error if the value is not found in the array.

arr.remove(2)            # Removes the element with value 2
print("After remove(2)  :", arr)


# -----------------------------------------------
# 8. LENGTH OF ARRAY
# -----------------------------------------------
# len() gives total number of elements in the array.

print("Length of Array  :", len(arr))


# -----------------------------------------------
# 9. LOOP THROUGH ARRAY
# -----------------------------------------------
# Use a for loop to go through each element one by one.

print("\nAll elements using loop:")
for element in arr:
    print(" -->", element)


# ============================================================
#              NEW ARRAY FOR BELOW EXAMPLES
# ============================================================
arr1 = [2, 3, 34, 62, 13, 64, -5, 53, 23, 533]
print("\nNew Array:", arr)


# -----------------------------------------------
# 10. SLICE - Get a part of the array
# -----------------------------------------------
# Syntax: arr[start : end]
#   - start  --> index where slice begins (included)
#   - end    --> index where slice stops  (NOT included)
#   - leaving start/end empty means beginning/end of array

print("\nSlice arr[1:3]  :", arr1[1:3])    # index 1 and 2 only → [3, 34]
print("Slice arr[-3:]  :", arr1[-3:])      # last 3 elements    → [53, 23, 533]
print("Slice arr[:-3]  :", arr1[:-3])      # all except last 3  → [2, 3, 34, 62, 13, 64, -5]


# -----------------------------------------------
# 11. CHECK IF VALUE EXISTS (in / not in)
# -----------------------------------------------
# Use 'in' to check if a value is present in the array.
# Returns True or False.

if 13 in arr1:
    print("\n13 is found in array")   # This will print
else:
    print("\n13 is NOT in array")

if 999 not in arr1:
    print("999 is NOT in array")      # This will also print


# -----------------------------------------------
# 12. MIN, MAX, SUM
# -----------------------------------------------
# Only works when ALL elements are numbers (int/float).

print("\nMinimum value :", min(arr1))    # Smallest number
print("Maximum value :", max(arr1))     # Largest number
print("Sum of all    :", sum(arr1))     # Total of all elements


# -----------------------------------------------
# 13. SORT - Arrange elements in order
# -----------------------------------------------
# sort()              --> Ascending  (small to big)
# sort(reverse=True)  --> Descending (big to small)
# Note: sort() changes the ORIGINAL array (in-place).

arr1.sort()
print("\nAfter sort() Ascending :", arr1)

arr1.sort(reverse=True)
print("After sort() Descending:", arr1)


# -----------------------------------------------
# 14. COPY - Make an independent copy
# -----------------------------------------------
# arr1 = arr      --> WRONG! Both point to same array.
#                     Changing arr also changes arr1.
#
# arr1 = arr.copy() --> CORRECT! arr1 is a separate copy.
#                       Changing arr does NOT affect arr1.

arr2 = arr1.copy()        # arr1 is now a separate copy of arr

arr1[5] = 10000           # Change something in arr

print("\nOriginal arr (changed) :", arr1)
print("Copied   arr1 (safe)   :", arr2)
# arr1 is unchanged — proof that copy() works correctly!


# ============================================================
#                      QUICK SUMMARY
# ============================================================
# arr[i]              --> Access element at index i
# arr[i] = val        --> Update element at index i
# arr.append(val)     --> Add val at END
# arr.insert(i, val)  --> Add val at index i
# arr.pop()           --> Remove LAST element
# arr.pop(i)          --> Remove element at index i
# arr.remove(val)     --> Remove first match of val
# len(arr)            --> Total number of elements
# arr[start:end]      --> Slice (part of array)
# val in arr          --> Check if val exists (True/False)
# min(arr)            --> Smallest value
# max(arr)            --> Largest value
# sum(arr)            --> Sum of all values
# arr.sort()          --> Sort Ascending
# arr.sort(reverse=True) --> Sort Descending
# arr.copy()          --> Independent copy of array
# ============================================================