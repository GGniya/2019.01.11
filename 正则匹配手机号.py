# 1 必须11位
# 2 以 135 135 187 *** 开头
import re
phone = '13598792356'

pattern = re.compile(r"^(135|136|138|187)\d{8}$")

pattern = re.compile(r"^1[35687]\d{9}$")


# pattern = re.compile(r"^\d{11}$")     #表示以数字开头且结尾的11位数字
 ##  ^  (shift+6)     表示 以xxx开头
 ##  $  (shift+4)     表示以xxx结尾



result = pattern.findall(phone)
if result:
    print("手机号")
else:
    print("不是手机号")