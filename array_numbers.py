    #TASK

#Write an algorithm that takes an array and moves all the zeros t othe end, preserving the order of the other elements. 
    sample = [1, 0, 1, 2, 0, 1, 3]
    output = [1, 1, 2, 1, 3, 0, 0]

  #SOLUTION1

sample = [1, 0, 1, 2, 0, 1, 3]

new_arry = [i for i in sample if i > 0]
for i in range(sample.count(0)) :
  new_arry.append(0)
new_arry
    
    #SOLUTION2

s1 = "hello"
s2 = "world"

for i in s1 :
  for j in s2 :
    if i == j :
      print("YES")
      break
else:
  print("NO")

  

  
