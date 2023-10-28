import math
import random


def standard_normal(val):
    return math.exp(-(val ** 2)/2) / math.sqrt(2 * math.pi)

sim_len = 100
area_lst= [0, 0]
max_y = standard_normal(0.56)
area = max_y * (2.4 - 0.56)
for i in range(sim_len):
    x = random.uniform(0.56, 2.4)
    y = random.uniform(0, max_y)
    if y <= standard_normal(x):
        area_lst[0] += 1
    else:
        area_lst[1] += 1

print(area_lst, "Integral is:", area * area_lst[0] / sim_len)