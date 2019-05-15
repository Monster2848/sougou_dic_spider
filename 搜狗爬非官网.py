import re
from bs4 import BeautifulSoup
import lxml
from lxml import etree
import requests


for page in range(1,1212):
    url = 'http://wubi.sogou.com/dict/list.php?page={}'.format(page)
    resp = requests.get(url)

    try:
        content = resp.content.decode('gbk')
    except Exception as e :
        print(e)
        continue

    try:
        content = re.search('(<div class="boxmain5" style="padding:0 15px;">.*)<div class="boxbtm5">',content,re.DOTALL).group(1)

        soup = BeautifulSoup(content,'lxml')
        aaa = soup.select(".dictbox")
        for ele in aaa:
            url = ele.select("a")[0].get("href")
            name =ele.select("a")[2].get_text()
            txt_content = name + ':' + url + '\n'
            with open('词库地址全.txt','a',encoding='utf-8') as f:
                f.writelines(txt_content)
    except Exception as e:
        print(e)


