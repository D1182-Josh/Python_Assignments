    #TASK

#Let's make a user name and password to login an account. Firstly define the username and password then take inputs for this two argument from user. DEsign python program 3 possibilities that first one is True user name and password, second is wrong username input and third is wrong password input. Then finish with try again output 

    #SOLUTION

name = input("Lütfen isminizi giriniz :")
password = input("Lütfen şifrenizi giriniz :")

while True :
  if name == "Melek" and password == "1234" :
    print("Başarılı bir şekilde giriş yaptınız!")
    break
  elif name != "Melek" and password == "1234" :
    print("Lütfen kullanıcı isminizi kontrol ediniz!")
    name = input("Lütfen isminizi giriniz :")
    password = input("Lütfen şifrenizi giriniz :")
  elif name != "Melek" and password != "1234" :
    print("Lütfen kullanıcı isminizi ve şifrenizi kontrol ediniz!")
    name = input("Lütfen isminizi giriniz :")
    password = input("Lütfen şifrenizi giriniz :")    
