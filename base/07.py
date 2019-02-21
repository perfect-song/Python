'''
汉诺塔问题
规则：
    每次移动一个盘子
    任何时候大盘子在下面，小盘子在上面
方法：
    1、n=q时，直接把A上的一个盘子移动到C上
    2、n=2时，
        把小盘子从A移动到B上
        把大盘子从A移动到C上
        把小盘子从B移动到C上
    3、n=3时：
        把A的两个盘子通过C移动到B上去，调用递归实现
        把A上剩下的一个最大盘子移动到C上
        把B上两个盘子，借助A移动到C上去，递归调用
    4、n=n时
        把A上的n-1个盘子借助C移动到B上，递归调用
        把A上最大盘子，移动到C上
        把B上的n-1个盘子，借助A移动到C 递归调用
'''


def hanno(n, a, b, c):
    if n == 1:
        print(a, '->', c)
        return None
    if n == 2:
        print(a, '->', b)
        print(a, '->', c)
        print(b, '->', c)
        return None
    # 吧n-1个盘子，借助c 移动到b
    hanno(n - 1, a, c, b)
    print(a, '->', c)
    # 把n-1个盘子，借助a移动到c
    hanno(n - 1, b, a, c)


#
# a = 'A'
# b = 'B'
# c = 'C'
# hanno(3, a, b, c)

'''
List
    del:删除命令  原地删除（id不变）
'''
# a = [1,2,3,4]
# print(id(a))
# print(a[2])
# del a[2]
# print(a)
# print(id(a))
# print(a[2])


'''
列表相加
    使用+连接两个列表
    使用乘 相当于把n个列表拼在一起
    
成员资格运算
    使用in 判断一个元素是否在列表中，同样not in 用于判断不在里面 in后面的变量要求是可迭代的内容
        
列表遍历
    for
    while
    
    
'''
a = [23, 13, 4, 6, 12, 5, 11]
for i in a:
    print(i)

print('*' * 20)
length = len(a)
idx = 0
while idx < length:
    print(a[idx])
    idx += 1
# 双层列表  对应上就行
b = [['one', 1], ['two', 2], ['three', 3]]
for k, v in b:
    print(k, '->', v)

'''
列表内涵：list content
    通过简单的方法穿件列表
'''
a = [i for i in range(10)]
print(a)
b = [i * 10 for i in a]
print(b)
b = [i for i in a if i % 2 == 0]
print(b)

'''
常用列表函数
len():求列表长度

max():求列表中最大值

min():求列表中最小值

list():将其他格式的数据转换成list
'''