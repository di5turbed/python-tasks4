import math

def prostye():
    num = 2
    while True:
        prostoe = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                prostoe = False
                break
        if prostoe:
            yield num
        num += 1

generator = prostye()
for x in range(10):
    print(next(generator))