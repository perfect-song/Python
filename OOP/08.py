'''
抽象类
'''

import abc

# 声明一个类并且指定当前类的元类
class Human(metaclass=abc.ABCMeta):

    # 定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类抽象方法
    @abc.abstractclassmethod
    def drink(cls):
        pass
    #定义静态抽象方法
    @abc.abstractstaticmethod
    def paly():
        pass

    def sleep(self):
        print('Sleeping......')


'''
函数名可以当变量使用
自己组装类
'''
def sayHello():
    print('Hello world')

sayHello()
s = sayHello##函数名当变量使用
s()

class A():
    pass

def say(self):
    print('Saying......')

A.say = say
a = A()
a.say()

## 使用MethodType组装类

from types import MethodType
class B():
    pass
def sayB(self):
    print('Say... B...')

b = B()

b.say = MethodType(sayB,B)
b.say()

# 使用Type创建类

#首先定义一些成员函数
def A_1(self):
    print('成员函数1')
def A_2(self):
    print('成员函数2')

A = type('Aname',(object,),{'class_def_1':A_1,'class_def_2':A_2})

a = A()
a.class_def_1()
a.class_def_2()

'''
通过元类创建类
元类写法固定，必须继承自type
元类一般命名以MetaClass结尾
'''

class TMeataClass(type):
    def __new__(cls, name, bases, attrs):
        print('哈哈哈，我是元类呀')
        attrs['id'] = '000000'
        attrs['addr'] = '上海宝山区'
        return type.__new__(cls,name,bases,attrs)

class teacher(object,metaclass=TMeataClass):
    pass


t = teacher

print(t.id)
print(t.addr)





