"""
You are given a floating-point number hour, representing the amount of time you have to reach the office. 
To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, 
where dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours 
before you can depart on the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) 
that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.

Example 1:
Input: dist = [1,3,2], hour = 6
Output: 1
Explanation: At speed 1:
- The first train ride takes 1/1 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
- Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
- You will arrive at exactly the 6 hour mark.

Example 2:
Input: dist = [1,3,2], hour = 2.7
Output: 3
Explanation: At speed 3:
- The first train ride takes 1/3 = 0.33333 hours.
- Since we are not at an integer hour, we wait until the 1 hour mark to depart. The second train ride takes 3/3 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 2 hour mark. The third train takes 2/3 = 0.66667 hours.
- You will arrive at the 2.66667 hour mark.

Example 3:
Input: dist = [1,3,2], hour = 1.9
Output: -1
Explanation: It is impossible because the earliest the third train can depart is at the 2 hour mark.
"""
# they have 2 section (A) & (B) 
# 1) A => Calculate 
# 2) B => Compare



# *******************(A)*******************
# calculate the time
# how many time to calculate the every Ceil value & Last value 
# in time veriable

def get_time(speed):
    time = 0

    for i in range(len(dist)):  
        if i == dist[i] - 1:        # this is last train(Normal Calculation)
            time += dist[i] / speed

        else:                       # (Ceil Calculation)
            time += -(-dist[i] // speed)

    return time

# *******************(B)*******************

# in this complate mid(speed)  with hour
#  
# if mid <= hour => (right = mid - 1)
# if you incresee the (left += 1) they will have unused to increse the mid(speed) becouse if you used the value are constent or very low

# else:(mid >= hour) => (left = mid + 1)
# if you reduse the (right = mid - 1) they will Loop infinitely / never narrow down correctly, because left and right would keep moving in a direction that never satisfies left > right properly relative to where the real answer is.

# TC:- O(n log n) | SC:- O(n)
def minSpeedOnTime(dist, hour):

    if hour < len(dist) - 1:
        return -1
    
    left = 1
    right = 10**7

    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if get_time(mid) <= hour:
            ans = mid
            right = mid - 1

        else:
            left = mid + 1
    return ans


dist = [1, 3, 2]
hour = 6

print(minSpeedOnTime(dist,hour))


"""
DRY RUN — minSpeedOnTime([1, 3, 2], 2.7)

dist = [1, 3, 2]
hour = 2.7

Binary search range: left = 1, right = 10,000,000
Goal: find smallest speed where get_time(speed) <= 2.7

Since right = 10^7 is huge, the first ~20 iterations all give
"Yes" (time is nearly 0 at huge speeds), so right keeps shrinking
fast (right = mid - 1) while left stays at 1.
Below is the FULL trace of every iteration:

Iter  left      right      mid       get_time(mid)   <=2.7?   action
1     1         10000000   5000000   ~2.0000004      Yes      ans=5000000, right=4999999
2     1         4999999    2500000   ~2.0000008       Yes      ans=2500000, right=2499999
3     1         2499999    1250000   ~2.0000016       Yes      ans=1250000, right=1249999
4     1         1249999    625000    ~2.0000032       Yes      ans=625000,  right=624999
5     1         624999     312500    ~2.0000064       Yes      ans=312500,  right=312499
6     1         312499     156250    ~2.0000128       Yes      ans=156250,  right=156249
7     1         156249     78125     ~2.0000256       Yes      ans=78125,   right=78124
8     1         78124      39062     ~2.0000512       Yes      ans=39062,   right=39061
9     1         39061      19531     ~2.0001024       Yes      ans=19531,   right=19530
10    1         19530      9765      ~2.0002049       Yes      ans=9765,    right=9764
11    1         9764       4882      ~2.0004097       Yes      ans=4882,    right=4881
12    1         4881       2441      ~2.0008193       Yes      ans=2441,    right=2440
13    1         2440       1220      ~2.0016393       Yes      ans=1220,    right=1219
14    1         1219       610       ~2.0032787       Yes      ans=610,     right=609
15    1         609        305       ~2.0065574       Yes      ans=305,     right=304
16    1         304        152       ~2.0131496       Yes      ans=152,     right=151
17    1         151        76        ~2.0263098       Yes      ans=76,      right=75
18    1         75         38        ~2.0526096       Yes      ans=38,      right=37
19    1         37         19        ~2.1052407       Yes      ans=19,      right=18
20    1         18         9         ~2.2222222       Yes      ans=9,       right=8
21    1         8          4         2.5              Yes      ans=4,       right=3
22    1         3          2         4.0              No       left=3
23    3         3          3         2.6666667        Yes      ans=3,       right=2

Loop condition check: left(3) <= right(2)? -> False -> LOOP ENDS

FINAL ANSWER: ans = 3


-------------------------------------------------------------
WHY IT WORKS (theory recap):
-------------------------------------------------------------
- As speed increases, get_time(speed) decreases.
- So valid speeds form a pattern: No No No ... No Yes Yes Yes ...
- We are searching for the FIRST "Yes" (smallest working speed).

- If get_time(mid) <= hour  -> mid WORKS.
    -> Save it as a candidate (ans = mid).
    -> Try to find something smaller: right = mid - 1

- If get_time(mid) > hour   -> mid FAILS.
    -> Nothing smaller can work either.
    -> Move right: left = mid + 1

- Loop ends when left > right, meaning we've narrowed
  down to the exact boundary — the smallest speed that works.

VERIFY: get_time(3) = ceil(1/3) + ceil(3/3) + 2/3
                     = 1 + 1 + 0.666...
                     = 2.666... <= 2.7  ✅ works

         get_time(2) = ceil(1/2) + ceil(3/2) + 2/2
                     = 1 + 2 + 1
                     = 4.0 > 2.7  ❌ fails

So 3 is indeed the minimum speed. Matches LeetCode expected output.
"""