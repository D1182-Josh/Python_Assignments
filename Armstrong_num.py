    #TASK

#A number from the user will be set to be "Armstrong". For example, if a number has 4 digits and is equal to the 4th (3rd power for 3-digit number) of each of its surroundings, this number is called the "Armstrong" number.

    #SOLUTION

num = input("")
toplam = sum([int(i) ** len(num) for i in num])

if int(num) == toplam :
  print(num, "is a armstrong number")
else:
  print(num, "is not a armstrong number")
