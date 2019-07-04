import xml.etree.ElementTree as et
import pandas as pd
import os
import shutil
import tkinter.messagebox
import time
import sys
import fnmatch
import subprocess
import tkinter
from tkinter import filedialog
import traceback
import re

# 获取<Cablink>节点下的光模块信息
def cablink():
    # 创建表的字段名
    name_field_Cablink = ['Link Type', 'Link Speed', 'BER', 'LCV']
    # 构造DataFrame结构
    df_Cablink = pd.DataFrame(columns=name_field_Cablink)
    # 在根节点下遍历查找所有<Cablink>
    for cablink in root.findall('Cablink'):
        # 获取节点<Cablink>下的元素对应的字段内容
        linkType = cablink.find('_linkType').text
        linkSpeed = cablink.find('_linkSpeed').text
        ber = cablink.find('_ber').text
        lcv = cablink.find('_lcv').text
        # 由Series构造一维数组，每次循环追加到DataFrame结构中
        df_Cablink = df_Cablink.append(
            pd.Series([linkType, linkSpeed, ber, lcv], index=name_field_Cablink), ignore_index=True)
        # 按照需求追加两次
        df_Cablink = df_Cablink.append(
            pd.Series([linkType, linkSpeed, ber, lcv], index=name_field_Cablink), ignore_index=True)
    df_Cablink.drop(labels=['Link Type'], axis=1, inplace=False)
    df_Cablink.insert(0, 'SFP', sfp()['SFP'])
    return df_Cablink


# 获取<SFP>节点下的光模块信息
def sfp():
    # 创建表的字段名
    name_field_SFP = ['SFP', 'Vendor', 'Serial Number', 'SFP Type', 'Wave Length', 'Transmission Mode',
                      'Transmission Rate', 'Transmission Distance', 'Tx Power High Alarm Threshold',
                      'Tx Power Low Alarm Threshold', 'Tx Power High Warning Threshold',
                      'Tx Power Low Warning Threshold', 'Rx Power High Alarm Threshold', 'Rx Power Low Alarm Threshold',
                      'Rx Power High Warning Threshold', 'Rx Power Low Warning Threshold',
                      'Temperature High Alarm Threshold', 'Temperature Low Alarm Threshold', 'Module Temperature',
                      'Transceiver Tx Supply Voltage', 'Transceiver Tx Bias Current', 'Transceiver Tx Power',
                      'Transceiver Rx Optical Power']
    # 构造一个DataFrame结构
    df_SFP = pd.DataFrame(columns=name_field_SFP)
    # 在根节点下遍历查找所有<SFP>节点
    for sfp in root.findall('SFP'):
        # 获取指定字段的元素内容
        physicalPort = sfp.find('_distname').text.split('/')[-2] + '/' + sfp.find('_physicalPort').text + '/' + \
                       sfp.find('_distname').text.split('/')[-1]
        sfpVendor = sfp.find('_sfpVendor').text
        sfpSerialNumber = sfp.find('_sfpSerialNumber').text
        sfpType = sfp.find('_sfpType').text
        waveLength = sfp.find('_waveLength').text
        transmissionMode = sfp.find('_transmissionMode').text
        transmissionRate = sfp.find('_transmissionRate').text
        transmissionDistance = sfp.find('_transmissionDistance').text
        txPwrHiAlmThreshold = sfp.find('_txPwrHiAlmThreshold').text
        txPwrLoAlmThreshold = sfp.find('_txPwrLoAlmThreshold').text
        txPwrHiWarnThreshold = sfp.find('_txPwrHiWarnThreshold').text
        txPwrLoWarnThreshold = sfp.find('_txPwrLoWarnThreshold').text
        rxPwrHiAlmThreshold = sfp.find('_rxPwrHiAlmThreshold').text
        rxPwrLoAlmThreshold = sfp.find('_rxPwrLoAlmThreshold').text
        rxPwrHiWarnThreshold = sfp.find('_rxPwrHiWarnThreshold').text
        rxPwrLoWarnThreshold = sfp.find('_rxPwrLoWarnThreshold').text
        tempHiAlmThreshold = sfp.find('_tempHiAlmThreshold').text
        tempLoAlmThreshold = sfp.find('_tempLoAlmThreshold').text
        temperature = sfp.find('_temperature').text
        txVoltage = sfp.find('_txVoltage').text
        txCurrent = sfp.find('_txCurrent').text
        txPower = sfp.find('_txPower').text
        rxPower = sfp.find('_rxPower').text
        # 由Series构造一维数组，每次循环追加到DataFrame中
        df_SFP = df_SFP.append(pd.Series(
            [physicalPort, sfpVendor, sfpSerialNumber, sfpType, waveLength, transmissionMode, transmissionRate,
             transmissionDistance, txPwrHiAlmThreshold, txPwrLoAlmThreshold, txPwrHiWarnThreshold, txPwrLoWarnThreshold,
             rxPwrHiAlmThreshold, rxPwrLoAlmThreshold, rxPwrHiWarnThreshold, rxPwrLoWarnThreshold, tempHiAlmThreshold,
             tempLoAlmThreshold, temperature, txVoltage, txCurrent, txPower, rxPower], index=name_field_SFP),
            ignore_index=True)
    return df_SFP


# 获取整条光纤链路的DataFrame数据
def link():
    name_field_link = ['Optical Link']
    df_link = pd.DataFrame(columns=name_field_link)
    for i in range(len(sfp()) // 2):
        for n in range(2):
            df_link = df_link.append(
                pd.Series([sfp().iloc[2 * i]['SFP'] + ' - ' + sfp().iloc[2 * i + 1]['SFP']],
                          index=name_field_link), ignore_index=True)
    return df_link


# 获取基站ID
def enbid():
    # 创建表的字段名
    name_field_enbid = ['eNB ID']
    # 构造DataFrame结构
    df_enbid = pd.DataFrame(columns=name_field_enbid)
    # 在根节点下遍历查找所有<Cablink>
    for cablink in root.findall('Cablink'):
        # 获取节点<Cablink>下的元素对应的字段内容
        enbid = cablink.find('_endPoint1').text.split('/')[0].split('-')[1]
        # 由Series构造一维数组，每次循环追加到DataFrame结构中
        df_enbid = df_enbid.append(
            pd.Series([enbid], index=name_field_enbid), ignore_index=True)
        # 按照需求追加两次
        df_enbid = df_enbid.append(
            pd.Series([enbid], index=name_field_enbid), ignore_index=True)
    return df_enbid


# 获取基站IP
def enbip(n):
    name_field_enbip = ['eNB IP']
    df_enbip = pd.DataFrame(columns=name_field_enbip)
    if n == 1:
        for sfp in root.findall('SFP'):
            enbip1 = files[0].split('_')[1]
            df_enbip = df_enbip.append(pd.Series([enbip1], index=name_field_enbip), ignore_index=True)
    else:
        for sfp in root.findall('SFP'):
            enbip = files[i].split('_')[1]
            df_enbip = df_enbip.append(pd.Series([enbip], index=name_field_enbip), ignore_index=True)
    return df_enbip


if __name__ == '__main__':

    try:
        # 指定存放提取到的xml文件路径
        path = 'D:/SFPxml/'
        # 预先清空路径下的xml文件
        for f in os.listdir(path):
            if re.search('.xml', f):
                os.remove(os.path.join(path, f))
        # 获取主窗口
        root1 = tkinter.Tk()
        root1.withdraw()
        root1.update()
        tkinter.messagebox.showinfo('提示', 'Please select \\BTS Site Manager\\tools\\CLI path')
        cmd_dir = filedialog.askdirectory()
        # 提取SFPxml文件
        # os.chdir('C:\\Program Files (x86)\\NSN\\Managers\\BTS Site\\BTS Site Manager\\tools\\CLI')
        os.chdir(cmd_dir)
        cmd = 'sfpmonitor.bat -ipfile addresses.txt -pw Nemuadmin:nemuuser -xml -outdir D:\SFPxml'
        p = subprocess.Popen(args=cmd)
        p.wait()
        # 自动存放生成的csv文件
        if not os.path.isdir('D:/SFPcsv/'):
            os.makedirs('D:/SFPcsv/')
        # 自动存放备份文件
        if not os.path.isdir('D:/SFPBackup/'):
            os.makedirs('D:/SFPBackup/')
        # 清除存在的union.csv以防追加错误
        if os.path.exists('D:/SFPBackup/union.csv'):
            os.remove('D:/SFPBackup/union.csv')
        # 获取路径下的xml文件列表
        files = fnmatch.filter(os.listdir(path), '*.xml')
        # 留出带有表头的第一张csv表
        root = et.parse(path + files[0]).getroot()
        df = pd.concat([enbip(1), enbid(), link(), cablink(), sfp().drop('SFP', axis=1)], axis=1)
        df.to_csv('D:/SFPcsv/' + files[0].split('xml')[0] + 'csv')
        reader = pd.read_csv('D:/SFPcsv/' + files[0].split('xml')[0] + 'csv', index_col=0)
        reader.to_csv('D:/SFPBackup/union.csv', index=None, header=True, mode='a')
        shutil.copy(path + files[0], 'D:/SFPBackup')
        # 清空处理过的xml文件
        os.remove(path + files[0])
        # 清除生成的csv表
        os.remove('D:/SFPcsv/' + files[0].split('xml')[0] + 'csv')
        # 遍历文件列表
        for i in range(1, len(files)):
            # 批量解析xml文件
            parsed_xml = et.parse(os.path.join(path, files[i]))
            # 获取根节点
            root = parsed_xml.getroot()
            # 整合所有分表
            df = pd.concat([enbip(2), enbid(), link(), cablink(), sfp().drop('SFP', axis=1)], axis=1)
            # 将DataFrame依次保存成.csv文件输出到D:\SFPcsv\
            df.to_csv('D:/SFPcsv/' + files[i].split('xml')[0] + 'csv', )
            # 将多张无表头的csv表合并
            reader = pd.read_csv('D:/SFPcsv/' + files[i].split('xml')[0] + 'csv', index_col=0)
            reader.to_csv('D:/SFPBackup/union.csv', index=None, header=False, mode='a')
            # 备份提取到的xml文件
            shutil.copy(os.path.join(path, files[i]), 'D:/SFPBackup')
            # 清空处理过的xml文件
            os.remove(path + files[i])
            # 清除每个csv分表
            os.remove('D:/SFPcsv/' + files[i].split('xml')[0] + 'csv')
        # 获取时间戳
        timeStamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        # 备份合并后的csv文件
        shutil.copy('D:/SFPBackup/union.csv', 'D:/SFPcsv/Union' + timeStamp + '.csv')
        # 清空备份过的csv文件
        os.remove('D:/SFPBackup/union.csv')
        # 完成时提示对话框
        tkinter.messagebox.showinfo('提示', '      Completed successfully!\n\nPlease click OK to exit program.')
        # 无错误退出
        sys.exit(0)
    except Exception :
        tkinter.messagebox.showinfo('异常', traceback.format_exc())