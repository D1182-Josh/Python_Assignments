    #TASK

                            
Write a function that reverses the bits in an integer.
For example, the number 417 is 110100001 in binary. Reversing the binary is 100001011 which is 267.
You can assume that the number is not negative.    

    #SOLUTION

def binary(num) :
  bin = ""
  while num != 0 :
    bin += str(num % 2)
    num = num // 2
  return int(bin,2)

binary(417)
...  267

