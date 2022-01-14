from itertools import count, cycle

counter = count(7)
cycler = cycle('hello')

for i in range(10):
    print(next(counter), next(cycler))
