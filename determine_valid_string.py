    #TASK

#Sherlock considers a string to be valid if all characters of the string appear the same  number of times. It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times . Given a string s, determine if it is valid. If so, return YES, otherwise return NO.
    Example
    s = abc
    This is a valid string because frequencies are {a : 1, b: 1, c: 1}
    s = abcc 
    This is a valid string because we can remove one c and have 1 of each character in the remaining string. 
    s = abccc
    This string is not a valid as we can only remove 1 occurence of c. That leaves character frequencies of {a : 1, b: 1, c: 2},

    Function Description
    Complete the isValid function in the editor below.
    isValid has the following parameters(s);
    - string s: a string

    Retuns
    -string: either YES or NO


   #SOLUTION1

from collections import Counter

s = "aabbcdefghh"
c= Counter(s)
freq = Counter(c.values())

if len(freq) == 1 :
  print("YES")
elif len(freq) == 2 :
  if max(freq.keys()) - min(freq.keys()) == 1 and freq[max(freq.keys())] == 1 :
    print("YES")
  elif  min(freq.keys()) == 1 and freq[min(freq.keys())] == 1 :
    print("YES")
  else:
    print("NO")
else:
  print("NO")

  #SOLUTION2
from collections import Counter
def isValid(s):
    c = Counter(s)
    freq = Counter(c.values())
    if len(freq) == 1:
        return "YES"
    elif len(freq) == 2:
        key_max = max(freq.keys())
        key_min = min(freq.keys())
        if key_max - key_min == 1 and freq[key_max] == 1:
            return "YES"
        elif key_min == 1 and freq[key_min] == 1:
            return "YES"
    return "NO"

isValid("aabbcd")
   
