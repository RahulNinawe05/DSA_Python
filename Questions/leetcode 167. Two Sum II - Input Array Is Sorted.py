def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        s = numbers[l] + numbers[r]

        if s == target:
            return [l + 1, r + 1]
        elif s > target:
            r -= 1
        else:
            l += 1

numbers = [1,2,3,4,5,6,7,8]
target = 11

print(twoSum(numbers,target))