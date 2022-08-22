import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False


data=pd.read_csv(os.path.join(os.getcwd(),'taipei_house_steal.csv'),encoding='utf-8')
data=pd.DataFrame(data)
print(data.info())#colum information, count, dtype, memory usage
print("data.index: ",data.index)
print("data.col: ",data.columns)


year=[]
month=[]
day=[]
for i in data["發生日期"]:
    year.append(str(i)[:-4])
    month.append(str(i)[-4:-2])
    day.append(str(i)[-2:])
    #print(f'year: {year} month: {month} day: {day}')

data.insert(5,column="year",value=year)
data.insert(6,column="month",value=month)
data.insert(7,column="day",value=day)


admin_area=[]

for i in data["發生地點"]:
    admin_area.append(str(i)[3:6])

data.insert(8,column="administrative area",value=admin_area)
print(data.head(3))


def build_dict(col):
    """
    :param col: list
    :return: dict
    to build dict to count list
    """
    d=dict()
    for i in col:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
dict_y=build_dict(year)
dict_m=build_dict(month)
dict_d=build_dict(day)
dict_a=build_dict(admin_area)

print(data.head(3))
target=data["administrative area"]
plt.plot([i for i in dict_a.keys()],[i for i in dict_a.values()],label="admin_area")
plt.legend()
plt.show()
