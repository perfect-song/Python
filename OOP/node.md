#  OOP python 面向对象
- 面向对象编程:
    - 基础
    - 共有私有
    - 继承
    - 组合
- 魔法函数：
    - 魔法函数概述
    - 构造类魔法函数
    - 运算类魔法函数
    
# 面向对象概述 ObjectOriented OO
- oop思想
    - 接触到任意一个任务，首先想到的是任务这个世界的构成，是由模型构成的
    
- 几个名词
    - OO：面向对象
    - OOA：面向对方的分析
    - OOD：面向对象设计
    - OOI：面向对象的实现
    - OOP：面向对象的编程
    - OOA->OOD->OOI->：面向对象的实现过程

# 类和对象的概念
   - 类：抽象名词，代表一个集合，共性的事物
    - 对象：具象的事物，单个个体
    - 类与对象的关系：
        - 一个具象，代表一类事物的某一个
        - 一个抽象，代表的一大类事物
    - 类中内容，应该具有两个内容
        - 表明事物的特征，叫做属性（变量）
        - 表明事物的功能或者动过，称为成员方法（函数）
 
# 类的基本实现
- 类的命名
    - 遵守变量命名的规则
    - 大驼峰（由一个或多个单词构成，每个单词首字母大写，单词跟单词直接相连）
    - 尽量避开跟系统命名相似的命名
- 如何声明一个类
    - 必须用class 关键字
    - 类由属性和方法构成，其他不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有值，使用None
- 实例化对象
    变量 = 类名() #实例化一个对象
    
- 访问对象成员
    - 使用点操作符
        obj.成员属性名称
        obj.成员方法
- 可以通过默认内置变量检查类和地下的所有成员
    - 对象所有成员检查
        # dict 前后各有两个下划线
        obj.__dict__
    - 类所有成员
        #dict前后各有两个下划线
        class_name.__dict__
    
# 类和对象成员分析
   - 类和对象都可以存储成员，成员可以归类所有，也可以归对象所有
   - 类存储成员时使用的是与类关联的一个对象
   - 对象存储成员时存储在当前对象中
   - 对象访问一个成员时，如果对象中没有该成员，参数访问类中的同名成员, 如果对象中有此成员，移动使用对象中的成员
   - 创建对象的时候，类中的成员不会放入到对象中，而是得到空对象，没有成员
   - 通过对象对类中成员重新赋值或者通过对象添加成员时，对应成员会保存在对象中，而不会修改类成员
# 关于self
   - self在对象方法中表示当前对象本身，如果通过对象调用一个方法，那么该对象会自动转入到当前方法的第一个参数中
   - self 并不是关键字，只是一个用于介绍对象的普通参数，理论上可以使用任何普通变量名代替
   - 方法中self形参的方法称为非绑定类的方法，可以通过对象访问，没有self的是绑定类的方法，只能通过类访问
   - 使用类访问绑定类的方法是，如果类方法中需要访问当前类的成员，可以使用__class__成员名来访问
   
# 面向对象三大特征
   - 封装（https://zhuanlan.zhihu.com/p/36173202   Python中对下划线的介绍）
        - 封装就是对对象的成员进行访问限制
        - 封装的三个级别
            - 公开 public
            - 受保护的 protected
            - 私有的 private 
            - public private protected 不是关键字
        - 判别对象的位置
            - 对象内部
            - 对象外部
            - 子类中
        - 私有
            - 私有程艳是最高级别的封装，只能在当前类或者对象中访问
            - 在成员面前添加两个下划线即可
                    class Person():
                        # name是共有成员
                        name = ''
                        # __age就是私有成员
                        __age = 18
            - Python 的私有不是真私有，是一种成为name mangling 的改名策略， 可以使用对象.__classname__attributename访问
         - 受保护的封装 protected
            - 受保护的封装是将对象成员进行一定级别的封装，然后，在类中或者在子类中都可以进行访问，但是在外部不可以
            - 封装方法：在成员名称前添加一个下划线  
        - 公开的    
            - 公共的封装实际对成员没有任何操作，任何地方都可以访问          
    - 继承
        - 继承就是一个类可以获得另一个类中的成员属性和成员方法
        - 作用： 减少代码，增加代码的复用功能 同时可以设置类与类直接的关系
        - 继承与被继承的概念：
            - 被继承的类叫做父类，也叫基类，也叫超类
            - 用于继承的类，叫做子类，也叫派生类
            - 继承与被继承一定存在is——a的关系
        - 继承的语法 
            class A(B):
                pass
        - 继承的特征
            - 所有的类都继承自object类，即所有的类都是object类的子类
            - 子类一但继承父类，则可以使用父类中除私有变量的所有内容
            - 子类继承父类后并没有将父类成员完全赋值到子类中，而是通过引用关系访问调用
            - 子类中可以定义独有成员属性和方法
            - 子类中定义的成员和父类成员如果相同，则优先使用子类成员
            - 子类如果想扩充父类方法，可以在定义新方法的同时访问父类成员来进行代码重写，可以使用 父类名.父类成员  的格式来调用父类成员，也可以使用 super().父类成员 的格式
         - 继承变量函数的查找顺序问题
            - 优先查找自己的变量
            - 没有则查找父类
            - 构造函数如果本类中没有定义，则自动查找调用父类构造函数
            - 如果本类有定义，则不继续向上查找
            
        - 构造函数
            - 是一个特殊的类，在类进行初始化时 进行调用了
            - 如果定义了构造函数，则实例化时使用自己的构造函数，不查找父类的构造函数
            - 如果子类没有定义构造函数，则自动查找父类构造函数
            - 如果子类没有定义构造函数，父类的构造函数带有参数，则构造对象的参数应该按照父类参数构造
        - super
            - super 不是关键字，而是一个类
            - super 的作用是获取MRO（MethodResolutionOrder） 列表中的第一个类
            - super 与父类没有实质关系，但是可以用个super调用父类
            - super 使用两个方法，参考构造函数中调用父类饭构造函数
            
        - 单继承和多继承
            - 单继承：每个类只能继承一个类
            - 多继承：每个类继承多个类
        - 单继承和多继承的优缺点：
            - 单继承：
                - 优点：传承有序逻辑清晰语法简单隐患少
                - 缺点：功能不能无限扩展，只能在当前唯一的继承链中扩展
            - 多继承：
                - 有点：类的功能扩展方便
                - 缺点：继承关系混乱
        - 菱形继承/砖石继承问题
            - 多个子类继承自同一个父类，这些子类有同一个类继承，浴室继承关系同形成菱形结构 
            - [MRO] http://www.cnblogs.com/whatisfantasy/p/6046991.html 
            - 关于多继承的MRO
                - MRO 就是多继承中，用于保存继承顺序的列表
                - python 本身采用C3算法来来解决多继承中菱形继承问题
                - MRO 列表本身计算原则
                    - 子类永远在父类前面
                    - 如果多个父类，则根据继承语法中括号内类的书写顺序存放
                    - 如果多个类继承了同一个类，孙子类中只会选取继承语法括号中第一个父类的父类
            
   - 多态 多态指的是一类事物的多种形态（一个抽象类由多个子类，因而多态的概念依赖于继承）
        - 多态就是同一个对象在不同的情况下出现
        - 在python中，多态不是语法，是一种设计思想
        - 多态性：一种调用方式，不同执行效果（多态性是指具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数调用不同内容的函数。
        在面向对象方法中一般是这样描述多态性：向不同的对象发送同一消息，不同的对象在接收时会产生不同的行为（即方法）。也就是说，每个对象可以用自己的方式去影响
        共同的消息。所谓消息就是调用函数，不同的行为就是指不同的实现，即执行不同的函数）
        - 多态： 同一事物的动物分为人类，狗类，猪类 https://www.cnblogs.com/luchuangao/p/6739557.html
        
   - Mixin设计模式
        - 主要采用多继承方式对类的功能进行扩展
        - 我们使用多继承语法实现Mixin
        - 使用Mixin实现多继承时候非常小心
            - 首先他必须表示某一单一功能，而不是某一个物品
            - 职责必须单一，如果有多个功能，则写多个Mixin
            - Mixin不能依赖于子类的实现
            - 子类即使没有继承Mixin类，也照样工作，只是缺少某个功能
        - 优点：
            - 使用Mixin可以在不对类进行任何修改的情况下扩充功能
            - 可以方便组织和维护不同功能组件的划分
            - 可以根据需要任意调整类的组合
            - 可以避免创建很多新的类，导致类的继承混乱
# 类相关函数
   - issubclass(A,B):检测A是不是B的子类
   - isinstance(a,A):检测一个对象是否是一个类的实例
   - hasattr():检测一个对象是否有成员
   - getattr():获去成员属性
   - setattr():设置成员属性
   - delattr():删除成员属性
   -dir(): 获取对象成员列表
     
# 类的成员描述符（属性）
   -  类成员描述符是为了在类中对类的成员属性进行相关操作而创建的一种方式
        - get:获取属性操作
        - set: 修改或者添加属性操作
        -delete: 删除属性操作
   - 如果想使用类的成员描述符，大概有三种方式
        - 使用类实现描述器
        - 使用属性修饰符
        - 使用property函数
            - property(fget, fset, fdel, doc)
        
   - 无论哪种修饰符都是为了对成员属性近相应的控制
        - 类的方式：适合多个类中的多个属性公用一个描述符
        - property():适用当前类中使用，可以控制一个类的对个属性
        - 属性修饰符:适用于当前类中使用，控制一个类中的一个属性
        
# 类的内置属性
  - __dict__: 以字典的方式显示类的成员组成
  - __doc__: 获取类的文档信息
  - __name__: 获取类的名称，如果在模板中使用，获取模板的名称
  - __bases__: 获取某个类的所有父类，以元组的方式显示

# 类的常用魔法函数
   - 魔法函数就是不需要人为调用，基本是在特定的时刻自动触发
   - 魔法函数的统一的特征，方法名被前后各两个下划线包裹
   - 操作类
        - __init__: 构造函数
        - __new__: 对象实例化方法，此函数比较特征，一般不需要使用
        - __call__: 对象当函数使用的时候调用
        - __str__:当对象呗当做字符串使用的时候调用
        - __repr__: 返回字符串(注：__repr__与__str__这两个方法都是用于显示的，__str__是面向用户的，打印操作会首先尝试__str__和str内置函数(print运行的内部等价形式
   )，他通常应该返回一个友好的显示；__repr__用于所有其他的环境中)
    - 描述符相关
        - __set__
        - __get__
        - __delete__
    - 属性操作相关
        - __getattr__:访问一个不存在的属性时触发
        - __setattr__:对成员属性进行设置的时候触发
            - 参数: 
                - self用来获取当前对象
                - 被设置的属性名称，以字符串形式出现
                - 需要对属性名称设置的值
            - 作用: 进行属性设置的时候进行验证或者修改
            - 注意: 在该方法中不能对属性直接进行复制操作，否则死循环
            
   - 运算分类相关魔法函数：
        - __gt__: 进行大于判断的时候触发的函数
            - 参数
                - self
                - 第二个参数是第二个对象
                - 返回值是任意值，推荐返回布尔值

# 类和对象的三种方法

   - 实例方法：  
        - 需要实例化对象才能使用的方法，使用过程中可能徐亚截止对象那个的其他方法的完成
   - 静态方法： 使用修饰器 @staticmethod
        - 不需要实例化，通过类直接访问
   - 类方法：使用修饰器 @classmethod
        - 不需要实例化
        
 # 类变量的三种基本用法
   - 赋值
   - 读取
   - 删除
   
# 抽象类
   - 抽象方法： 没有具体实现内容的方法称为抽象方法
   - 抽象方法的主要意义是规划子类的行为和接口
   - 抽象类的使用需要借助abc模块
           import abc
   - 抽象类：包含抽象方法的类叫做抽象类， 通常称为ABC类
   - 抽象类的使用：
        - 抽象类可以包含抽象方法，也可以包含具体方法
        - 抽象类中可以有方法也可以有属性
        - 抽象类不允许直接实例化
        - 必须继承才可以使用，且继承的子类必须实现所有继承来的抽象方法
        - 假如子类没有实现所有继承的抽象类的方法，则子类不能实例化
        - 抽象类的主要作用是设定类的标准，以便开发的时候具有统一规范
        
# 自定义类
   - 类其实是一个类定义和各种方法的自由组合
   - 可以定义类和函数，然后自己通过类直接赋值
   - 可以借助于MethodType实现
   - 借助于type实现
   - 利用元类实现  —— MetaClass
        - 元类是类
        - 
   
   

   