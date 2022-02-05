    #TASK

#Write a program that given a string and replace every letter with its position in the alphabet. If anything in the text isn't a letter , ignore it and don't return. "a"=1, "b"=2, etc. Example alphabet_position("The sunset sets at twelve o'clock.") Should return "20 8 5 19 21 14 19 5 20 19 1 20 20 23 5 12 22 5 3 12 15 3 11" 


    #SOLUTION

alpha = "abcdefghijklmnopqrstuvwxyz"
string = input("").lower()
print(* [alpha.index(i)+1 for i in string if i.isalpha()])    
