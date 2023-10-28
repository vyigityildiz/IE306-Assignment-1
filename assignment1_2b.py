import random
import matplotlib.pyplot as plt

def variance(lst):
    mean = sum(lst) / len(lst)
    var = 0
    for i in lst:
        var += (i - mean) ** 2
    return var / len(lst)

val_lst = list()

for i in range(750):
    rand_nums = [random.uniform(0, 1) for j in range(10)]
    val_lst.append(sum(rand_nums))

mean_val = sum(val_lst) / len(val_lst)
variance_val = variance(val_lst)
print("Mean:", mean_val, "Variance:", variance_val)

plt.hist(val_lst, bins=30)
plt.show()