def functioner(emoji) :
  return lambda x :print(x, emoji)
myPrint_smile = functioner(":)")
myPrint_sad = functioner(":(")
myPrint_neutral = functioner(":|")

myPrint_smile("hello")
myPrint_sad("hello")
myPrint_neutral("hello")
