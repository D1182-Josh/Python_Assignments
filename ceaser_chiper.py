    #TASK

#   ROT13 is a simple letter substitution chiper that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an wxample of the Ceaser cipher. Create a function that takes a string and retuns the string ciphered with Rot13. If there are numbers or special characters included in the string, they shoukd be returned as tehey are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation". please note that using encode is considered cheating. 

    ("tast") >>>> ("grfg")
    ("Test") >>>> ("Grfg")
    ("Tes12t // tESt") >>>> ("Grf12g // gRFg")

    #SOLUTION

alpha_lower = "abcdefghijklmnopqrstuvwxyz"
alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
new_t = ""
text = input("")
for i in text :
  if i.islower() :
    new_t += alpha_lower[(alpha_lower.index(i) + 13) %  len(alpha_lower)]
  elif i.isupper() :
    new_t += alpha_upper[(alpha_upper.index(i) + 13) %  len(alpha_lower)]
  else :
    new_t += i
    
new_t    
