""" 
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
"""
# ===============================================================================================================================================

"""
****Roman Hamesh Incresing order me calculate kiya jata he****
if value[s[i]] < value[s[i+1]]: condition is true
why current value is less than next value,
it means Roman rule of subtraction is applied

current symbol chhota hai aur next symbol bada hai,
isliye current ko total me add nahi karte,
current ko subtract karte hai

because Roman numeral ka actual value
next − current hota hai
but hum next ko baad me add karenge

example:
I < V  → 1 < 5
isliye 1 ko subtract kiya
baad me V (5) add hoga
final value = 5 − 1 = 4

X < L → 10 < 50
isliye 10 subtract
baad me 50 add
final value = 40

else condition:
jab current value >= next value hoti hai,
to koi subtraction rule nahi hota

iska matlab Roman normal order me hai
isliye current value ko direct total me add kar dete hai


loop ke baad last character ka koi next nahi hota,
isliye wo loop me handle nahi hota

Roman rule ke according
last symbol hamesha add hota hai
isliye last value ko Sum me add karte hai
"""
# TC - O(n) , SC - O(1)

def romanToInt(s):
    value= {
    "I" : 1,"V" : 5,"X" : 10,
    "L" : 50,"C" : 100,"D" : 500,
    "M" : 1000
    }

    Sum = 0

    for i in range(len(s) - 1):
        if value[s[i]] < value[s[i+1]]:
            Sum -= value[s[i]]
        else:
            Sum += value[s[i]]
    Sum += value[s[-1]]
    return Sum
char =  "LVIII"
# char = "XL"
print(romanToInt(char))


