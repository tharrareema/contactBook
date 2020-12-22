import random
random.randrange(0,10)
def multipleclue(n):
    r=random.randint(0,10)
    str1=""
    for k in range(3):
        str1=str1 + "," + str((r+k)*n) 
    return str1
strresult = multipleclue(random.randrange(0,10))
print(strresult)

print("done")

