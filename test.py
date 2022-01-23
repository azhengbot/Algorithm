n = ["2 2", "1 2", "1 2"]

m = ["1 2"]

from collections import Counter

c = Counter(n)

max_count = 0
max_count_point = n[0]

for k, v in c.items():
    if k in m:
        continue
    k_int = [int(i) for i in k.split(" ")]
    max_count_point_int = [int(i) for i in max_count_point.split(" ")]

    print(k_int)
    print(max_count_point_int)
    if v > max_count:
        max_count = v
        max_count_point = k
    if v == max_count:
        if sum(k_int) < sum(max_count_point_int):
            max_count_point = k
        if sum(k_int) == sum(max_count_point_int):
            if k_int[0] < max_count_point_int[0]:
                max_count_point = k

print(max_count_point)
