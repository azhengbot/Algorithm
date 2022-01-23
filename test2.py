n = 8
l = [1, 9, 9, 4, 1, 2, 2, 9]


def func(n, l):

    q = [l[0]]

    sum_sub = 0
    for i in range(1, n):
        sum_sub += l[i]

        if sum_sub >= q[-1]:
            q.append(sum_sub)
            sum_sub = 0

    return n - len(q)


print(func(n, l))
