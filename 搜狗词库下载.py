import re
import requests

f = open('金融保险类词库.txt','r',encoding='utf-8')  # 这里的文件名写包含（名称：下载地址）的txt文件
a = 1

while a:
    try:
        a = f.readline()
        list = a.split(':',1)
        name,url = list[0],list[1]
        resp = requests.get(url=url)
        name = re.sub('/','_',name)
        file_name = './搜狗词库_部分/' + str(name) + ".scel"
        with open(file_name,'wb') as ff:
            ff.write(resp.content)
    except Exception as e:
        print(a)
        print(e)

f.close()