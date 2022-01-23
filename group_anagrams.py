    #TASK

#Title: given an array of string,you can combine words with different letters. Alphabetic words refer to strings with the same letters but arranged differently. Given an array of string, group anagrams together.
#Example:
#input:["eat","tea","tan","ate","nat","bat"]
#output:
    **[
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
     ]
#Explain:
    #All inputs are lowercase.Do not consider the order of the answer output.Note:
#All inputs will be in lowercase.The order your output does not matter.

    #SOLUTION

strs = ["eat", "tea", "tan", "ate", "nat", "bat", "cat", "tac"]
group = {}

for i in strs :
  kelime = "".join(sorted(i))
  if kelime in group :
    group[kelime].append(i)
  else :
    group[kelime] = [i]

print(list(group.values()))    

