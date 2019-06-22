# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:13:40 2019

@author: 14771
"""

import requests
from openpyxl import Workbook  #写入excel用到的包
from bs4 import BeautifulSoup
import re
import time
#import traceback

def getHTMLText(url,code = 'utf-8'):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
    except:
        print('')
    return r.text

def getStockList(lst,stockURL):
    html = getHTMLText(stockURL,'GB2312')
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])
        except:
            continue

def getStockInfo(lst,stockURL):
    time_start=time.time()
    star_num = 4500
    index = star_num

    wb = Workbook()    # 将数据写入Excel
    dest_filename = 'stockInfo.xlsx'
    ws = wb.active     # 新建一个sheet
    titleList = ['序号','股票代码', '股票名称', '发行时间']    # 设置表头
    ws.append(titleList)
    
    # 打印.txt表头
    #tplt = "{:4}\t{:8}\t{:16}\t{:32}"
    #with open(fpath,'a',encoding = 'utf-8') as f:
        #f.write(tplt.format("序号","股票名称","股票代码","发行时间") + '\n')
    
    for stock in lst[star_num : len(lst)-1]:
        url = stockURL + stock + ".html"
        html = getHTMLText(url,'GB2312')
        #html = html.encode("iso-8859-1").decode('gbk').encode('utf-8')
        try:
            if html == "":
                continue
            
            soup = BeautifulSoup(html,'html.parser')
            listTimeText = soup.find(attrs={'class':'pb3'})
            
            # 创建字典
            #infoDict = {}
            #infoDict.update({'序号':index})
            #infoDict.update({'股票代码':lst[index]})
            #infoDict.update({'股票名称':soup.find(id='name').text})
            #infoDict.update({'发行时间':re.findall(r'\d+\-\d+\-\d+',listTimeText.text)[0]})
            
            # 将每条数据写入列表
            stock_code = lst[index]
            stock_name = soup.find(id='name').text
            release_time = re.findall(r'\d+\-\d+\-\d+',listTimeText.text)[0]
            row = [index, stock_name, stock_code, release_time]
            ws.append(row)
            #setSQLData.append(row)
            
            index = index + 1
            time_end=time.time()
            print('\r已输出：{:.2f}%\t耗时：：{:.2f} s'.format((index-star_num+1)*100/(len(lst)-star_num),time_end-time_start),end = '')
            
            # 写入.txt文件
            #with open(fpath,'a',encoding = 'utf-8') as f:
                #f.write(str(infoDict['序号']) + '\t' + str(infoDict['股票代码']) + '\t\t' + str(infoDict['股票名称']) + '\t\t' + str(infoDict['发行时间']) + '\n')
                
        except:
            #traceback.print_exc()
            continue
    wb.save(filename=dest_filename)

def main():
    stock_list_url = 'http://quote.eastmoney.com/stock_list.html'
    stock_info_url = 'http://quote.eastmoney.com/'
    #output_file = 'E:/Python/code/stockInfo.txt'
    slist = []
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url)
    
main()