import matplotlib.pyplot as py
import random

list1 = random.sample(range(100), k=20)
list2 = random.sample(range(100), k=20)

py.plot(list1,list2)