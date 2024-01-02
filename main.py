#Benfords law
import random
one  = 0
two = 0
three = 0 
#print(random.randint(0,9999))
for i in range(0,1000):
  i = random.randint(0,9999)
  number = str(i)
  if number[0] == "1":
    one += 1

  if number[0] == "2":
    two += 1

  if number[0] == "3":
    three += 1

print("ones = " + str(one))
print("twos = " + str(two))
print("threes = " + str(three))
print("Calculated: "+str(one+two+three))
print("Expected: " + str(10*(30.1+17.6+12.5)))
    