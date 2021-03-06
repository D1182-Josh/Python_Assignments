    #TASK

#The drawing shows 6 squares the sides of which have length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters od these squares is: 4* (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80 Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing: 
Hint: 
#    See Fibonacci sequence Ref: http://oeis.org/A00045 The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares. 
    perimeter(5) should return 80 
    perimeter(7) should return 216

    #SOLUTION1

def perimeter(n) :
  a,b = 1,1
  fibo = [a,b]
  while len(fibo) <= n :
    a,b = b, a+b
    fibo += [b]
  return sum(fibo) * 4
perimeter(7)
... 216

    #SOLUTION2
def perimetre(n) :
  numbers = [0,1]
  for i in range(0,n) :
    numbers += [numbers[i]+ numbers[i+1]]
  return sum(numbers) * 4

perimetre(7)
... 216 
        #SOLUTION3
arry = [1, 2, 3, 4, 9, 10, 11, 12, 99, 100, 101 ,200] 
["1-4" ,"9-12", "99-101", "200"]


indeks = []
for i in range(len(arry)-1) :
  if arry[i+1] - arry[i] != 1 :
    indeks += [arry[i]]
new_arry = []
print(indeks)
if len(indeks) == 0 :
  new_arry += ["{} - {}". format(min(arry), max(arry))]
elif len(indeks) == 1 :
  temp = []
  temp += [arry[:arry.index(indeks[0])+1]]
  temp += [arry[arry.index(indeks[0])+1 :]]
  new_arry += ["{} - {}". format(min(temp[0]), max(temp[0]))]
  new_arry += ["{} - {}". format(min(temp[1]), max(temp[1]))]


print(new_arry)

... [4, 12]
    []




