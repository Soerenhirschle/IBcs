import random

def both():
    counter=1
    while counter <3:
        counter +=1
        for x in range(8, -4, -1):
            print(x)
both()


def is_odd(a):
    if a%2 == 0:
        print(str(a) + 'False')
    else:
        print(str(a)+ 'True')

for i in range(1,11):
    is_odd(i)


def dice_roll(a):
    total=-1
    count=0
    while a != total:
        count+= 1
        rollone= random.randint(1,6)
        rolltwo= random.randint(1,6)
        roll3=random.randint(1,6)
        total= rollone+rolltwo+roll3
        # print(total)
    print(count)
dice_roll(12)
