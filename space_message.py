    #TASK

#You  have received an encrypted message from space. Your task is to decrypt the message with the following simple rules:
#Message string will consist of capital letters, numbers, and brackets only.
#When there's a block of code inside the brackets, such as [10AB], it means you need to repeat the letters AB for 10 times.
#Message can be embedded in multiple layers of blocks.
#Final decrypted message will only consist of capital letters.
#Create a function that takes encrypted message txt and returns the decrypted message.
#Examples

#space_message("ABCD") ➞ "ABCD"

#space_message("AB[3CD]") ➞ "ABCDCDCD"

"AB" = "AB"

"[3CD]" = "CDCDCD"

space_message("IF[2E]LG[5O]D") ➞ "IFEELGOOOOOD"

        #SOLUTION1
text = "AB[3CD]EF[6G]".split("]")
text =" ".join(text).split("[")
text = " ".join(text).split()
new = ""
for i in text :
  if i[0].isdigit() :
    new += int(i[0]) * i[1:]
  else :
    new += i
print(new)

... ABCDCDCDEFGGGGGG

    #SOLUTION2

def space_message(text) :
  text = text.split("]")
  text =" ".join(text).split("[")
  text = " ".join(text).split()
  return "".join([int(i[0]) * i[1:] if i[0].isdigit() else i for i in text])

space_message("AB[3C]EF[6G]")
... 'ABCCCEFGGGGGG'

