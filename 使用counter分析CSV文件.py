from collections import Counter
f = open("python.csv", encoding="gbk")
lines = f.readlines()
f.close()

city_list = []

for line in lines:
    line = line.strip()
    city = line.split('","')[2]
    city_list.append(city)

result = Counter(city_list)
city_info = result.most_common(20)
city_info = {city:count for city,count in city_info}

from pyecharts import Pie
columns = city_info.keys()
data1 = city_info.values()
pie = Pie("饼状图", "python在各城市工作数量", title_pos='center', width=900)
pie.add("工作数量", columns, data1, center=[75, 50], is_legend_show=False, is_label_show=True)
pie.render("饼状图.html")