#母牛数量问题
# https://blog.csdn.net/qq_34342154/article/details/77104452
""""
【基本思路】
　　原问题。O(2^N)的方法。斐波那契数列为１，１，２，３，５，８……，也就是除第一项和第二项以外，对于第N项，有F(N) = F(N-1) + f(N-2)，于是可以很轻松的写出暴力递归的代码。下面是使用python3.5实现的代码：
""""
# 递归求解
def fibonacci3(n):
    if n < 1 :
        return 0
    if n == 1 or n == 2 or n == 3:
        return n
    return fibonacci3(n-1) + fibonacci3(n-3)

# ＃动态规划
def fibonacci4(n):
    if n < 1:
        return 0
    if n == 1 or n == 2 or n == 3:
        return 3
    prepre = 1
    pre = 2
    cur = 3
    for i in range(4, n+1):
        tmp = cur
        cur = prepre + cur
        prepre = pre
        pre = tmp
    return cur

def fibonacciUseMatrix2(n):
    def matrixPower(m, p):
        res = [[1 if i == j else 0 for i in range(len(m[0]))] for j in range(len(m))]
        tmp = m
        while p > 0:
            if p & 1 != 0:
                res = muliMatrix(res, tmp)
            tmp = muliMatrix(tmp, tmp)
            p >>= 1
        return res

    def muliMatrix(m1, m2):
        res = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    res[i][j] += m1[i][k] * m2[k][j]
        return res

    if n < 1:
        return 0
    if n == 1 or n ==2 or n == 3:
        return n
    base = [[1,1,0], [0,0,1], [1,0,0]]
    res = matrixPower(base, n-3)
    return 3 * res[0][0] + 2 * res[1][0] + res[2][0]

print("---------------fibonacci3-----------------")
print(fibonacci3(10))

print("---------------fibonacci4-----------------")
print(fibonacci4(10))