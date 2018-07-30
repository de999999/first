colleges = ["Harvard","Yale","UChicago","Dartmouth","UPenn"]
colleges.sort()
print ("Sorted list:", colleges)

for i in range(len(colleges)-1):
    print(colleges[i])

from random import*
def randomcollege():
    randomnumber = randint(0,len(colleges)-1)
    print(randomnumber)
randomcollege()
