def twoSum(nums, target):
    counter = 1
    for i in nums:
        for j in nums[counter:]:
            if i + j == target:
                return nums.index(i), nums[nums.index(i)+1:].index(j) + nums.index(i) + 1
        counter+=1

print(twoSum([1,3,4,2],6))
print([1,2,3,4][1:3])