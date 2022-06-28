#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 21:57:56 2021

@author: cui_hao
"""
# 转发网络 
import pandas as pd
import os
import random
import requests
from bs4 import BeautifulSoup
import re
import time

#below is a demo
cwd = '/Users/cui_hao/Documents/GitHub/Emergence_Popularity_Sina_Weibo/clustered grouped'
os.chdir(cwd)
type_group_cluster = "group2_cluster3"

text_file = open( type_group_cluster + ".txt", "r")
groups_clusters = text_file.read().split('\n')  
text_file.close()
groups_clusters = list(filter(None, groups_clusters)) 

# you need to replace your own cookie and change your cookie from time to times !!!  
today_cookie_mobile = " SSOLoginState=1653994392; SUB=_2A25PkYPHDeRhGeFN71sS8SzFwjWIHXVtfS2PrDV6PUJbktB-LXfzkW1NQAOoWgg2uR-J-psO-i_4rlJKeoRIUGi2; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFebFUdhj4ecuLMYZc.yuio5NHD95QNe0B4e02E1K.4Ws4Dqcj_i--4i-82iKysi--ciK.Ni-27i--Ni-i8i-2pi--fi-z7iK.pi--Xi-i8i-27; _T_WM=cf5194d98d53499813dcd5fcca8af07f"
cook_mobile = {"Cookie": today_cookie_mobile}
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
header = { 'User-Agent' : user_agent}

def GetMobileUrl(web_link):
    rand_letter = web_link.split("?")[0].split("/")[-1]
    userid = re.compile(".*/(\d+)").match(web_link).group(1)
    mobile_url = "https://weibo.cn/repost/" + rand_letter + "?uid=" + userid + "&rl=1"
    return mobile_url

def getUrlList(Mobile_url):   #should be a string, the last part of the url
    """
    获取一个根的所有的转发页面链接
    :param url: 主页面链接
    :return: 所有评论链接 
    """
    cook_mobile = {"Cookie": today_cookie_mobile}
    
    form_action = Mobile_url.split("/")[-1]

    time.sleep(random.uniform(0.9, 3.5)) 
    
    html = requests.get(Mobile_url, cookies=cook_mobile, headers = header).content  
    soup = BeautifulSoup(html, "lxml") #html.parser
    form = soup.find("form", attrs={"action": "/repost/" + form_action})
    
    if form is None: 
        
        url_list = [Mobile_url]
        
    else:
        b = Mobile_url + "&page="
        c = form.find("div").text.split("/")[1]
        d = len(c) -1
        e = c[0:d]        #评论的页数
        url_list = []
        for i in range(1,int(e) + 1):
            url_list.append(b + str(i))
    url_list.reverse()
    return url_list

####################################

def GetRepost(all_url):
    
    cook_mobile = {"Cookie": today_cookie_mobile}
    
    try:
        weiboRepost=open(str(time.strftime('%Y%m%d%H%M%S',time.localtime()))+"repost.csv", 'w')
        title = '原用户名\t原内容\t原发布时间\t转发用户名\t转发用户id\t转发内容\t点赞数\t转发时间\t转发来源\n' #\
        print(title.replace("\n",""))
        weiboRepost.write(title)
        
        html = requests.get(all_url[-1], cookies=cook_mobile, headers = header).content
        soup = BeautifulSoup(html, "lxml")
        r = soup.findAll('div', attrs={"class": "c"})
            
        origin_username = soup.find("div", attrs={"id": "M_"}).find("a").text     
        origin_content = soup.find("div", attrs={"id": "M_"}).find("span", attrs={"class": "ctt"}).text 
        origin_time = soup.find("div", attrs={"id": "M_"}).find("span", attrs={"class": "ct"}).text 

        for i in all_url:
            time.sleep(random.uniform(0.3, 2.5)) 

            if all_url.index(i) > 0 and all_url.index(i) % 30 == 0:
                
                time.sleep(70) 
            
            html = requests.get(i, cookies=cook_mobile, headers = header).content
            
            soup = BeautifulSoup(html, "lxml")
            r = soup.findAll('div', attrs={"class": "c"}) 
            for j in r[4:]: 
                
                if j.find_all('a',href=re.compile("/u")) != []:
                   
                    userid = re.compile(".*/(\d+)").match(str(j.find_all('a')[0])).group(1)
                    rep_username = j.find("a").text
                    repost_content = j.text.split('\xa0')[0] 
                    if len(j.text.split('\xa0')) != 1:
                        numlikes = j.text.split('\xa0')[1]
                        repost_time = j.text.split('\xa0')[2]
                        from_device = j.text.split('\xa0')[3]
                        line = origin_username + "\t" + origin_content + "\t"+ origin_time +"\t" + rep_username + "\t" + userid + "\t" + repost_content + "\t" + numlikes + "\t" + repost_time + "\t" + from_device + "\n"
                        print(line.replace("\n", ""))
            
                if j.find_all('a',href=re.compile("/u")) == [] and j.text.split('\xa0')[0] !="" : #type(re.compile(".*/(\w*\d*)").match(str(j.find_all('a')[0]))) == re.Match and 
                    
                    userid = re.compile(".*/(\w*\d*)").match(str(j.find_all('a')[0].get("href"))).group(1)
                    rep_username = j.text.split('\xa0')[0].split(':')[0]
                    if len(j.text.split('\xa0')) != 1:
                        repost_content = j.text.split('\xa0')[0] 
                        numlikes = j.text.split('\xa0')[1]
                        repost_time = j.text.split('\xa0')[2]
                        from_device = j.text.split('\xa0')[-1]
                        line = origin_username + "\t" + origin_content + "\t"+ origin_time +"\t" + rep_username + "\t" + userid + "\t" + repost_content + "\t" + numlikes + "\t" + repost_time + "\t" + from_device + "\n"
                        print(line.replace("\n", ""))
                
                print(line.replace("\n", ""))
               
                #写入文件
                weiboRepost.write(line)    
                
                 #考虑个性域名，字母在前，数字在后, 数字也可能不出现。   
                 
        weiboRepost.close()
        
    except Exception:
        print("Exceptions")
    except urllib.error.URLError:
        print('The handshake operation timed out')
    except NameError:
        print("Name Timeout is not defined")
    except ConnectionError:
        print("Error description: Socket error timed out.")  

#below is a demo

new_below7_12 = ['2020年首只秦岭大熊猫宝宝诞生',
 '上海浦东机场货机火灾已扑灭',
 '朱广权的七夕段子',
 '水果弹珠果冻',
 '满脑子都是太空弹',
 '福建省考资料分析']

for keyword in new_below7_12:   
    os.chdir(cwd + "/" + type_group_cluster)  #working directory 很重要！！！
    if keyword + "keywordpost.txt" in  os.listdir():	
        df = pd.read_csv(keyword + "keywordpost.txt", sep = "\t")
        filtered_df = df[df['转发数'].notnull()] 
        filtered_df = filtered_df[filtered_df['发布时间'].str.contains('今') == False]
        print(len(filtered_df))
        filtered_new = filtered_df.drop_duplicates()
        print(len(filtered_new))
       
        keyword_url_list = list(filtered_new["手机版链接"]) 

        print(keyword, len(keyword_url_list))

	##### make new dir to store reposts and change to new dir 

        dir = cwd + "/" + type_group_cluster + "/" + keyword  ##!!!!!!!

        if not os.path.exists(dir):
            os.mkdir(keyword) 

        os.chdir(cwd +  "/" + type_group_cluster + "/" + keyword)

        for i in range(37, len(keyword_url_list)): 
            print("This is the {}th mobile repost link".format(i+1)) 
            GetRepost(getUrlList(keyword_url_list[i])) 
            print("The {}th mobile repost link is done.".format(i+1))

        print("The whole crawling is done." + keyword)

##########-------------------------------------------------##################
