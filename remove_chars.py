    #TASK

#Write a Python program to remove the characters which have odd index values of a given string.

    #SOLUTION

kelime = input("")
y_kelime = ""
for i in range(len(kelime)) :
  if i % 2 == 0 :
    y_kelime += kelime[i]
print(y_kelime)   
