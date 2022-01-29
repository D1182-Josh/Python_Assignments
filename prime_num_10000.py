    #TASK

#How many of the first 10,000 prime numbers start with 3 and end with 7?

    #SOLUTION

asal_sayılar = [1,2]
num = 3
while len(asal_sayılar)<10000:
    for i in range(2,num):
        if num%i==0:
            break
    else:
        asal_sayılar.append(num)
    num+=1
    
