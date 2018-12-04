#求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
#以n=100为例
# 1.使用递归
def Sum_Solution( n):
    if n == 1:
        return 1
    return Sum_Solution(n - 1) + n

print(Sum_Solution(100))

# 2.使用求和函数
s = sum(list(range(1,101)))
