    #TASK
  
#Write python codes that calculate the digits of pascal's triangle as many as the number of digits received from the user. 
# input : 6
output : 
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    [1, 5, 10, 10, 5, 1]

    #SOLUTION1

n = int(input(""))
for i in range(n) :
  print(list(str(11 ** i)))


    #SOLUTION2

pascal =[[1],[1,1]]
for i in range(2,10):
  liste=[1]
  for j in range(1,i):
    liste.append(pascal[i-1][j-1]+pascal[i-1][j])
  liste.append(1)
  pascal.append(liste)
for i in pascal:
  print(i) 
    


