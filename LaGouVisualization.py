import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyecharts import Geo
import wheel
import pyecharts_snapshot
#figure图中配置matplotlib加入中文字体
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False
data = pd.read_csv(r'C:\Users\ASUS\Documents\LaGouPythonJob.csv',encoding='utf-8',header =None,sep='/t')
#统计数据出现的频率或总数，创建水平条形图
data['学位'].value_counts().plot(kind='barh',rot=0,subplots=True)
print(data['学位'].value_counts())
#创建直方图
data['工作经验'].value_counts().plot(kind='bar',rot=0,color='y',subplots=True)#rot是将字体旋转
#统计所有不同工作城市的总数
total_cities = data['工作城市'].value_counts().size
#创建饼图，保留各工作城市所占百分比的小数点后两位，使在0~1之间按总块数平均分隔炸裂开
data['工作城市'].value_counts().plot(kind='pie',autopct='%1.2f%%',explode=np.linspace(0,1,total_cities),subplots=True)
data2 = list(map(lambda x:(data['工作城市'][x],eval(re.split('k|k',data['薪水'][x])[0])*1000),range(len(data))))
city_salary_table = pd.DataFrame(data2)
salary_mean = list(map(lambda x:(city_salary_table.groupby(0).mean()[1].index[x],city_salary_table.groupby(0).mean()[1].values[x]),range(len(city_salary_table.groupby(0)))))
#热力图
geo = Geo("中国Python工资分布热力图","制作人：The-ignorant",title_text_size=20,subtitle_text_size=14,subtitle_color="#F00",title_color="#F00",title_pos="center",width=1366,height=768,background_color='#090031')
attr,value = geo.cast(salary_mean)
geo.add("",attr,value,type="heatmap",is_visualmap=True,maptype="china",visual_range=[0,1000],border_color='#166ABB',geo_normal_color='#15115e',geo_emphasis_color='#090031',visual_text_color='#fff')
geo.render("中国Python工资分布热力图.html")
#效应散点图
geo = Geo("中国Python工资分布散点图","制作人：The-ignorant",title_text_size=20,subtitle_text_size=14,subtitle_color="#F00",title_color="#F00",title_pos="center",width=1366,height=768,background_color='#090031')
attr,value = geo.cast(salary_mean)
geo.add("",attr,value,type="effectScatter",maptype="china",border_color='#166ABB',geo_normal_color='#15115e',geo_emphasis_color='#090031')
geo.render("中国Python工资分布散点图.html")

