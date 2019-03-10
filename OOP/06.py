'''
属性案例
创建一个student类，描述学生类
学术具有student.name属性
但name格式并不统一
可以增加一个函数，然后自动调用的方式，但很蠢
'''


class student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.setname(name)

    def into(self):
        print('hi my name is {0},'.format(self.name))

    def setname(self, name):
        self.name = name.upper()


s1 = student('ll', 19)
s2 = student('haha', 20)
s1.into()
s2.into()

print('*' * 50)

'''
property 案例
定义一个person类，具有name age 属性
对于任意输入的姓名，我们希望都用大写方式保存
年龄，我们希望内部统一用整数保存
x = property(fget, fset, fdel, doc)
'''


class person():
    def fget(self):
        return self._name * 2

    def fset(self, name):
        self._name = name.upper()

    def fdel(self):
        self._name = 'NoName'

    name = property(fget, fset, fdel, '对name进行操作')


p1 = person()
p1.name = 'hehe'
print(p1.name)

print('*' * 50)

'''
作业：
    1、 在用户输入年龄的时候，可以输入整数，小数，浮点数
    2、但是内部为了数据清洁，我们统一需要保存整数，直接舍去小数点
'''


class Person():
    '''
    类的说明文档

    '''

    def fget(self):
        return int(self._age)

    def fset(self, age):
        self._age = age

    def fdel(self):
        self._age = 0

    age = property(fget, fset, fdel, '修改年龄')


p2 = Person()
p2.age = 28.9
print(p2.age)

##类的内置函数

print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__bases__)  # 以元组方式存放

print('*'*50)

'''
 魔法函数
'''
class A():
    def __init__(self):
        print('我被调用')
    def __call__(self, *args, **kwargs):
        print('我又被调用了')

    def __str__(self):
        return ' 你好'
a = A()
a()
print(a)

print('*'*50)

'''
__gt__
'''

class B():
    def __init__(self,name):
        self._name = name
    def __gt__(self,obj):
        print('{0} 会比{1}大么'.format(self,obj))
        return self._name>obj._name

    def __str__(self):
        return self._name

b1 = B('one')
b2 = B('two')
print(b1>b2)

