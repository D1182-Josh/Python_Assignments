    #TASK

#   The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 – 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

    Examples:
rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

    #SOLUTION1

def rgb(r,g,b) :
  new_lst = []
  for i in [r,b,g] :
    if i < 0 : new_lst += [0] 
    if i > 255 : new_lst += [255]
    else : new_lst += [i]
  r,b,g = new_lst
  output = "%02x%02x%02x" % (r, g, b)
  return output.upper()

rgb(255,255,255)
... 'FFFFFF'

        #SOLUTION2

def rgb(r,g,b) :
  r,g,b = [0 if i < 0 else 255 if i > 255 else i for i in (r,g,b)]
  return("{:02X}{:02X}{:02X}".format(r,g,b))

rgb(255,255,255)
... 'FFFFFF'

        #SOLUTION3

def rgb_to_hex(r, g, b):
  r, g, b = [0 if i < 0 else 255 if i > 255 else i for i in (r, g, b)]
  return (‘{:02X}{:02X}{:02X}’).format(r, g, b)
rgb_to_hex(255, 255, 300)
...









