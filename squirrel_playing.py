    #TASK

#  The squirrels in Palo Alto spend mopst of the day playing. In particular, they play if the temprature is between 60 and 90 (inclusive). Unless it is summer, then the upper limits is 100 instead of 90. Given an int temprature and a boolean is_summer, return True if the squirrels play and False otherwise. 

    (70, False) --> True
    (95, False) --> False
    (95, True) --> True

  
  #SOLUTION

def playing(temp,summer) :
  if 60 <= temp <= 100  and summer == True:
    return True
  elif  60 <= temp <= 90  and summer == False :
    return True
  else :
    return False
    
print(playing(70, False))
print(playing(95, False))
print(playing(95, True))  
