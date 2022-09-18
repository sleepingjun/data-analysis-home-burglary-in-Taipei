Recently, I have been trying to tidy up my past project, and then I will write a document to record.  
I did this project 3-4 years age, and used excel to analyze; however, I lost my file. Therefore, I decide to rewrite it and use pycharm.  
Thoughts: After finishing rewriting this project, I think using Excel or JupyterNotebook could be more convenient than using pycharm, when the dataset is not too big to open.  
我最近都在整理過去在學時期做的小程式或是小專案，然後把它們加上說明後放上來，做為過去學習的見證跟紀錄。  
現在這個專案是我大學時上通識學Excel VBA的時候做的，當時報告要求從抓檔案、錄製巨集、分析結果並說明都要自己來。但奇妙的是，檔案都不見了，也許他就在我第N次消失的隨身碟裡面吧...  
對於當時的報告，我只記得是使用政府公開資料庫中的檔案，然後分析的資料集是有關偷竊紀錄的。因此，我決定重新抓資料，並試著改用python來實作。  
實作完後，我真的深刻感受到，有些其實沒那麼大的資料，還是用Excel做吧，好呈現還方便看。另一方面，我使用的是pycharm，如果是要使用python且要即時呈現資料分析結果的話，其實我更推薦用Colab或是JupyterNotebook。有的人會說要用R來做，但我R的語法都還給老師了，全部忘光光XD  

## Context  
* [Introduction](#introduction)  
* [Target](#target)  
* [Start](#start)  


## Introduction  
This project is to analyze the [dataset](https://data.gov.tw/dataset/130312) named 臺北市住宅竊盜點位資訊 from Taiwan government opendata platform.  
此專案旨在分析台灣政府公開資料平台提供的台北市住宅竊盜點位資訊。  

## Target  
**What I want to know?**  
Q. Which administrative area is more peaceful/dangerous than others. (find top3)  
A. Safe: Datong(大同), Nangang(南港), Wenshan(文山); Dangerous: Zhongshan(中山), Shilin(士林), Wanhua(萬華)  
Explanation: Acoording to these figures below, I found that house burglary cases in Datong are less than other areas, and those in Zhongshan are more. I was taken aback, when I knew that Zhongshan is the most dangerous district. Since there are many delicious dessert shops:cry:.  Maybe the next step I can do further analysis on it.  
解釋: 根據以下圖表，我發現大同區的住宅竊盜案件少於其他區，而中山區的多於其他區。當我得知中山區是案件最多的區域實，我其實蠻驚訝的。因為中山區有好多好吃的甜點店，難道是要偷蛋糕嗎?(開玩笑的) 下一步我也許可以針對這部分做進一步的分析。  
![line](https://github.com/sleepingjun/data-analysis-home-burglary-in-Taipei/blob/main/line_admin_area_count.png)
![pie](https://github.com/sleepingjun/data-analysis-home-burglary-in-Taipei/blob/main/pie_admin_area_percentage.png)  
Q. Whether Public Security improves every year?  
A. Yes.   
Q. Whether Public Security is influenced by month? (maybe it's too cold/hot to steal XD)  
A. No.  
Q. Whether Public Security is influenced by date?  
A. Yes. Cases in 1 and 15 are more than other days. I suppose that is due to payday, because most of Taiwanses people's payday is in the beginning or middle of month.  
對中山、士林、萬華區做時間段分析後，我很高興看到住宅竊盜的案件有逐年下降的趨勢，這代表了治安越來越好了。而以月份來看，其實案件數量都蠻平均的，但我發現1月的數字特別高，讓我不得不想，是不是因為過年時間大約都在國曆1月中到2月中的時候。而以日期來看，我發現每月1號跟15號的案件數都會比較多，我猜是因為台灣發薪日都是月初跟月中。  
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
![UTF8更改方式](https://github.com/sleepingjun/data-analysis-home-burglary-in-Taipei/blob/main/UTF-8%E6%A0%BC%E5%BC%8F.JPG)  
3. See code in `main.py` and write by yourself. My suggest is to use JupyterNotebook when you need to check table and fig anytime.  
