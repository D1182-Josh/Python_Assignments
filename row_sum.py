    #TASK

#Imagine this triangle:
1
2 3 
4 5 6 
7 8 9 10
.........

#Create a function that takes a number n and returns the sum of all numbers in nth row. Examples rowSum(1)--> 1
        rowSum(2)--> 5
        rowSum(4)--> 34

     #SOLUTION

n = int(input(""))
total = 0 
for i in range(1,n+1) :
  total += i
print(total)
toplam = 0
for j in range(1, total+1) :
  toplam += j
toplam     
