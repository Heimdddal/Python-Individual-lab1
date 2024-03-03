import random

def generateList(elementsAmount):
    list = []
    for i in range(elementsAmount):
        list.append(random.randint(5, 1400))
    return list

