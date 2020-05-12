def nth_power(exponent):
    print("exponent" + str(exponent))

    def exponent_of(base):
        print("base" + str(base))
        return base ** exponent

    return exponent_of  # 返回值是exponent_of函数


square = nth_power(2)  # 计算一个数的平方
cube = nth_power(3)  # 计算一个数的立方
# 输出
print(square)
# 输出
print(cube)

print(square(2))  # 计算2的平方
print(cube(2))  # 计算2的立方
