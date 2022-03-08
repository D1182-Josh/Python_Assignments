    #   TASK

#Write a Python program to count the number of characters in a string. Sample String: 'google.com' Expected Result : {'g' : 2, 'o' : 3, 'l' : 1, 'e' : 1, '.' : 1, 'c' : 1, 'm' : 1}

    #SOLUTION

s = input("")
s_dict = {}
for i in s :
  if i not in s_dict :
    s_dict[i] = 1
  else:
    s_dict[i] += 1

s_dict

    s = "google"
    {i : list(s).count(i) for i in set(s)}


