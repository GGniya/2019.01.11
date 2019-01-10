f = open("python.csv",encoding= "gbk")
lines = f.readlines()
f.close()
print(lines)

# city_info = {
#     '北京' : {}
# }

city_info = {}

for line in lines:
    line = line.strip()              #去除特殊字符
    city = line.split('","')[2]     #切割
    # print(line)
#     publish = line.split('","')[6].strip('"')        #去除特殊字符
#
#     if city not in city_info:
#         # continue               #结束
#         city_info[city] = {}     #字典嵌套字典
#     print(city,publish)
#     if publish in city_info[city]:
#         city_info[city][publish] += 1
#     else:
#         city_info[city][publish] = 1
# print(city_info)
# from pyecharts import Line
# columns = list(city_info['上海'].keys())
# columns2 = list(city_info['北京'].keys())
# data1 = list(city_info['上海'].values())
# data2 = list(city_info['北京'].values())
# line = Line("折线图", "每日工作数量趋势")
# # is_label_show是设置上方数据是否显示
# line.add("北京", columns2, data2, is_label_show=True)
# line.add("上海", columns2, data2, is_label_show=True)
# # line.add("北京", columns, data1, is_label_show=True,is_more_utils=True)
# # line.add("上海", columns, data1, is_label_show=True,is_more_utils=True)      #  is_more_utils=True  更多工具
#
# line.render("折线图.html")