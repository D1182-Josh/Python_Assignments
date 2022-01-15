    #TASK

#Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is. For example, if name is Robert Roser, then the output should be R.B. Roser.

    #SOLUTION

name = list(map(str.title, input("").split()))
print("{}.{}.{}".format(name[0][0],name[1][0],name[2]))

    #SOLUTION2

name = list(map(str.upper, input("").split()))
count = 0
for i in name :
  count += 1
  if count < len(name) :
    i = i[0] +( "*" * (len(i) -1))
  else :
    i = i
  print(i , end = " ")

    #SOLUTION3

name = input("").split()
short_name = ""
for i in range(len(name) -1) :
  short_name += name[i][0] + len(name[i][1:]) * "*" + " "
short_name += name[-1]
print(short_name.upper())







