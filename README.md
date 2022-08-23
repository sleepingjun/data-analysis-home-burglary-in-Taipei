Recently, I have been trying to tidy up my past project, and then I will write a document to record.  
I did this project 3-4 years age, and used excel to analyze; however, I lost my file. Therefore, I decide to rewrite it and use pycharm.  

## Context  
* [Introduction](#introduction)  
* [Target](#target)  
* [Start](#start)  


## Introduction  
This project is to analyze the [dataset](https://data.gov.tw/dataset/130312) named 臺北市住宅竊盜點位資訊 from Taiwan government opendata platform.  

## Target  
**What I want to know?**  
Q. Which administrative area is more peaceful/dangerous than others. (find top3)  
A. Safe: Datong(大同), Nangang(南港), Wenshan(文山); Dangerous: Zhongshan(中山), Shilin(士林), Wanhua(萬華)  
Explanation: Acoording to these figures below, I found that house burglary cases in Datong are less than other areas, and those in Zhongshan are more. I was taken aback, when I knew that Zhongshan is the most dangerous district. Since there are many delicious dessert shops:cry:.  Maybe the next step I can do further analysis on it.  
![line](https://github.com/sleepingjun/data-analysis-home-burglary-in-Taipei/blob/main/line_admin_area_count.png)
![pie](https://github.com/sleepingjun/data-analysis-home-burglary-in-Taipei/blob/main/pie_admin_area_percentage.png)  
Q. Whether Public Security improves every year?  
A. Yes.   
Q. Whether Public Security is influenced by month? (maybe it's too cold/hot to steal XD)  
A. No.  
Q. Whether Public Security is influenced by date?  
A. Yes. Cases in 1 and 15 are more than other days. I suppose that is due to payday, because most of Taiwanses people's payday is in the beginning or middle of month.  
![y-m-d](https://github.com/sleepingjun/data-analysis-home-burglary-in-Taipei/blob/main/y_m_d_analysis.png)  

(Extra). I want to know more about the top3 dangerous districts, Zhongshan(中山), Shilin(士林),and Wanhua(萬華)  
![dangerous](https://github.com/sleepingjun/data-analysis-home-burglary-in-Taipei/blob/main/dangerous_district_time_analysis.png)  
I found that the count of cases in Wan Hua and Zhong Shan are the same, so I used histgram to show cases in Zhong Shan.  

## Start  
If you want to start this projet with me, you can do following steps:  
1. Install envirnment using requirements.txt, or do it yourself.  
**quick start** `import -r requirements.txt`  


2. Download taipei_house_steal.csv here or go to [opendata platform](https://data.gov.tw/dataset/130312)  
**Notice**: if you want to download open dataset yourself, please note that you need to transfer format to **UTF-8** or you won't be able to open file in python.
3. See code in `main.py` and write by yourself. My suggest is to use JupyterNotebook when you need to check table and fig anytime.  
