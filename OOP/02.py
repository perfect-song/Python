'''
类实例的属性和其对象的实例的属性在不同对象的实例属相赋值前提下指向同一个变量

'''
class A():
    name = 'dada'
    age = 18
    pass
print(A.name)
print(A.age)
print(id(A.name))
print(id(A.age))
print(A.__dict__)

print('*'*20)

a = A()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print(a.__dict__)

print('*'*20)

a.name = 'll'
a.age = 16

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print(a.__dict__)

class student():
    name = 'leilei'
    age = 18
    def say(self):
        # self.name = 'lulu'
        # self.age = '24'
        print("my name is {0}".format(self.name))
        print('my age is {0}'.format(self.age))

print(student.name)
print(student.age)
s = student()
s.say()
print(s.name)
print(s.age)
print(student.name)
print(student.age)
print('*'*20)
class Teacher():
    name = 'da'
    age = 20
    def say(self):
        self.name = 'yang'
        self.age = 24
        print("my name is {0}".format(self.name))
        print('my age is {0}'.format(self.age))
    def sayagain():
        print(__class__.name)##访问类成员变量
        print('hello world')

t = Teacher()
t.say()
# Teacher.say()
Teacher.sayagain()

print('*'*20)

class A():
    name = 'hehe'
    age = 15
    def __init__(self):
        self.name = 'haha'
        self.age = 16
    def say(self):
        print(self.name)
        print(self.age)
class B():
    name = 'lele'
    age = 18

a = A()
#此时系统默认把a作为第一个参数传入函数
a.say()

# A.say() 报错，因为没有传入参数，系统不会把A作为参数传入
A.say(a) #把a作为参数传入

A.say(A)#同样把A作为参数传入

A.say(B)#此时，传入的是类实例B，因为B具有name和age属性所以不会报错


'''
Python的私有通过改名字
'''

class Person():
    name = 'll'
    __age = 18

p = Person()
print(p.name)
# print(p.__age)
print(Person.__dict__)
print(p._Person__age)# 可以访问了