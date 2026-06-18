""" 
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, 
the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""

# Brute force 

# Problem: Container With Most Water
# Approach: Check all pairs, calculate area, keep maximum
# Time: O(n²) | Space: O(1)

"""
Imagin you have to create a container,so
what you need {height,width(base)} 
both are multiplication to create a container (area)
Using Nested Loop 
"""

def maxArea_Brutforce(height):
    max_width = 0
    for i in range(0,len(height)):  
        for j in range(i+1,len(height)):
            high= min(height[i],height[j])    # min value berween Height {i} & Height {j}
            base= j - i                      # find out width on x axis 
            area = high * base             # area 
            max_width = max(max_width,area)

    return max_width

# Optimal 

# Problem: Container With Most Water
# Optimal Approach: Two Pointers – start from both ends, move the smaller height pointer
# Time: O(n) | Space: O(1)

"""
A brute-force approach checks every pair → O(n²). We can do better.
Key insight: Start with the widest possible container (left = 0, right = n-1). 
The water is limited by the shorter of the two walls. 
Moving the taller wall inward can only decrease width without increasing the height limit — 
so we always move the shorter wall inward, hoping to find a taller one.
"""

def maxArea_Optimal(height):
    max_water = 0
    left_pointer = 0
    right_pointer = len(height) - 1

    while left_pointer < right_pointer:

        wdt  = right_pointer - left_pointer

        ht = min(height[left_pointer], height[right_pointer])   # Minimum value find out of both pointers
        currunt_water = ht * wdt
        max_water = max(max_water,currunt_water)                # find out max & store in max_water

        if height[left_pointer] < height[right_pointer]:        # if left side is lower than right side
            left_pointer += 1
        else:
            right_pointer -= 1
        
    return max_water

height = [1,8,6,2,5,4,8,3,7] # assume Hight of the container
print(maxArea_Brutforce(height))
print(maxArea_Optimal(height))