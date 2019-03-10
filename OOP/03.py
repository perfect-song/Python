'''
继承
在Python中，任何类都有一个共同的父类叫object
'''

class Person():
    name = 'noname'
    age = 0
    __score = 0 # 考试分数 私有
    _petname = 'sec' # 小名 是受保护的 子类可以使用，但是不能公用

    def sleep(self):
        print('Sleeping............')
    def work(self):
        print("make some money")

class Teacher(Person):
    #子类定义了与父类同名的变量名称，则优先使用子类本身
    name = 'hahaha'
    def make_test(self):
        print('attention')
    def work(self):
        # Person.work(self)#形式1  父类名.父类成员
        super().work() # 形式2 super().父类成员
        # 扩充父类功能
        self.make_test()



t = Teacher()
print(t.name)
print(Teacher.name)
print(t._petname)#可以访问受保护的？？？

print(id(Person.name))
print(id(Teacher.name))
print(id(t.name))


print(id(Person._petname))
print(id(Teacher._petname))
print(id(t._petname))


print(t.work())

'''
g继承中的构造函数

'''

class Animal():
    def __init__(self):
        print('Animal')
    pass

class puruAni(Animal):
    def __init__(self, name):
        print('puruAni is {0}'.format(name))
    pass

class Dog(puruAni):
    # __init__ 就是构造函数
    # 每次实例化的时候，第一个被自动调用
    # 因为主要工作进行初始化，所以称为构造函数
    def __init__(self):
        print('dog dog dog')

class cat(puruAni):
    pass
## 实例化是自动调用了Dog()中的构造函数
d = Dog()

# 此时应该自动调用构造函数，因为cat没有构造函数，所以查找父类构造函数，在puruAni()中查找到构造函数，则停止向上查找

# 当puruAni() 中的构造函数有name参数时，报错 因为puruAni()的构造函数需要两个参数，实例化的时候给了一个
# c = cat()
c = cat('kit')

print(type(super))
help(super)