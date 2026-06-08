# str = ["flower","flow","flight"]

# result = ""
# for s in str:
#     i = 0
#     while s[i] == str:
#         print(s[i])
#         i += 1

a = [1,2,3,4,5,6,7,8,9] 
k = 11
n = len(a)

l = 0
r = len(a) - 1

while l < r:    
    s = a[l] + a[r]

    if s == k:
        print(l,r)
        break

    elif s > k:
        r -= 1

    else:
        l +=1 
