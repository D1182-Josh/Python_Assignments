    #TASK

#Given a list, right rotate the list by n position
#Write a program to shift every element of a list to circularly right

    #SOLUTION

#kaç birim kaydırmak istediğimiz sayıyı gidiyoruz.
num = int(input(""))
liste = [1, 2, 3, 4, 5, 6]
new_liste = liste[len(liste)- num:] +liste[0:len(liste)- num]
new_liste    
