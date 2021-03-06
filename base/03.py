'''
程序结构
    顺序
    分支
    单分支
        if 条件表达式：
            语义1
            语义2
            语义3
            ......
    双分支
        if 条件表达式：
            语义1
            语义2
            语义3
            ......
        else:
            语句1
            语句2
            语句3
            ......
    多分支
        if 条件表达式：
            语义1
            语义2
            语义3
            ......
        elif:
            语句1
            语句2
            语句3
            ......
        elif:
            语句1
            语句2
            语句3
            ......
        ...
        else:
            语句1
            语句2
            语句3
            ......

        条件表达式就是计算结果必须是布尔值的表达式
        表达式后面的冒号不能少
        注意if后面的出现语句，如果属于if块，则必须同一个缩进等级
        条件表第十三结构为True执行if欧美的缩进的语句块


        if语句可以嵌套使用，但不推荐
        Python没有switch-case语句
    循环
        重复执行某些固定动作或者处理基本固定的事物

        for循环
            for 变量 in 序列:
                语句1
                语句2
                语句3
                ......
        range 左闭右开 （randint是个特例 左右都包含）
            生成一个数字序列
            具体范围可以设定

        for-else语句

        break：无条件结束整个循环
        continue：无条件结束本次循环从新进入下一轮循环
        pass：一般用于站位，没有跳过功能，只是表示这有个东西

'''
'''
input()
1.在屏幕上输出括号内的字符串
2.接受用户输入的内容并返回到程序
3.input返回的内容一定是字符串类型
'''
age = int(input('请输入一个年龄：'))
print('你输入的年龄为: {0}'.format(age))
if age < 18:
    print('小于18')
else:
    print('大于18')


score = int(input("请输入一个分数："))
if score>90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
elif score>=60:
    print('D')
else:
    print('不及格')
