    #TASK

#Write a Python program to calculate the sum of three given numbers, if the values are equals are then return three times of their sum?


    #SOLUTION

nums = list(map(int, input().split()))
print(sum(nums) * 3 if nums[0] == nums[1] == nums[2] else sum(nums))    
