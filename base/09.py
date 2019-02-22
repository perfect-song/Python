'''
内建函数

元组函数
len(): 获取元组长度
tuple():函数，转化或者创建元组

基本跟list通用
count() 统计数据出现的次数
index() 返回数据的索引位置


元组变量交换法：
a, b = b, a
'''

'''
集合 Set
集合是高中的一个概念
一堆确定无序的唯一数据，集合每一个数据成为一个元素

特征：
    集合内部数据无序，即午安使用索引和分片
    集合内部数据元素具有唯一性，可以用来排出重复说数据
    集合内数据 str、int、float、tuple冰冻集合等，即背部只能放在可哈希的数据
    
集合的内涵
    自动过滤掉重复的元素
    
集合函数/关于集合的函数：
    len()
    max()
    min()
    set():生成一个集合
    add():向集合内添加元素
    clear():原地清空数据
    copy():拷贝
    remove():移除指定的值，直接改变原有的值，如果删除的值不存在，则报错
    discard(): 移除集合中指定的值，跟remove一样，但是如果要删除值不存在不报错
    pop():随机移除一个元素
'''

s = {1, 2, 3, (1, 23), 'hello world'}
print(id(s))
for i in s:
    print(i, end=' ')

print(len(s))
# print(max(s))
s.add('haha')
for i in s:
    print(i, end=' ')

print(id(s))
s.discard(1222)
# s.remove(122222)

'''
集合函数：
    intersection():交集
    difference():差集
    union():并集
    issubset(): 检查一个集合是否是另个的子集
    issuperset():检查一个集合是否是另一个的超集
'''

s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8, 9}
s_1 = s1.intersection(s2)
print(s_1)
s_2 = s1.difference(s2)
print(s_2)
s_3 = s1.union(s2)
print(s_3)

print(s2 - s1)
# print(s2 + s1) 不支持加号+

'''
frozen set:冰冻集合
    冰冻集合就是不可以进行人格修改集合
    frozenset是一种特殊的集合
'''
s = frozenset()
print(type(s))

print('*'*50)
'''
dict 字典
    字典是一种组合数据，没有顺序的组合数据，数据以键值对的形式出现
    

'''
#字典创建
#创建空字典 形式1
d1 = {}

#创建空字典 形式2
d2 = dict()

# 创建有值的字典 每一组数据用冒号个烤，每一对键值对用逗号隔开
d3 = {'one':1,'two':2,'three':3}
print(d3)

#用dict创建有内容的字典 形式1
d4 = dict({'one':1,'two':2,'three':3})
print(d4)
#  用dict创建有内容的字典 形式2
d5 = dict(one=1,two=2,three=3)
print(d5)
#  用dict创建有内容的字典 形式3
d6 = dict([("one",1),("two",2),("three",3)])
print(d6)

'''
字典特征：
    字典是序列类型，但是是无序序列，所以没有分片和索引
    字典中数据每个都是键值对组成
        key:必须是可哈希的值，比如int string float tuple 但是list  set dict 不行
        value:任何值
'''

# 字典常用操作
print("*"*50)
#访问数据
print(d3['one'])

'''
删除使用del

成员检测 in 、 not in 
    只检测key
'''
print(d3)
del d3['one']
print(d3)

if 2 in d3:
    print('value')
if 'two' in d3:
    print('key')
if ('two',2) in d3:
    print('key_value')

#for循环直接用key开访问字典
for k in d4:
    print(k,d4[k])

for k in d4.keys():
    print(k,d4[k])

for v in d4.values():
    print(v)

for k,v in d4.items():
    print(k,'---',v)
'''


'''
#字典生成式

dd1 = { k:v for k,v in d4.items()}

# 加限制条件的字典生成式
dd2 = {k:v for k,v in d4.items() if v%2==0}


print(dd1)
print(dd2)

'''
字典相关函数
    len()
    max()
    min()
    dict()
    str()返回字典的字符串格式
    clear(): 清空字典
    items(): 返回字典键值对组成的元组格式
    key(): 返回字典的键组成的一个可迭代的结构
    value(): 返回字典的值组成的结构 可迭代的
    get():根据指定键返回相应导致，好处是可以设置默认值 如果key存在返回value值，如果不存在返回默认值，不设置默认值时，默认值为None
    fromkeys:使用指定的序列作为键，，使用一个值作为字典的所有键的值
'''
print('*'*50)
print(str(dd1))

i = dd1.items()
print(i)
print(type(i))

k = dd1.keys()
print(k)
print(type(k))

v = dd1.values()
print(v)
print(type(v))


print(dd1.get('one',1010))
print(dd1.get('four'))#默认为None
print(dd1.get('four',4))#设置默认值为4
#注意fromkeys()两个参数
#注意fromkeys()的调用主体
l = ['one','two','three']
d = dict.fromkeys(l,100)
print(d)