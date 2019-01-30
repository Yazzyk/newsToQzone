#coding:utf-8
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import platform
import json

mySystem = 'System:' + platform.uname().system + platform.uname().release + '\n设备名:' + platform.uname().node+'\n'

def news():
    re = requests.get('https://www.apiopen.top/journalismApi')
    getJson = json.loads(re.content)
    datalist = getJson.get('data')
    return datalist

info = 'auto-sent from selenium on RaspberryPi\n今日新闻：\n'
count = 0

for tech in news()['tech']:
    tech_news = tech['title']+':'+tech['link']+'\n发表时间：'+tech['ptime']
    count+=1
    info+=tech_news+'\n'
# for auto in news()['auto']:
#     auto_news = auto['title']+':'+auto['link']+'\t发表时间：'+auto['ptime']
#     count += 1
#     info+=auto_news+'\n'
# for money in news()['money']:
#     money_news = money['title']+':'+money['link']+'\t发表时间：'+money['ptime']
#     count += 1
#     info+=money_news+'\n'
# for sports in news()['sports']:
#     sports_news = sports['title']+':'+sports['link']+'\t发表时间：'+sports['ptime']
#     count += 1
#     info+=sports_news+'\n'
# for dy in news()['dy']:
#     dy_news = dy['title']+':'+dy['link']+'\t发表时间：'+dy['ptime']
#     count += 1
#     info+=dy_news+'\n'
# for war in news()['war']:
#     war_news = war['title']+':'+war['link']+'\t发表时间：'+war['ptime']
#     count += 1
#     info+=war_news+'\n'
for toutiao in news()['toutiao']:
    toutiao_news = toutiao['title']+':'+toutiao['link']+'\t发表时间：'+toutiao['ptime']
    count += 1
    info+=toutiao_news+'\n'
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
    print("we are in "+ browser.title)
    print("wait 20s to complete loading page")
    time.sleep(20)
    #browser.find_element_by_xpath("//div[@id='QM_Mood_Poster_Inner']/div/div[4]/div[4]/a[2]/span").click()
    #print("send clicked")
    #print("input substitutor is now --* "+browser.find_element_by_id('$1_substitutor_content').get_attribute('innerHTML')+" *--")
    if(browser.find_element_by_id('$1_content_content').get_attribute('innerHTML')==""):
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
    #print("content now is now --* "+browser.find_element_by_id('$1_content_content').get_attribute('innerHTML')+" *--")
    #print("trying to click content")
    #time.sleep(1)
    browser.find_element_by_id('$1_content_content').click()
    print("content clicked")
    time.sleep(2)
    print("trying to modify content")
    #browser.find_element_by_id('$1_content_content').clear()
    browser.find_element_by_id('$1_content_content').send_keys(info+mySystem+'--Coded by BlankYk')
    print("tried")
    browser.find_element_by_xpath('//a[starts-with(@title,"同步至QQ签名")]').click()
    time.sleep(3)
    print("content is now --* "+browser.find_element_by_id('$1_content_content').get_attribute('innerHTML')+" *--")
    time.sleep(3)
    print("trying to CTRL+Enter to send")
    browser.find_element_by_id('$1_content_content').send_keys(Keys.CONTROL,Keys.ENTER)
    print("it should have been sent")
    time.sleep(3)

    print("Done!!!")
    browser.quit()

print('共{}个新闻'.format(count))

Qzone(info)

