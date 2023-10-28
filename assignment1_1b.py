def rate(h):
    return ((60 - h) / 10) - h / 20

h = 10
simu_lst = [h]

for i in range(20):
    new_h = h + rate(h) * 0.5
    simu_lst.append(new_h)
    h = new_h

t = 0
for height in simu_lst:
    print(t, "&", height, chr(92) + chr(92))
    t += 0.5
