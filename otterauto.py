# -*- coding: utf-8 -*-

from selenium import webdriver
import os
import sys
import csv
from time import sleep
chromedriver = os.path.join(sys.path[0],'chromedriver.exe')
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome()
url ="http://10.240.10.67:8085/login.htm"
allstophref=[]

if len(sys.argv[1])==0:
    print('输入stop/start')
with open(os.path.join(sys.path[0],'channellist.txt'),'r',encoding='utf-8') as list_file:
    #write = csv.writer(csv_file)
    #write.writerow(['标题','播放次数','连接'])
        browser.get(url)
        sleep(3)
        user = browser.find_element_by_name("_fm.l._0.n")
        user.send_keys('admin')
        sleep(1)
        password = browser.find_element_by_name("_fm.l._0.p")
        password.send_keys('otter67')
        sleep(1)
        #button = browser.find_element_by_class_name('login_btn right').find_element_by_tag_name('a')
        browser.execute_script('document.login.submit()')
        if sys.argv[1] == 'stop':
            for line in list_file.readlines():
                channelname=browser.find_element_by_class_name('search_o').find_element_by_name('searchKey')
                channelname.send_keys(line)
                sleep(1)
                browser.execute_script('document.search_channel.submit()')
                tablerows = browser.find_element_by_class_name('changecolor_w').find_elements_by_tag_name('tr')
                for tablerow in tablerows:
                    tableherf=tablerow
                    if tablerow.text.split(' ')[1] == line.replace('\n','') and tablerow.text.split(' ')[2] == '运行':
                        stophref=tableherf.find_elements_by_tag_name('td')[4].find_elements_by_tag_name('a')[1].get_attribute('href')
                        allstophref.append(stophref.split("'")[-2])
                        print('需要关闭的channel==> '+line.replace('\n',''))
        if sys.argv[1] == 'start':
            for line in list_file.readlines():
                channelname=browser.find_element_by_class_name('search_o').find_element_by_name('searchKey')
                channelname.send_keys(line)
                sleep(1)
                browser.execute_script('document.search_channel.submit()')
                tablerows = browser.find_element_by_class_name('changecolor_w').find_elements_by_tag_name('tr')
                for tablerow in tablerows:
                    tableherf=tablerow
                    if tablerow.text.split(' ')[1] == line.replace('\n','') and tablerow.text.split(' ')[2] == '停止':
                        stophref=tableherf.find_elements_by_tag_name('td')[4].find_elements_by_tag_name('a')[1].get_attribute('href')
                        allstophref.append(stophref.split("'")[-2])
                        print('需要打开的channel==>' + line.replace('\n', ''))
        for singlestophref in allstophref:
            browser.get(singlestophref)
        print('已经打开/关闭上述channel')




# @Time    : 2019/1/17 9:10
# @Auth    : DAQIUYIN
# @File    : otterauto.py
# @SoftWare: PyCharm Community Edition