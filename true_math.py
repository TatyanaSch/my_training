from math import inf


d = inf
def divide(first, second):
    global d
    if second == 0:

        print(d)
    else:
        result = first / second
        print(result)


divide(1, 0)