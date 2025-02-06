import random

set1 = set()
set2 = set()

cont = 0
def createSet1 (card):    
    card = 0
    cont = 0
    while cont < card:
        numRan = random.random()
    numRan = (numRan * 1000 // 10)
    set1.add(numRan)
    cont+=1
    return set1

def createSet2 (card):    
    card = 0
    cont = 0
    while cont < card:
        numRan = random.random()
    numRan = (numRan * 1000 // 10)
    set2.add(numRan)
    cont+=1
    return set2

select = int(input("Elija el set a crear: 1. Set1  2. Set2: " ))
if select == 1:
    cardGet = input("Ingrese la cardinalidad del conjunto a crear: ")
    createSet1(cardGet)