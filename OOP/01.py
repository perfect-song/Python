'''
定义一个学生类 使用来形容学生

'''


# 定义一个类

class Student():
    pass


# 定义一个对象
ll = Student()


# 定义一个学Python的学生类

class PythonStudent():
    name = None
    age = 18
    course = "Python"

    # 注意 函数的缩进的层级 和 系统默认有一个self函数
    def doHomework(self):
        print("I do my homework")
        # 推荐在函数末尾使用return
        return None

# 实例化 一个leilei的学生，是一个具体的人
leilei = PythonStudent()
print(leilei.name)
print(leilei.age)
leilei.doHomework()

print(PythonStudent.__dict__)