class twosum:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]


input_list = [2, 8, 12, 15]
object = twosum()
print(object.twoSum(input_list, 17))
