content = "\nhello woeld  >    \t  \n"

# content = content.replace()     #适用于去除字符里面的有的

content = content.strip()       #适合去除两端的特殊东西
# strip :默认可以去除字符串两端的换行/空格/tab等特殊字符
content = content.lstrip()        #去除左端的
content = content.rstrip()        #去除右端的

content = content.strip("<>")     #单独指定去除特殊字符

print(content)