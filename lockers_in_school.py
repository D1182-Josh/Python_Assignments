    #TASK
                                  
#There are number of lockers "n" and number of students "n" in the school. The principal asks the first student to go to every locker and open it. Then he has the second student go to every second locker and close it. The third goes to every third locker and, if it is closed, he opens it, and if it is open, he closes it. The fourth student does this to every fourth locker, and so on. After the process is completed with the "n"th student, how many lockers are open?
#The task is to write a function which gets any number as an input and returns the number of open lockers after last sudent complets his activity. So input of the function is just one number which shows number of lockers and number of students. For example if there are 1000 lockers and 1000 students in school then input is 1000 and function returns number of open lockers after 1000th student completes his action.
#The given input is always an integer greater than or equal to zero that is why there is no need for validation.    

    #SOLUTION1

n = int(input(""))
doors = [1 if i % 2 == 0 else 0 for i in range(n)]

for k in range(2,n) :
  for j in range(k,n,k+1) :
    if doors[j] == 1 :
      doors[j] = 0
    else :
      doors[j] = 1
print(doors.count(1))
... 100
    10

        #SOLUTION2

def locker(x):
   locker = [0 for i in range(0, x)]
   for i in range (0, x):
      for j in range(i, x, i + 1):
         if locker[j] == 0: locker[j] = 1
         elif locker[j] == 1: locker[j] = 0
   return locker.count(1)
locker(100)
... 10





