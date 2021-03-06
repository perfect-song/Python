##注释
#行注释：以#开头，可以单独行也可以多行
#块注释：好几行代码或者内容，以三个连续单引号或者双引号开始和结束，中间任何内容机器都忽略
'''
块注释
'''

##变量

'''
命名规则：可以包含数字、大小写字母、下划线或者更多（但是不推荐）， 一般使用前三种
数字不开头
一般下划线开头的具有特殊意义，不建议使用
区分大小写

保留字和关键字：class def break for(命名避开)
'''


import keyword
print(keyword.kwlist)


'''
变量申明 赋值：

var_name = var_value
var1 = var2 = var3 = var_value
var1, var2, var3 = var1_value, var2_value, var3_value
'''

'''
变量类型

严格意义上python只有一个类型

标准类型六种：
数字：（没有大小限制）
    整数（二进制（0b开头，0b01101）、八进制(0o开头)、十进制、十六进制（0x开头））
    浮点数：小数
        科学计数法e/E后面表示10的指数，0.876 = 8.76e-1
    复数
    布尔值：True（1）/False（0）
字符串：
    用来表示一串文字信息
    表示：
        单引号
        双引号
        三引号
    单引号和双引号交错使用
    
    转义字符
        用一个特殊的方法表示出一系列不太方便写出的内容，比如回车键、换行键、退格键
        借助反斜杠字符，一旦字符串中出现反斜杠，则反斜杠后面的一个或者几个字符表示已经不死原来的意思了，进行了转义    (\\表示\，\n表示换行（win下），\r\n换行（linux）)
    格式化
        利用百分号（%）
            在字符串中出现%表示一个特殊的含义，表示对字符进行格式化
            %d：此处应该放入一个整数
            %s：表示此处应该放一个字符串 
            如果出现多个占位符，则相应内容需要用括号括起来
        
        利用format函数
            直接用format函数进行格式化
            推荐使用format
            在使用上，以{}代替%号，后面用format带参数完成
        
    None:
        表示什么都没有
        如果函数没有返回值，可以返回None
        用来占位置
        用来解除变量绑定
            
    
    内建函数
    
列表
元组
字典
集合
'''

s = "helle \n world"
print(s)

print("helle %s"%"world")
print('I an %d years old'%23)

s1 = 'I am %s, I am %d years old'
print(s1%('zhangsan', 24))


s2 = 'I am {0}, I am {1} years old.'
print(s2.format('zhangsan', 24))


