    #TASK

#Write a python program that writes as many fibonacci sequences as we want from the user. 
#Example; 1, 1, 1, 2, 3, 5, 8(first seven fibonacci numbers)


    #solution

n = int(input(""))
a,b = 0,1
fibonacci = [a,b]
while len(fibonacci) < n :
  a,b = b , a+b 
  fibonacci += [b]

print(fibonacci)    
