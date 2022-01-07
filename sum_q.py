    #TASK

#in each while loop, take a number from the user and the numbers entered by the user to a variable named "sum". When the user presses the "q" key, terminate the loop and print the "sum variable" to the screen.

    #SOLUTION

toplam = 0
while True :
  num = input("Please enter number, press q to quit ")
  if num == "q" :
    break
  else :
    toplam += int(num)

print("sum of numbers : " , toplam)    
