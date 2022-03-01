    #TASK
#Write a function like this


                    * 1
                  2 1 * *
                * * * 1 2 3
              4 3 2 1 * * * * 
            * * * * * 1 2 3 4 5     

    #SOLUTION

num =5

for i in range(1,num+1) : # üçgenin tepe noktası 1 den başlaması gerektiği için range(0,..) yerine range(1,num+1) diyoruz diyoruz aslında buradaki sayı aralığı bize satır sayısı haliyle döngünün kaç defa döneceğini belirtir.
  bosluk = "  " * (num + 1 - i) #boşluk tanımlamamızın sebebi for döngüsü her tamamlanmasında boşluk azalıyor üçgen formatına geliyor ve azalma miktarı her döngüde girilen satır sayısının bir eksiği kadar oluyor.bunun için -i dedik. 
  if i % 2 == 1 : #her döngüde yazdırma biçimi bir düz bir ters şeklinde ilerdiği için bunu bir formüle sokmamız gerekiyordu. Yani bir koşul karşılandığında düz yazdırsın diğer koşul karşılandığında tersten yazdırsın. for döngüsü  den başlayarak 6 ya kadar değer alacağı için eğer i tek sayıysa yani i % 2 == 1 düz yazdırsın , eğer i çift sayı ise yani i % 2 == 0 ise bize tersten yazdırsın demiş olduk.
    print(bosluk, * i * "*", * range(1,i+1)) #sayı tek veya çiftte olsa önce boşluk düzenlemnesi gerektiği için önce print içine boşluk yazıyoruz, daha sonra tek olduğunda önce yıldız bastırıp daha sonra sayı bastırsın istiyoruz. sayıyı artan şekilde yazdırması için *range() fonk kullanıyoruz.
  else :
    print(bosluk, *range(i,0,-1),* i * "*" )


    so: 
num =5

for i in range(1,num+1)
    bosluk = "  " * (num + 1 - i)
    if i % 2 == 1
       print(bosluk, * i * "*", * range(1,i+1)
     else :
        print(bosluk, *range(i,0,-1),* i * "*" )

    
