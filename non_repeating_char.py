    #TASK

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
    
    Example 1:
        Input: s = "leetcode"
        Output: 0

    Example 2:
        Input: s =  "loveleetcode"
        Output: 2


     #SOLUTION

s = input("")
for i in s :
  if s.count(i) == 1 :
    print(s.index(i))
    break
else :
  print(-1)     
