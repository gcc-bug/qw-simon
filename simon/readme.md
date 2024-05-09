# 问题描述
对于一个黑盒函数(black box)或oracle $f:\{0,1\}^n\to \{0,1\}^n$，已知存在一个比特串 $s, s\in {0,1}^n$ 使得对任意 $x,y\in\{0,1\}^n$，当且仅当 $x\oplus y\in \{0^n,s\}$时 $f(x) = f(y)$ 。其中 $\oplus$ 表示异或。问题的目标是使用尽可能少的查询或者调用函数，得到 $s$ 的值。

由于对任意字符串 $a\in {0,1}^n, b\in {0,1}^n$都有 $a\oplus b \oplus b = a$ ， $a\oplus b = b\oplus a$ ，  $a\oplus a = 0$ 成立。
因此 $x \oplus y = 0^n$ ，当且仅当 $x=y$ 时成立。而 $x\oplus y = s$ 时有 $x\oplus s = y$。
因此 
$$
f(x) = f(y) = f(x\oplus s)
$$ 
即函数 $f$ 是周期函数。

> 例子：
> 对以下用真值表表示的函数 $f$ ，  $s$ 是 $010$
> | $x$ | $f(x)$ |
> | :-----| ----: |
> | 000 | 101 | 
> | 001 | 010 | 
> | 010 | 101 | 
> | 011 | 010 | 
> | 100 | 000 | 
> | 101 | 110 | 
> | 110 | 000 | 
> | 111 | 110 | 

# 算法流程

## 量子线路
<!-- //todo: add fig -->
其中 $U_{f}: |x\rangle |y\rangle \to |x\rangle |y\oplus f(x)\rangle$
1. 初始化两个量子寄存器为 $0$, 系统状态为 $|0\rangle ^ n |0\rangle ^ n$ 。
2. 应用Hadmard 门在所有第一个量子寄存器中的量子比特，系统状态变为 $\frac{1}{\sqrt{2^n}}\sum_{k=0}^{2^n - 1}|k\rangle |0\rangle ^ n$ 。
3. 应用 $U_f$ 门，系统状态变为 $\frac{1}{\sqrt{2^n}}\sum_{k=0}^{2^n - 1}|k\rangle |f(k)\rangle ^ n$ 。
4. 应用Hadmard 门在所有第一个量子寄存器中的量子比特，系统状态变为 $\frac{1}{\sqrt{2^n}}\sum_{k=0}^{2^n - 1} [\frac{1}{\sqrt{2^n}}\sum_{j=0}^{2^n - 1} (-1)^ {j\cdot k}| j\rangle] |0\rangle ^ n = \sum_{j=0}^{2^n - 1} | j\rangle [\frac{1}{2^n} \sum^{2^n - 1}_{k=0}(-1)^{j\cdot k} |f(k)\rangle]$ 。
5. 测量第一个量子寄存器的，测量一个状态为 $|j\rangle$ 的概率为 $||\frac{1}{2^n} \sum^{2^n - 1}_{k=0}(-1)^{j\cdot k} |f(k)\rangle||^2$

上述状态中的 $\cdot$ 表示在 $\mathcal{F}_2$ 域上的乘法。对于字符串 $a = (a_1,a_2,\cdots , a_n), b = (b_1,b_2,\cdots , b_n)$ 有：
$$
a\cdot b = (a_1× b_1)\oplus(a_2× b_2)\oplus\cdots\oplus(a_n× b_n)
$$
对量子线路测量时的 $|j\rangle$ 的概率幅分析如下：
- 当 $s = 0^n$ 时， $||\frac{1}{2^n} \sum^{2^n - 1}_{k=0}(-1)^{j\cdot k} |f(k)\rangle||^2 = \frac{1}{2^n}$。
- 当 $s\neq 0^n $时，取 $f(k)=f(k') = y,y\in \{0,1\}^n$，其中 $k\oplus k' = s$ 。因此：
$$
\frac{1}{2^n} \sum^{2^n - 1}_{k=0}(-1)^{j\cdot k} |f(k)\rangle \\
= \frac{1}{2^n} \sum_{z}((-1)^{j\cdot k}+(-1)^{j\cdot k'}) |y\rangle \\
= \frac{1}{2^n} \sum_{z}((-1)^{j\cdot k}+(-1)^{j\cdot (k\oplus s)}) |y\rangle \\
= \frac{1}{2^n} \sum_{z}(-1)^{j\cdot k}(1+(-1)^{j\cdot s}) |y\rangle 
$$
综上，无论 $s=0$ 或 $s\neq0$ 测量结果均是满足 $j\cdot s = 0$ 的状态 $| j \rangle$，概率幅相同。因此测量结果的概率分布是满足 $j\cdot s = 0$ 的均匀分布。

## 经典处理
在对量子线路运行多次后，假设得到一组线性无关的非零字符串 $y_1, y_2,  \dots , y_{N}$ ，排列为矩阵 $A = [y_1, y_2, \dots , y_{N}]$。由于 $y_i \cdot s =0$ 均成立。因此齐次方程 $A^T x = 0$的解就是 $s$ 对应的形式，显然该方程有平凡解 $s=0$，而方程存在非平凡解需要 $r(A^T) < n$。
同时问题中已知 $s$ 的个数为一，
因此需要 $n-1$ 个线性无关的 $y_i$ 。
