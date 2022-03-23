    #TASK

#create a function that returns a list containing the prime factor of whatever integer is passed to it. 
Examples:

    prime_factors(20) --> [2, 2, 5]
    prime_factors(100) --> [2, 2, 5, 5]

    #SOLUTION1

number = 100
primes = []
prime_factor = []
for num in range(2, number + 1):
  for i in range(2, num):
    if (num % i) == 0:
      break
  else:
    primes += [num]

while number != 1 :
  for j in primes :
    if number % j == 0 :
      prime_factor += [j]
      number = number / j

prime_factor
... [2, 5, 2, 5] 

    #SOLUTION2
def prime_factors(number) :
  primes = []
  prime_factor = []
  for num in range(2, number + 1):
    for i in range(2, num):
      if (num % i) == 0:
        break
    else:
      primes += [num]

  while number != 1 :
    for j in primes :
      if number % j == 0 :
        prime_factor += [j]
        number = number / j
  return sorted(prime_factor)

prime_factors(111)
... [3, 37]

        #SOLUTION3

def prime_factor(num) :
  counter = 2
  prime_factors = []
  while num != 1 :
    if not num % counter :
      prime_factors += [counter]
      num /= counter
    else:
      counter += 1
  return prime_factors

prime_factor(130)
... [2, 5, 13]

        #SOLUTION4









