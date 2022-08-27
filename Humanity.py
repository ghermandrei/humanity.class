#print('Hmanity count',Humanity.people)
from ast import Break



class Humanity:
    people=8_000_000_000
    planet = "Earth"
    growth = 0
    decline= 0 

    def dailybirth():
        return 400_000

    def dailydeath()    :
    
        return 150_000
day = 0   
##############Calculation of population################3
for day in range (365):
  day+=1 
  Humanity.growth+=Humanity.dailybirth()
  Humanity.decline += Humanity.dailydeath()
  Humanity.people +=(Humanity.dailybirth()- Humanity.dailydeath())

print(f"Total births at ",  day ," 'th day in 2022 : ",Humanity.growth)
print (f'Total death at ',day ," 'th in 2022 : ",Humanity.decline)    
print (f'Total population at ',day ," 'th in 2022 : ",Humanity.people)    



Humanity_evolution= Humanity.growth-Humanity.decline
if Humanity_evolution >=0:
    print( f"The growth of population at", day,' "thday in 2022 is  ',Humanity_evolution)
else:
    print( f"The growth of population at", day, "th day in 2022 is ",Humanity_evolution) 

    

################### adding more planets##########


   
print ("-----------------------------------")

print('Humanity before planet 2015',Humanity.planet)

Humanity.planet=[Humanity.planet,'mars','moon']


print('Humanity after planet 2015',Humanity.planet)

while len(Humanity.planet) !=5 :
  Humanity.planet.append(input('Add one more planet : '))
  print(('Humanity before planet 2015',Humanity.planet))
 
  