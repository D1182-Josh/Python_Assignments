    #TASK

#Given a number N, the task is to print the prime numbers from 1 to N.
# Example:    Input : N = 10
		      Output: 2, 3, 5, 7

#Example:     Input: N = 5
              Output: 2, 3, 5

#A prime number is a natural number greater than 1, which is only divisible by 1 and itself.

    #SOLUTION

prime = [2]
n = int(input(""))
for i in range(3,n+1) :
  for j in range(2,i) :
    if i % j == 0 :
      break
  else :
    prime += [i]

print(",".join([str(k) for k in prime]))    
