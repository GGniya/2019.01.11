from pyecharts import Pie
f = open("python.csv",encoding= "gbk")
lines = f.readlines()
f.close()


for line in lines:
    line = line.strip()              #去除特殊字符
    city = line.split('","')[2]     #切割
    # print(city)

# 统计个数
#方案1:字典                  能统计 但是不能排序
    city_info = {}
    if city in city_info:
        city_info[city] += 1
    else:
        city_info[city] = 1
    # print(city_info)
#方案2:  利用包                       能统计个数 / 排序 /前多少个
    from collections import Counter
    city_list = []                      #  给一个空列表
    city_list.append(city)
    result = Counter(city_list)
    city_info = result.most_common(20)
    city_info = {city: count for city, count in city_info}
    # print(city_info)


    columns = city_info.keys()
    data1 = city_info.values()
    pie = Pie("饼状图", "python在各城市工作数量", title_pos='center', width=900)
    pie.add("工作数量", columns, data1, center=[75, 50], is_legend_show=False, is_label_show=True)
    pie.render("饼状图.html")

