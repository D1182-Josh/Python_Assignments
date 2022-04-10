    #TASK


#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.    

    #SOLUTION

nums = list(range(100,1000))
palindrome = 0 
for i in nums: 
  for j in nums :
    temp = i * j
    if str(temp)== str(temp)[::-1] :
      if temp > palindrome :
        palindrome = temp
print(palindrome)

... 906609
