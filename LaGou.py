'''
Title = 拉勾可视化及爬虫
Date = 2019-02-16
'''

import numpy as np
import time
import requests
# 正则表达式
import re
import pandas as pd
import json


# Request_URL = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
# Request_Headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
# 'Accept-Encoding':'gzip, deflate, br',
# 'Accept-Language':'zh-CN,zh;q=0.9',
# 'Connection':'keep-alive',
# 'Content-Length':'26',
# 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
# 'Cookie':'JSESSIONID=ABAAABAAAFCAAEG9993D8F4503D9D975BA37505E78F75B1; _ga=GA1.2.1175355564.1550276200; _gid=GA1.2.1374510635.1550276200; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1550276200; user_trace_token=20190216081639-20fded1b-3180-11e9-8492-525400f775ce; LGUID=20190216081639-20fdf142-3180-11e9-8492-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; SEARCH_ID=b39385b9ec064fa1956b3acd908d4b64; LGRID=20190216081652-2939ae8a-3180-11e9-8492-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1550276214',
# 'Host':'www.lagou.com',
# 'Origin':'https://www.lagou.com',
# 'Referer':'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=',
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
# 'X-Anit-Forge-Code':'0',
# 'X-Anit-Forge-Token':'None',
# 'X-Requested-With':'XMLHttpRequest'}
# Form_Data = {'first': 'false', 'pn': '1', 'kd': 'Python'}
# html = requests.post(url=Request_URL, data=Form_Data, headers=Request_Headers)
# print(html.text)
# #data = re.findall('[{"companyId":.*?,"positionName":"(.*?)","salary":"(.*?)","workYear":"(.*?)","education":"(.*?)","city":"(.*?)","financeStage":"(.*?)","companySize":"(.*?)","district":"(.*?)","companyFullName":"(.*?)","firstType":"(.*?)","secondType":"(.*?)"}]',html.text)
# data = re.findall('"companyId":.*?,"score":.*?,"positionId":.*?,"positionName":"(.*?)","city":"(.*?)","district":(.*?),"companyFullName":"(.*?)","createTime":.*?,"positionAdvantage":.*?,"salary":"(.*?)","workYear":"(.*?)","education":"(.*?)","companyLogo":.*?,"jobNature":.*?,"approve":.*?,"industryField":.*?,"companyShortName":.*?,"financeStage":"(.*?)","companySize":"(.*?)","companyLabelList":.*?,"publisherId":.*?,"positionLables":.*?,"industryLables":.*?,"businessZones":.*?,"adWord":.*?,"formatCreateTime":.*?,"longitude":.*?,"latitude":.*?,"hitags":.*?,"resumeProcessRate":.*?,"resumeProcessDay":.*?,"imState":.*?,"lastLogin":.*?,"explain":.*?,"plus":.*?,"pcShow":.*?,"appShow":.*?,"deliver":.*?,"gradeDescription":.*?,"promotionScoreExplain":.*?,"firstType":.*?,"secondType":.*?,"isSchoolJob":.*?,"subwayline":.*?,"stationname":.*?,"linestaion":.*?,"thirdType":.*?,"skillLables":.*?', html.text)
# Data_Frame = pd.DataFrame(data)
# print(Data_Frame)
# Data_Frame.to_csv(r"C:\Users\李慧源\Documents\LaGouPythonJob.csv",header=False,index=False, mode='a+')
# for n in range(30):
#     # 要提交的数据
#     Form_Data = {'first': 'false', 'pn': str(n), 'kd': 'Python'}
#     time.sleep(np.random.randint(2, 5))
#     # 提交数据
#     html = requests.post(url=Request_URL, data=Form_Data, headers=Request_Headers)
#     # 提取数据
#     data = re.findall(
#         '{"companyFullName":"(.*?)","positionName":"(.*?)","salary":"(.*?)","workYear":"(.*?)","education":"(.*?)","financeStage":"(.*?)"',
#         html.text)
#     # 转换成数据
#     Data_Frame = pd.DataFrame(data)
#     # 保存到本地
#     Data_Frame.to_csv(r"C:\Users\李慧源\Documents\LaGouPythonJob.csv",header=False,index=False, mode='a+')





def get_json(Request_URL, Form_Data):

    Request_Headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '27',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'user_trace_token=20190531102321-432750ec-be16-4df6-b62c-908f85e6c4b4; _ga=GA1.2.364929319.1559269404; LGUID=20190531102323-106f6823-834b-11e9-a180-5254005c3644; index_location_city=%E5%8C%97%E4%BA%AC; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216b9d6db37c2ca-01375d2e54ff7b-e343166-2073600-16b9d6db37d599%22%2C%22%24device_id%22%3A%2216b9d6db37c2ca-01375d2e54ff7b-e343166-2073600-16b9d6db37d599%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; _gid=GA1.2.1940257608.1562245627; JSESSIONID=ABAAABAAAGGABCB770FA83E624930D59EE620C0E90FED38; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1561958794,1561959507,1562245627,1562282045; LGSID=20190705071404-6abd81f3-9eb1-11e9-a4da-5254005c3644; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DHjKn6M_NJEft7ldOWWAPzDkFTyd-8JFs-wOwFlU8B7G%26wd%3D%26eqid%3Dfa9d94e900089d25000000025d1e8838; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=search_code; X_MIDDLE_TOKEN=b86889cdf980bc5b1699ea5207b7df57; X_HTTP_TOKEN=fe1d5dda2ca2c81711038226517769789fc1a3028f; SEARCH_ID=5f64a9ae7ae248a89145067eae0fcb3a; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1562283013; _gat=1; LGRID=20190705073012-ab476661-9eb3-11e9-bd01-525400f775ce',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_python?px=default&city=%E5%85%A8%E5%9B%BD',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest'}

    content = requests.post(url=Request_URL, headers=Request_Headers, data=Form_Data)

    result = content.json()
    info = result["content"]["positionResult"]["result"]
    info_list = []
    for job in info:
        information = []
        information.append(job['positionName'])  # 职位名称
        information.append(job['city'])  # 工作城市
        information.append(job['district'])  # 工作地点
        information.append(job['companyFullName'])  # 公司全名
        information.append(job['salary'])  # 薪水
        information.append(job['workYear'])  # 工作经验
        information.append(job['education'])  # 学位
        information.append(job['financeStage'])  # 融资状态
        information.append(job['companySize'])  # 公司规模
        info_list.append(information)
        # 将列表对象进行json格式的编码转换,其中indent参数设置缩进值为2
        # print(json.dumps(info_list,ensure_ascii=False,indent=2))
        # print(info_list)
    return info_list


def main():

    info_result = []
    title = ['职位名称', '工作城市', '工作地点', '公司全名', '薪水', '工作经验', '学位', '融资状态', '公司规模']
    Request_URL = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
    for n in range(1, 5):
        Form_Data = {
            'first': 'true',
            'pn': n,
            'kd': 'python'
        }
        time.sleep(np.random.randint(2, 10))
        info = get_json(Request_URL, Form_Data)
        info_result = info_result + info
    df = pd.DataFrame(columns=title,data=info_result)
    df.to_csv('H.csv',index=False)

if __name__ == '__main__':
    main()
