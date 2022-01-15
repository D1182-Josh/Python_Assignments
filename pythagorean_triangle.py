    #TASK

Write a program that prints the numbers from 1 to 100 a pythagorean triangle. For example: 3 4 5

    #SOLUTION

for x in range(1,100) :
  for y in range(x,100) :
    for z in range(y,100) :
      if x ** 2 + y **2 == z ** 2 :
        print(x,y,z)    
