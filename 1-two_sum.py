def twoSum(nums, target):
    cache = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in cache:
            return [cache[diff], i]
        cache[num] = i
        
print(twoSum([2, 1, 5, 3], 4)) # [ 1, 3]
print(twoSum([2, 7, 11, 15], 9)) # [0, 1]
print(twoSum([3, 2, 4], 6)) # [1, 2]
print(twoSum([3, 3], 6)) # [0, 1]
print(twoSum([2, 7, 11, 15], 9)) # [0, 1]

