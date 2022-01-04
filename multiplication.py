    #TASK
 
 #Try to print a multiplication table with numbers from 1 to 10.


    #SOLUTION

num = int(input("Please enter a number : "))
for i in range(11):
  print("{} x {} = {}".format(num,i,num*i))
