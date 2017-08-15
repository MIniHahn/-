print    ("请在20内猜测一数，您共有10次机会")
from random import *

a = randint(1,20)

for i in range(10):
    guess = input(">")
    b = int(guess)
    if b>a:
        print ("大了")
        print ("您还有%d次机会" %(9-i))
    elif b<a:
        print ("小了")
        print ("您还有%d次机会" %(9-i))
    else:
        print ("恭喜您，猜对了！") 	
        break