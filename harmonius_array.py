    #TASK

#   We define a harmonious array as an arraywhere the difference between its maximum value and its minimum value is exactly 1. Given an integer array nums, return the length of its longest harmmonious subsequence among all its possible subsequences. A subsequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements. 

    Example:

        Input: nums=[1,3,2,2,5,2,3,7]
        Output: 5
        Explanation: The longest harmonious subsequence is [3,2,2,2,3].

    Example:

        Input: nums=[1,2,3,4]
        Output: 2


     #SOLUTION

nums = [1,3,2,2,5,2,3,7]
new_num = []
x = sorted(set(nums))
for i in range(1,len(x)) :
	if abs(x[i]-x[i-1])==1 :
		new_num.append(nums.count(x[i]) + nums.count(x[i-1]))
if len(new_num) != 0 :
  print(max(new_num))
else :
  print(0)    
