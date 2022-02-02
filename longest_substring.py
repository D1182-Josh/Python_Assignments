    #TASK

#Given a string s, return the longest palindromic substring in s.

#Example1 : input: s="babad"
            Output: "bab"

#Note: "aba" is also a valid answer.     

#Example 2:  input: s="cbbd"
             output: "bb"

        
        #SOLUTION

max_len = 0
max_sub = ""
s = input("")
for i in range(len(s)) :
  for j in range(1, len(s)+1):
    substring = s[i:j]
    if (substring == substring[::-1]) and (len(substring)> max_len) :
      max_sub = substring
      max_len = len(substring)

max_sub        
