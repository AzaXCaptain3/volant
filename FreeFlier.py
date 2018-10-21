import random
import time

LENGTH = 100

zone = [0] * LENGTH

for i in range(LENGTH):
    j = random.randint(0,10)
    if j==9:
        zone[i] = 1
print(zone)

total = 0
for i in range (LENGTH):
    total = total + zone[i]
print("Total dents", total)

for i in range(100):
    time.sleep(1.9)
    if (zone[i] == 1):
        point = (("The dent is on point"), (i))
        print(point)








