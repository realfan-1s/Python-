import timeit
import random


def test1():
    list = []
    for i in range(1000):
        list += [i]


def test2():
    list = []
    for i in range(1000):
        list.append(i)


def test3():
    list = [i for i in range(1000)]


def test4():
    List = list(range(1000))


t1 = timeit.Timer('test1()', 'from __main__ import test1')
print('contact ', t1.timeit(number=1000), ' ms')

t2 = timeit.Timer('test2()', 'from __main__ import test2')
print('contact ', t2.timeit(number=1000), ' ms')

t3 = timeit.Timer('test3()', 'from __main__ import test3')
print('contact ', t3.timeit(number=1000), ' ms')

t4 = timeit.Timer('test4()', 'from __main__ import test4')
print('contact ', t4.timeit(number=1000), ' ms')

for i in range(10000, 1000001, 20000):
    t = timeit.Timer('random.randrange(%d) in x' % i,
                     'from __main__ import random, x')
    x = list(range(i))
    list_Time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    dict_Time = t.timeit(number=1000)
    print('%d, %10.3f,%10.3f' % (i, list_Time, dict_Time))
