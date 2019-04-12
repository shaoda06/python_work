def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


num_0 = int(input("Num1: "))
num_1 = int(input("Num2: "))

gcd = gcd(num_0, num_1)
print("%d 和 %d的最大公约数为： " % (num_0, num_1), gcd)
print("%d 和 %d的比例为： %d:%d" % (num_0, num_1, num_0/gcd, num_1/gcd))

