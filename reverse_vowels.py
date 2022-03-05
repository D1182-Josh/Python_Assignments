    #TASK

#Given a string s, reverse only all the vowels in the string and return it. The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in the both cases. 
    Example 1:
        Input: s= "hello"
        Output: "holle"

    Example 2:
        Input: s = "leetcode"
        Output: "leotcede"

    #SOLUTION1

s = "hello"
indeks = [i for i in range(len(s)) if s[i] in "AEIOUaeiou"]
consonants = [j for j in s if j not in "AEIOUaeiou" ]
vowels = [k for k in s if k in "AEIOUaeiou"][::-1]

for i in range(len(indeks)) :
  consonants.insert(indeks[i], vowels[i])
print("".join(consonants))

    
