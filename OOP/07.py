'''
三种实例方法案例
'''

class person():
    # 实例方法

    def eat(self):
        print(self)
        print('Eating...')

    # 类方法 第一个参数一般命名为cls 区别于self
    @classmethod
    def play(cls):
        print(cls)
        print('Playing...')

    # 静态方法 不需要用第一个惨呼表示自身或者类
    @staticmethod
    def say():
        print('Saying....')


yy = person()
## 实例方法
yy.eat()

## 类方法
person.play()
#也可以
yy.play()
##静态方法
person.say()
yy.say()
