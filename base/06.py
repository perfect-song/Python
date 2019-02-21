'''
内置数据结构（变量类型）
    list
        一组有顺序的数据的组合
        创建：[]、list()
        访问：使用下标（索引）从0开始\
        分片操作：
            [:] 左闭右开. 如果不写，左边默认为0，右边默认为len(l)
            分片可以控制增长幅度，默认增长幅度为1[a:b:c]从a到b（不包括b）增长幅度为c
            下标可以超出范围，超出后就不考虑了
            下标可以为负,但是坐标的值必须小于右边的值
            如果分片一定要左边比右边大，则步长需要使用负数

    set
    dict
    tuple
'''
# 创建
l1 = []
print(type(l1))
l2 = list()
print(type(l2))

# 访问
l = [1, 2, 3, 4, 5, 6]
print(l[3])
for i in range(len(l)):
    print(l[i])

# 分片
print(l[1:3])
print(l[1:])
print(l[:4])

# 幅度
print(l[1:6:2])
# 下标越界
print(l[1:8])

# 负数下标
print(l[-4:-2])
print(l[-2:-4:-1])

# 反转列表
print(l[::-1])

'''
内置函数id() 负责显示一个变量或者数据的唯一确定编号
'''
# 注意
l1 = [2, 4, 512, 5, 6, 32]
l2 = l1[:]
l3 = l1
print(id(l1))
print(id(l2))
print(id(l3))
l1[2] = 100
print(l1)
print(l2)
print(l3)
print(id(l1))
print(id(l2))
print(id(l3))

print('*' * 50)

a = 10
b = a
print(id(a))
print(id(b))
a = 11
print(a)
print(b)
print(id(a))
print(id(b))
