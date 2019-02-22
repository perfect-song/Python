'''
一个序列有N个数：A[1]、A[2]、A[3].....A[N],求出最长非降子序列的长度

'''

A = [5, 3, 4, 8, 6, 7]

def fun(A, n):
    length = 1
    d = []
    for i in range(n):
        d.append(1)
        for j in range(i):
            if A[j] <= A[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
        if d[i] > length:
            length = d[i]
    return length


print(fun(A, 6))

