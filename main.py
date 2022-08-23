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
total=int(len(data))


def split_date(data,date_col):
    """
    to split date into year, month, day list
    :param data: dataframe
    :param date_col: str
    :return: list
    """
    year=[]
    month=[]
    day=[]
    for i in data[date_col]:
        year.append(str(i)[:-4])
        month.append(str(i)[-4:-2])
        day.append(str(i)[-2:])
        #print(f'year: {year} month: {month} day: {day}')
    return year,month,day
year,month,day=split_date(data,"發生日期")
data.insert(5,column="year",value=year)
data.insert(6,column="month",value=month)
data.insert(7,column="day",value=day)

# split administrative areas
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

    return dict((key,d[key]) for key in sorted(d.keys()))


#analysis time, all
dict_y=build_dict(year)
dict_m=build_dict(month)
dict_d=build_dict(day)

fig, ax = plt.subplots(3,1)

ax[0].plot([i for i in dict_y.keys()],
           [i for i in dict_y.values()],
           '.-',
           label="year")
ax[0].legend()
ax[1].bar(dict_m.keys(),
          dict_m.values(),
          alpha=0.5,
          label="month")
ax[1].legend()
ax[2].bar(dict_d.keys(),
          dict_d.values(),
          alpha=0.5,
          label="date")
ax[2].legend()
plt.close()


# analysis administrative area
dict_a=build_dict(admin_area)
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

#I wanna do further analysis on Zhongshan dist.
print("dangerous part")
zs_data=data.loc[(data["administrative area"]=="中山區")]
sl_data=data.loc[(data["administrative area"]=="士林區")]
wh_data=data.loc[(data["administrative area"]=="萬華區")]

zs_year,zs_month,zs_day=split_date(zs_data,"發生日期")
zs_year,zs_month,zs_day=split_date(zs_data,"發生日期")
zs_year,zs_month,zs_day=split_date(zs_data,"發生日期")

sl_year,sl_month,sl_day=split_date(sl_data,"發生日期")
sl_year,sl_month,sl_day=split_date(sl_data,"發生日期")
sl_year,sl_month,sl_day=split_date(sl_data,"發生日期")

wh_year,wh_month,wh_day=split_date(wh_data,"發生日期")
wh_year,wh_month,wh_day=split_date(wh_data,"發生日期")
wh_year,wh_month,zs_day=split_date(wh_data,"發生日期")

sl_dict_y=build_dict(sl_year)
sl_dict_m=build_dict(sl_month)
sl_dict_d=build_dict(sl_day)

zs_dict_y=build_dict(zs_year)
zs_dict_m=build_dict(zs_month)
zs_dict_d=build_dict(zs_day)

wh_dict_y=build_dict(wh_year)
wh_dict_m=build_dict(wh_month)
wh_dict_d=build_dict(wh_day)

fig, ax = plt.subplots(3,1)

ax[0].plot([i for i in zs_dict_y.keys()],
           [i for i in zs_dict_y.values()],
           '.-',
           label="Zhong Shan")
ax[0].plot([i for i in sl_dict_y.keys()],
           [i for i in sl_dict_y.values()],
           '.-',
           label="Shi Lin")
ax[0].plot([i for i in wh_dict_y.keys()],
           [i for i in wh_dict_y.values()],
           '.-',
           label="Wan Hua")
ax[0].legend(prop={'size': 6})
ax[0].set_xlabel("year")
ax[1].plot([i for i in zs_dict_m.keys()],
           [i for i in zs_dict_m.values()],
           '.-',
           label="Zhong Shan")
ax[1].plot([i for i in sl_dict_m.keys()],
           [i for i in sl_dict_m.values()],
           '.-',
           label="Shi Lin")
ax[1].plot([i for i in wh_dict_m.keys()],
           [i for i in wh_dict_m.values()],
           '.-',
           label="Wan Hua")
ax[1].legend(prop={'size': 6})
ax[1].set_xlabel("month")
ax[2].bar(zs_dict_d.keys(),
           zs_dict_d.values(),
           alpha=0.5,
           label="Zhong Shan")
ax[2].plot([i for i in sl_dict_d.keys()],
           [i for i in sl_dict_d.values()],
           '.-',
           label="Shi Lin")
ax[2].plot([i for i in wh_dict_d.keys()],
           [i for i in wh_dict_d.values()],
           '.-',
           label="Wan Hua")
ax[2].legend(prop={'size': 6})
ax[2].set_xlabel("day")
plt.tight_layout()
plt.show()