    #TASK

#The Fibonacci sequence of number is a sequence of numbers whose first two terms are 1 and each subsequent term is the sum of the two preceding terms. Print the first 100 fibonacci numbers to the screen.

    #SOLUTION

a,b = 0,1
fibonacci = [a,b]
for i in range(98) :
  a,b = b,a+ b
  fibonacci += [b]
print(fibonacci)
print(len(fibonacci))    
