#股票爬取
import requests
from bs4 import BeautifulSoup
import traceback
import re
 
def getHTMLText(url,code="utf8"):
    try:
        kv={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'} 
        r = requests.get(url,headers=kv)
        r.raise_for_status()
        print(r.status_code)
        r.encoding =code
        return r.text
    except:
        return ""
 
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser') 
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[S][HZ]\d{6}",href)[0])
            if len(lst)==10:
                print(lst)
                break
            print(lst)
            
        except:
            continue
 
def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock
        html = getHTMLText(url)
        try:
            if html=="":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('article',attrs={'id':'stock_info'})
             
            print(name.string)
            infoDict.update({'股票名称': name.string})
        
            
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
             
            with open(fpath, 'a', encoding='utf-8') as f:
                count=count+1
                f.write( str(infoDict) + '\n' )
                print("xie")
                
                print(count)
                print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
        except:
            count = count + 1
            print("false")
            print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
            continue


def main():
    stock_list_url = 'https://hq.gucheng.com/gpdmylb.html'
    stock_info_url = 'https://hq.gucheng.com/'
    output_file = 'D:/BaiduStockInfo1.txt'
    slist=[]
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)
 
main()
