    #TASK

#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.    

    #SOLUTION

def n_divice(n):
  total = sum([i for i in range(1,n) if n % i == 0])
  sum_total = sum([j for j in range(1,total) if total % j == 0])
  if n == sum_total and n != total :
    return n

sum([n_divice(k) for k in range(1,10000) if n_divice(k) != None])
... 31626

    #SOLUTION2
def amicable(nums) :
  def n_divice(n):
    total = sum([i for i in range(1,n) if n % i == 0])
    sum_total = sum([j for j in range(1,total) if total % j == 0])
    if n == sum_total and n != total :
      return n
  return sum([n_divice(k) for k in range(1,nums) if n_divice(k) != None])

amicable(10000)
... 31626




