     #TASK

#  Write a Python program to sum of two given integers. However, if the sum is between is 15 to 20 it will return


    #SOLUTION

  while True:
  num =list(map(int, input("").split()))
  if 20 > sum(num) > 15 :
    print(sum(num))
    break
  else:
    print("Please enter different nums :")    



