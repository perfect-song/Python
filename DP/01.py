'''
动态规划：
计算 n 最少有多给少个V中元素组成 V=[1,3,5]

'''

V = [1, 3, 5]
def fun(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    m = []
    for v in V:
        if v <= n:
            m.append(fun(n - v) + 1)
    return min(m)


print(fun(5))
