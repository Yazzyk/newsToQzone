# coding:utf-8
import requests
import time
import platform
import json
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

mySystem = 'System:' + platform.uname().system + platform.uname().release + '\nDevice:' + platform.uname().node + '\n'


def news():
    re = requests.get('https://36kr.com/api/newsflash')  # 更换api接口
    getJson = json.loads(re.text)
    datalist = getJson.get('data')
    return datalist


info = '新闻api更换为36氪测试\n'+mySystem + 'auto-sent from selenium on ' + platform.uname().node + '\n新闻推送：\n'
count = 0  # 计算一下收到多少个新闻

# print(news()['items'][0]['title'])
for need_info in news()['items']:
    need_news = need_info['title'] + ':' + need_info['news_url'] + '\n发表时间：' + need_info['created_at']
    count += 1
    info += need_news + '\n'


def Qzone(info):
    qq = ''
    qq_pwd = ''
    print("starting")
    browser = webdriver.PhantomJS()
    print("browser binded to PhantomJS")
    browser.get('https://qzone.qq.com')
    print("browser.get started")
    browser.switch_to.frame('login_frame')
    print("switched to login frame")
    browser.find_element_by_id('switcher_plogin').click()
    print("clicked Switch button")
    browser.find_element_by_id('u').clear()
    print("User field clear")
    browser.find_element_by_id('u').send_keys(qq)
    print("User field set")
    browser.find_element_by_id('p').clear()
    print("Passwd clear")
    browser.find_element_by_id('p').send_keys(qq_pwd)
    print("Passwd set")
    browser.find_element_by_id('login_button').click()
    print("Login button clicked")
    time.sleep(5)
    browser.find_element_by_id('aIcenter').click()
    time.sleep(5)
    print("we are in " + browser.title)
    print("wait 10s to complete loading page")
    time.sleep(10)
    if (browser.find_element_by_id('$1_content_content').get_attribute('innerHTML') == ""):
        print("trying to click substitutor")
        browser.find_element_by_id('$1_substitutor_content').click()
        print("clicked. Now substitutor_content not displayed and content_content displayed")
        time.sleep(3)
    else:
        print("content is previously set. trying to click it")
        browser.find_element_by_id('$1_content_content').click()
        print("clicked")
        time.sleep(2)
        print("trying to clear it")
        browser.find_element_by_id('$1_content_content').clear()
        print("and now it is cleared")
        time.sleep(2)
    browser.find_element_by_id('$1_content_content').click()
    print("content clicked")
    time.sleep(2)
    print("trying to modify content")
    browser.find_element_by_id('$1_content_content').send_keys(info + '--Coded by BlankYk')
    print("tried")
    time.sleep(3)
    print("content is now --* " + browser.find_element_by_id('$1_content_content').get_attribute('innerHTML') + " *--")
    time.sleep(3)
    print("trying to CTRL+Enter to send")
    browser.find_element_by_id('$1_content_content').send_keys(Keys.CONTROL, Keys.ENTER)
    print("it should have been sent")
    time.sleep(3)

    print("Done!!!")
    browser.quit()


print('共{}个新闻'.format(count))

Qzone(info)
