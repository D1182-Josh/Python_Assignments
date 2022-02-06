    #TASK

#Asquare triple(a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2. Given an integer n, return the number of square triples such that 1 <=a, b, c<=n. Example:
        Input: n=5
        Output: 2
        Explanation: The square triples are (3,4,5) and (4,3,5)


     #SOLUTION

n = int(input(""))
counter = 0

for i in range(1,n+1) :
  for j in range(1,n+1) :
    for k in range(1,n+1) :
      if i ** 2 + j ** 2 == k ** 2 :
        counter += 1
print(counter)     
