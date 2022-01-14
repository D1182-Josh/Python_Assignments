    #TASK

#Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is. For example, if name is Robert Roser, then the output should be R.B. Roser.

    #SOLUTION

name = list(map(str.title, input("").split()))
print("{}.{}.{}".format(name[0][0],name[1][0],name[2]))
