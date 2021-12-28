       #TASK
 #      integer formatında verilen sayının döngü kullanmadan aralarında birer boşluk bırakarak tersini yazzdırınız..


#SOLUTION

    num = input("please enter a number : ")
    reserve_num = " ".join([i for i in (list(num)[::-1])])
    reserve_num





    OR 
     

     num = 7536
     print(num % 10, (num % 100 -num % 10 ) // 10, (num % 1000 - num % 100) // 100, (    num % 10000 - num % 1000) // 1000)
