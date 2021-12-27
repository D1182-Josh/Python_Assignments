    #  task
    Write a python programme to compute the greatest common divisor(GCD) of two pozitive integers


    #SOLUTİON

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

if number1 > number2 :
  bolen = number1
else :
  bolen = number1
for i in range(1, bolen+1):
  if number1 % i == 0 and number2 % i ==0 :
   great_divisor = i
print(great_divisor)   
