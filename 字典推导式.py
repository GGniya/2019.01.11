list = [('name','zhangsan'),('age',20),('address','郑州')]


dict = {}
for key , value in list:
    dict[key] = value

dict = {key: value for key, value in list}
print(dict)



