    #TASK
 
#in a small town the population is p0=1000 at the beginning if a year. The population regulary increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population grester or equal to p=1200 inhabitants? 

    #SOLUTION

population = 1000
year = 0

while population <= 1200 :
  population += (population * 0.02) + 50
  year += 1

print(year)
    
