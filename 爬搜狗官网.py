import requests
from lxml import etree
base_url = 'https://pinyin.sogou.com/dict/cate/index/80/default/{}'

for i in range(1,6):
    url = base_url.format(i)
    print(url)
    resp = requests.get(url=url)
    eroot = etree.HTML(resp.text)
    element = eroot.xpath('//*[@id="dict_detail_list"]/div')
    elements = eroot.xpath('//*[@id="dict_detail_list"]/div/div[1]/div/a')
    elements2 = eroot.xpath('//*[@id="dict_detail_list"]/div/div[2]/div[2]/a')
    for ele in element:
        name = ele.xpath('./div[1]/div/a/text()')
        dic_url = ele.xpath('./div[2]/div[2]/a/@href')

        if name and dic_url:
            txt_line = name[0]+':'+dic_url[0]+'\n'
            with open('金融保险词库.txt','a',encoding='utf-8') as f:
                f.writelines(txt_line)

