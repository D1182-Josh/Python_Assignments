   # TASK

# Kullanıcının girdiği hatalı karakterleri kalın metin(rakam veya özel karakterleri) temizleyen ve sonuçta "Ali Demir" gibi çıktı veren bir kod yazınız.


   #SOLUTION

s = input("sentence")
new_s =""

for i in s :
  if i.isalpha() or i == " " :
    new_s += i


capitalize_s = " ".join([j.capitalize() for j in new_s.split()])
capitalize_s   
