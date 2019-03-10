# 动态规划
- 什么是动态规划
    - 动态规划算法通常指基于一个递推公式及衣蛾或者多个初始状态，当前子问题的解将由上次子问题的解推出。
    - 使用动态规划来解题只需要多项式时间复杂度，因此他比回溯法、暴力法等要快很多
 
# 动态规划的本质，是对状态的定义以及状态转移方程的定义
 - 什么是状态？
    - 状态是用来描述该问题的子问题的解
- 什么是状态转移方程
    - 状态与状态之间的关系式    
# 例子1
- 问题：如果我们有面值为1元、3元、5元的硬币若干，如何使用最小的硬币凑够11元呢？
- 状态定义：d(i)表示凑够i元需要最少的硬币数量
-解答：
    - 当i=0时，我们需要0个硬币 即d(0)=0
    - 当i=1时，只有面值为1的硬币可用，我们需要一枚1元硬币，即d(1)=1
    - 当i=2时，仍然只有面值为1的可用，我们需要两枚1元硬币，即d(2)=2
    - 当i=3时，1元和3元都可以使用，两种其情况，第一种，使用1元，d_1(3)=d(3-1)+1=d(2)+1=3
    第二种，使用3元硬币，d_2(3)=d(3-3)+1=d(0)+1=1,最后选择，d(3)=min{d_1(3),d_2(3)}=d_2(3)=1
    这样的方程就称为状态转移方程
    - 后面依次类推
    - 代码见 01.py
- 总结 
    - 我们首先考虑能用的面值是多少，然后依据面值的不同取不同情况下的最小值
    - 比如i下a,b c 面值可用
    d(i)=min{d(i-a)+1,d(i-b)+1,d(i-c)+1}——状态转移方程

 
# 例子2
- 更加复杂的问题， 如何找到状态之间的转移方式（状态转移方程），因此引入递推关系来将状态联系起来

- 问题： 一个序列有N个数：A[1],A[2],A[3]......A[N]，求出最长非降子序列长度（LIS——longest increasing subsequence问题 ）
- 状态定义：我们沿用刚才例题的思想一步步找到状态和状态转移方程。假如我们考虑求A[1],A[2]...A[i]的最长非降子序列的长度，其中
i<N,那么上面的问题变成原问题的一个子问题了，然后我们定义状态d(i)表示前i个数中以A[i]结尾的最长非降子序列的长度。所以如果我们把
d(1)到d(N)都计算出来，那么我们最终找的就是这里面最大的那个
- 解答：
    - 计算d(i)， 如果j<i and A[i]=>A[j],则d(i)=max{1,d(j)+1}
    - 计算从d(0),d(1)....d(N),最大的就是d(N)的值
    -代码见 02.py    
- 总结：
    - 复杂度为O(n^2)
