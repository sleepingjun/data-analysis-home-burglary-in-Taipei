import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

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

#analysis time


# analysis administrative area
total=int(len(data))
house_burglary_amount = [i for i in dict_a.values()]
area_name = [i for i in dict_a.keys()]
target=data["administrative area"]
plt.plot(area_name,
         house_burglary_amount,
         '-.bo',
         label="house_burglary_count")
for i,j in zip(data["編號"],house_burglary_amount):
    plt.text(i-1,j+0.5,
             str(j),
             ha='center',va='bottom',
             fontsize=15)
plt.legend()
plt.title("House Burglary Cases Count in Taipei City")
plt.xticks(rotation=45)
plt.close()

fig, ax =plt.subplots(figsize=(6,3))

def num_to_percent(num,gross=total):
    """
    number invert to percentage
    :param num: part num
    :param gross: total num
    :return: float
    """
    absolute = int(np.round(num/100.*(gross)))
    return absolute
house_burglary_per=[]
for i in house_burglary_amount:
    house_burglary_per.append(num_to_percent(i))
wedges, texts, autotexts = ax.pie(house_burglary_per,
                                  labels=area_name,
                                  autopct='%1.1f%%'
                                  )

ax.legend(wedges, area_name,
          title="Area",
          loc="center",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Administrative Area Percentage of House Burglary\nTotal: "+str(len(data)))
plt.close()