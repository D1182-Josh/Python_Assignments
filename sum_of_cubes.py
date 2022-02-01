    #TASK

#How many of the 3-digit numbers are equal to the sum of the cubes of their digits.

    #SOLUTION

toplam = 0
counter = 0
for i in range(100, 1000) :
  for j in str(i) :
    toplam = toplam + int(j) ** 3
  if i == toplam :
    counter += 1
    print(toplam)
  toplam = 0
print(counter)    
