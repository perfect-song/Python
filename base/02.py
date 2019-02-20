'''
表达式
    用一个或者几个数字或者变量和运算符组合成一行代码
    通常糊返回一个结果

运算符：
    有一个以上值经过变化得到更新值的过程就叫做运算
    用于运算的符号叫运算符
    运算符类型：
        算数运算符 + - * /
        比较或者关系运算符
        赋值运算符
        逻辑运算符 python 中没有异或运算
            and 逻辑与
            or 逻辑或
            not 逻辑非

            逻辑运算的短路问题：逻辑运算式，按照运算顺序计算，一旦确定整个式子未来的值，则不再进行计算，直接返回
        位运算
        成员运行
            用来检测某一个变量是否在另一个变量的成员
            in
            not in
        身份运算
            用来检测两个变量是否是同一个变量
            is: var1 is var2
            is not

            a = 9
            b = 9
            print(a is b) -------True
            a = 'hello'
            b = 'hello'
            print(a is b) -------False??????
'''
a = 9
b = 9
print(a is b)
a = "I love wangxiaojing"
b = "I love wangxiaojing"
print(a is b)