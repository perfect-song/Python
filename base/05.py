'''
函数作用域
    变量由作用范围限制

分类：
    全局(global)：在函数外部定义
    局部(local)：在函数内部定义
变量的作用范围：
    全局变量：在整个全局范围都有效（函数内部或者外部都可以使用）
    局部变量：在局部可以使用（即函数内部可以）

原则：LEGB原则
    L（local）：局部作用域
    E（Enclosing function local）外部嵌套函数作用域
    G（global module）函数定义所在的模块作用域
    B（Building）python内置函数的作用域



提升局部变量为全局变量
    使用global



globals locals函数

可以通过globals和locals函数显示出全局变量和局部变量
'''

a1 = 100  # 全局


def fun():
    print(a1)
    print('I in func')
    global a2
    a2 = 99  # 局部
    print(a2)


print(a1)

fun()

print('*' * 20)
print(a2)

print('*' * 20)

a = 1
b = 2


def fun(c, d):
    e = 3
    print('loacl={}'.format(locals()))
    print('global={}'.format(globals()))


fun(2, 3)

'''
eval()函数
    把一个字符串当成一个表达式来执行，返回表达式执行后的结果
    eval(string_code,globals=None,locals=None)

exec()函数
    跟eval()功能类似，但是不返回结果
    exec(string_code,globals=None,locals=None)
'''
x = 100
y = 200
z1 = x + y
z2 = eval('x+y')
z3 = exec('x+y')
# print(z1)
# print(z2)
# print(z3)
exec("print('x+y=',x+y)")

'''
递归函数
    函数直接或者间接调用本身
    优点：
        简洁，容易理解
    缺点：
        对递归深度限制，消耗资源大
        python对递归深度游限制，超出限制会报错
        在写递归的时候一定要注意结束条件
'''
x = 0


def func():
    global x
    x += 1
    print(x)
    # func()


func()

'''
斐波那契数列
1, 1, 2, 3, 5, 8, 13, .......

'''
def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(3))
print(fib(10))
