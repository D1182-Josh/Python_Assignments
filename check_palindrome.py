    #TASK

#Write a program to check if a given string is a Polindrome. A  palindromereads same from front and back e.g. -aba, ccaacc, mom, etc.

#  INPUT: aba
#OUTPUT  : True


    #SOLUTION

word = input("").lower()
print(word[::] == word[::-1])    
