# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:35:39 2019

@author: 14771
"""

#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134
#Cookie: tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zfvmw%2Fq5hkYtwHp2MYN%2F8n40r0cdtGzn%2BOQKS%2BUMkS3AfR0NUAsWPTUUty5Guje86sv6Toa2Nf8GFMetkf5%2FmKgoq5j0MbTw9n%2Fi9pBFQNTHnskp9y2VcJC9ZMVAsr38MfiRPCjskSe9t7CSWt9gmhH16x%2FaswxUZSaixOBaQ1zOcMcvGB9%2FBtxAzru7UENrm%2FviUenlQPZS78uy05nfwyYo4adA00sNyR1jbuKEqZT1%2FvSYQghRxeUebZ30R8acqR; cookie2=1c4dab5f579ac14f1d2e184f3ac46994; _tb_token_=eaee03be13a8b; v=0; uc1=cookie14=UoTZ7YMZHOWTMQ%3D%3D&lng=zh_CN&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&existShop=false&cookie21=UtASsssme%2BBq&tag=8&cookie15=UtASsssmOIJ0bQ%3D%3D&pas=0; skt=41a0e25f6fe269c3; csg=22a30cb0; existShop=MTU1OTk3NTAxNQ%3D%3D; dnk=%5Cu5FAE%5Cu7B11%5Cu4E36%5Cu63A9%5Cu76D6%5Cu60B2%5Cu4F24s62; whl=-1%260%260%261559980308308; enc=ZcbdF9Zv%2FKD38008Abyr2Yyi8Cl37Jctf4ndi0beZPMrRJ%2FRcOJZszeI9YeXeoQ6eC8JPR7AleuwEKZyonHjGQ%3D%3D; _cc_=UtASsssmfA%3D%3D; isg=BEFBu1up-Wsk7hVfQIC6dw0aSY1bbrVgGPO0P6Odpsv5im1c57yGMD3MbD5pmU2Y; thw=cn; uc3=vt3=F8dBy3jfC35T1tn1YGw%3D&id2=UNDVc87RrNJVIA%3D%3D&nk2=rTulWbK7mFsrh3Vi2%2Ba0r5o%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; t=0d6557db7ab5c97c165e11f586d7d87e; _m_h5_tk_enc=c7e84809c81892b8f2f78d8c1b848390; miid=372776381738407132; mt=ci=67_1; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; lgc=%5Cu5FAE%5Cu7B11%5Cu4E36%5Cu63A9%5Cu76D6%5Cu60B2%5Cu4F24s62; cna=WMVnFdGehxkCAbfbmF2h27Cw; _m_h5_tk=a8732680b997e6e50178cdb9535f7de7_1559982413151; tracknick=%5Cu5FAE%5Cu7B11%5Cu4E36%5Cu63A9%5Cu76D6%5Cu60B2%5Cu4F24s62; l=bBQAsJs4vqd02gT8BOfBhurza77T0LpTzkPzaNbMiIB1OUfaCdImZHwdq35WL3Q6E_fa3EtP7GcUvd3p5aUdg; tg=0; hng=CN%7Czh-CN%7CCNY%7C156

import requests
import re

def getHTMLText(url):
    try:
        headers = {
                'Cookie':'cookie2=1440f88debacf28806aafd56557a5bde; v=0; _tb_token_=73e71738e74eb; uc1=cookie14=UoTaGOnwtSIZBg%3D%3D; enc=ZcbdF9Zv%2FKD38008Abyr2Yyi8Cl37Jctf4ndi0beZPMrRJ%2FRcOJZszeI9YeXeoQ6eC8JPR7AleuwEKZyonHjGQ%3D%3D; _cc_=UtASsssmfA%3D%3D; isg=BIeH7vuhl-NyGhNpGmKEyTfYDztRjFtucnEyqVl0EJY9yKeKYV7pvlfGakgzOzPm; thw=cn; uc3=vt3=F8dBy3jfC35T1tn1YGw%3D&id2=UNDVc87RrNJVIA%3D%3D&nk2=rTulWbK7mFsrh3Vi2%2Ba0r5o%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; t=0d6557db7ab5c97c165e11f586d7d87e; _m_h5_tk_enc=d15eb30aa4302fa4501c354816ba9502; miid=372776381738407132; mt=ci=67_1; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; lgc=%5Cu5FAE%5Cu7B11%5Cu4E36%5Cu63A9%5Cu76D6%5Cu60B2%5Cu4F24s62; cna=WMVnFdGehxkCAbfbmF2h27Cw; _m_h5_tk=d80ce7888f865ddda0a1118811e09728_1559997801528; tracknick=%5Cu5FAE%5Cu7B11%5Cu4E36%5Cu63A9%5Cu76D6%5Cu60B2%5Cu4F24s62; l=bBQAsJs4vqd02EYaBOfClurza779eIJT4kPzaNbMiICP_u165HdfWZTIbbYBC31Vw15yR37NjXrLBeYBq1f..; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; ucn=center; ubn=p'
                }
        r = requests.get(url,headers = headers,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("")
    
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList =[]
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)
        
main()