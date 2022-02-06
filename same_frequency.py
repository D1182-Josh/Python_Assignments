    #TASK

#Given a string s, return True if s is a googd string, or False otherwise. A string s is good if all the characters that appear in s have  the same number of occurrences.
    Example :
        Input: s = "abacbc"
        Output: True 
    Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.


    #SOLUTION

s = input("")
s_dict = {}

for i in s :
  if i in s_dict :
    s_dict[i] +=1
  else :
    s_dict[i] = 1
  
print(len(set(s_dict.values())) == 1)    
