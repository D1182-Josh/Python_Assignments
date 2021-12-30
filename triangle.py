    #TASK

#    if the entered side lengths do not form a triangle, write the code that determines the type of triangle according to the three side information entered by the user.(In absolute value, the difference of two sides is taken, if the difference is greater than the other side, the entered values do not form a triangle. This is done for all sides.)


    #SOLUTION

sides = list(map(int, input("").split()))
if abs(sides[0] - sides[1]) < sides[2] and abs(sides[1] - sides[2]) < sides[0] and abs(sides[0] - sides[2]) < sides[1] :
  print("It is a triangle!")
else:
  print("It is not a triangle!")
