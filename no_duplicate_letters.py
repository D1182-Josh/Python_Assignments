    #TASK

#Given a common phrase, retun False if any individual word in the phrase contains duplicate letters. return True otherwise. 
    Examples
     no_duplicate_letters("Fortune favours the bold.") --> True
    no_duplicate_letters("You can a horse to water, but you can't make him drink.") --> True
     no_duplicate_letters("Look before you leap.") --> False
     Duplicate letters in "Look " and "before". 
      no_duplicate_letters("An apple a day keeps the doctor away.") --> False
      Duplicate letters in "apple", ,"keeps", "doctor", and "away".


     #SOLUTION1

text = "Look before you leap.".split()

all([len(i) == len(set(i)) for i in text])

    #SOLUTION2

def no_duplicate_letters(text) :
  text = text.split()
  return all([len(i) == len(set(i)) for i in text])

no_duplicate_letters("Fortune favours the bold.")    

     
