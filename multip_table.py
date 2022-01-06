    #TASK

#Make a multiplation table  for 1 to 10. side by side


    #SOLUTION
#1 one after the other / down by down

for i in range(1,11) :
  for j in range(1,11):
    print("{} x {} = {}".format(i,j,j*i))
  print("*" * 10)



#2

j = 1
while j <= 10 :
  for i in range(1,11) :
    if len(str(i))==1 and len(str(j))==1 and len(str(i*j))==1:
      print(" {} x  {} =   {}".format(i,j,i*j), end = "|")
    elif len(str(i))==1 and len(str(j))==1 and len(str(i*j))==2:
      print(" {} x  {} =  {}".format(i,j,i*j), end = "|")
    elif len(str(i))==2 and len(str(j))==1 and len(str(i*j))==2:
      print("{} x  {} =  {}".format(i,j,i*j), end = "|")
    elif len(str(i))==1 and len(str(j))==2 and len(str(i*j))==2:
      print(" {} x {} =  {}".format(i,j,i*j), end = "|")
    elif len(str(i))==2 and len(str(j))==2 and len(str(i*j))==3:
      print("{} x {} = {}".format(i,j,i*j), end = "|")
    else:
      print(" {} x {} ={}".format(i,j,i*j), end = "|")
  j += 1
  print()

#3


for i in range(1,11):
 for j in range(1,11):
  print(format(j,"2d"),"x",format(i,"2d"),"=",format(i*j,"3d"),"|", end="")
 print()
