"""
A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, 
we load the ship with packages on the conveyor belt (in the order given by weights). 
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 
and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:

Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
"""

# why firstly calculate low = max(weights)
# => in every day ship capacity fixed , don't break the packege 

# Core Logic:-
# The ship loads packages in order, every day.
# If ship capacity is less than any single package, that package cannot be shipped.
# So, minimum ship capacity = maximum weight package.

# TC:- O(n^2)   |  SC:- O(1)
def shipWithinDays_Brute_Solution(weights, days):
    min_capacity = max(weights) 
    max_capacity = sum(weights) 
    for capacity in range(min_capacity, max_capacity+1):    

        day_used = 1
        currunt_load = 0

        for w in weights:                                  
            if currunt_load + w <= capacity:
                currunt_load += w

            else:
                day_used += 1
                currunt_load = w

        if day_used <= days:
            return capacity


def shipWithinDays_Optimal_Solution(weights, D):
    left = max(weights) 
    right = sum(weights) 

    while left <= right:

        mid = (left + right) // 2


        days_used = 1
        calculate = 0

        for w in weights:                                  
            if calculate + w <= mid:
                calculate += w
            else:
                days_used += 1
                calculate = w

        if days_used > D:
            left = mid + 1
        else:
            right = mid - 1

    return left

weights= [3,2,2,4,1,4]
days = 3

print(shipWithinDays_Brute_Solution(weights,days))
print(shipWithinDays_Optimal_Solution(weights,days))


# capacity  is inversly propotion to the days

"""
Inputs: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Initial values:

left = 10 (max weight)
right = 55 (sum of weights)

Iteration 1

left=10, right=55 → mid = 32
Simulate loading with capacity 32:
Day 1 loads: 1,2,3,4,5,6,7 (total = 28) — adding 8 would make 36, too much
Day 2 loads: 8,9,10 (total = 27)
days_used = 2
Since 2 ≤ D(5), capacity 32 works → try smaller → right = 31(mid - 1)


Iteration 2

left=10, right=31 → mid = 20
Simulate with capacity 20:
Day 1: 1,2,3,4,5 (=15)
Day 2: 6,7 (=13)
Day 3: 8,9 (=17)
Day 4: 10 (=10)
days_used = 4
4 ≤ 5 → works → right = 19(mid - 1)


Iteration 3

left=10, right=19 → mid = 14
Simulate with capacity 14:
Day 1: 1,2,3,4 (=10)
Day 2: 5,6 (=11)
Day 3: 7 (=7)
Day 4: 8 (=8)
Day 5: 9 (=9)
Day 6: 10 (=10)
days_used = 6
6 > 5 → too slow, capacity too small → left = 15


Iteration 4

left=15, right=19 → mid = 17
Simulate with capacity 17:
Day 1: 1,2,3,4,5 (=15)
Day 2: 6,7 (=13)
Day 3: 8,9 (=17)
Day 4: 10 (=10)
days_used = 4
4 ≤ 5 → works → right = 16


Iteration 5

left=15, right=16 → mid = 15
Simulate with capacity 15:
Day 1: 1,2,3,4,5 (=15)
Day 2: 6,7 (=13)
Day 3: 8 (=8)
Day 4: 9 (=9)
Day 5: 10 (=10)
days_used = 5
5 ≤ 5 → works → right = 14
"""