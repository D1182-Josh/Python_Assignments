    #TASK

#Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of number and for the multiplesof of five print " Buzz". For numbers which are multiples of both three and five print "FizzBuzz". Sample Output: fizzbuzz 1 2 fizz 4 buzz.


    #SOLUTION

n = 100
for i in range(1,n+1):
  if not i % 15:
    print("FizzBuzz")
  elif not i % 5:
    print("Buzz")
  elif not i % 3:
    print("Fizz")
  else:
    print(i)


