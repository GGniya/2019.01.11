# 列表推导式  是为了简化代码
#     字典推导式 就是[ ]  换成 { }    然后 换一下添加语句

#创建一个列表  存放1-1000的所有偶数

a = []
for i in range(1,10001):
    if i % 2 == 0:
        a.append(i)

#等价于
a = [x for x in range(1,1001) if x % 2 == 0]      #推导式    print(x, y)

a = [('a','a1'),('b','b1')]
for x,y in a:
    print(x, y)


