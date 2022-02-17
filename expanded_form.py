    #TASK

#   Write number in Expanded Form you will be given a number and you will need return it as a string in . For Example: 
                                12 >>>> '10 + 2'
                                42 >>>> '40 + 2 '
                                70304>>>> '70000 + 300 + 4'


     #SOLUTION1

num = input("")[::-1]
" + ".join([str(int(i) * (10 ** num.index(i))) for i in num if i != "0"][::-1])

    #SOLUTION2

num = input("")[::-1]
num_list = []
for i in num :
  if i == 0 :
    
  num_list += [str(int(i) *(10 **(num.index(i))))]

" + ".join((num_list[::-1]))
    

     
