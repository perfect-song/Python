'''
__mro__返回家族谱
'''

class A():
    pass
class B(A):
    pass

print(A.__mro__)
print(B.__mro__)

'''
单继承与多继承
'''

class fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print('swimming')
class bird():
    def __init__(self,name):
        self.name = name
    def fly(self):
        print('I can fly')
class person():
    def __init__(self,name):
        self.name = name
    def work(self):
        print('working')
class superman(person,fish,bird):#多继承
    def __init__(self,name):
        self.namr = name
class student(person):##单继承
    def __init__(self,name):
        self.name = name
s = superman('yeye')
s.fly()
s.swim()
s.work()