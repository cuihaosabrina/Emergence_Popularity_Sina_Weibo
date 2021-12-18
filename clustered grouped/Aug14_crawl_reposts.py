#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 21:57:56 2021

@author: cui_hao
"""
# 转发网络 
#server_crawl_repost.py
import pandas as pd
import os
#from datetime import datetime, timedelta
import random
import requests
from bs4 import BeautifulSoup
import re
import time

#cwd = "/mnt/sdb1/cuihao/keywords"
cwd = '/Users/cui_hao/Documents/GitHub/Weibo_thesis/keywords0717to0917/clustered grouped'
os.chdir(cwd)
# 要非常注意directory!!!
type_group_cluster = "group2_cluster1"
"group3_cluster2"
#"group3_cluster3"
#"group2_cluster2"
#"group1_cluster3"
#"group1_cluster2"

#"group1_cluster1"
#"group2_cluster3"
#
#
#"group2_cluster1"
#"group1_cluster3" 

text_file = open( type_group_cluster + ".txt", "r")
groups_clusters = text_file.read().split('\n')  
text_file.close()
groups_clusters = list(filter(None, groups_clusters)) #576 需要filter None!!!!

print(len(groups_clusters)) #408 #576 #410


#social_hashtags = groups_clusters

today_cookie_mobile = "M_WEIBOCN_PARAMS=lfid%3D102803%26luicode%3D20000174; _T_WM=413a515abcf58f8344099ca33f07ae3b; SSOLoginState=1638380969; SUB=_2A25Mo8X5DeRhGeFN71sS8SzFwjWIHXVsb-uxrDV6PUJbktB-LWankW1NQAOoWi_FAweL0o78jzR7U3V1fYJ5Q2Jt; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFebFUdhj4ecuLMYZc.yuio5NHD95QNe0B4e02E1K.4Ws4Dqcj_i--4i-82iKysi--ciK.Ni-27i--Ni-i8i-2pi--fi-z7iK.pi--Xi-i8i-27"
#"SSOLoginState=1638380969; SUB=_2A25Mo8X5DeRhGeFN71sS8SzFwjWIHXVsb-uxrDV6PUJbktB-LWankW1NQAOoWi_FAweL0o78jzR7U3V1fYJ5Q2Jt; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFebFUdhj4ecuLMYZc.yuio5NHD95QNe0B4e02E1K.4Ws4Dqcj_i--4i-82iKysi--ciK.Ni-27i--Ni-i8i-2pi--fi-z7iK.pi--Xi-i8i-27"
#"M_WEIBOCN_PARAMS=lfid%3D102803%26luicode%3D20000174; MLOGIN=1; SSOLoginState=1638380969; SUB=_2A25Mo8X5DeRhGeFN71sS8SzFwjWIHXVsb-uxrDV6PUJbktB-LWankW1NQAOoWi_FAweL0o78jzR7U3V1fYJ5Q2Jt; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFebFUdhj4ecuLMYZc.yuio5NHD95QNe0B4e02E1K.4Ws4Dqcj_i--4i-82iKysi--ciK.Ni-27i--Ni-i8i-2pi--fi-z7iK.pi--Xi-i8i-27; _T_WM=74697775660"
#"_T_WM=9fc10bfbf501ae65832ebcd520bf6ad8; SSOLoginState=1637015847; SUB=_2A25MlpF3DeRhGeFN71sS8SzFwjWIHXVseD8_rDV6PUJbktCOLVDxkW1NQAOoWn_ZS9a95VFuWnckhtXgLWHjA2v2; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFebFUdhj4ecuLMYZc.yuio5NHD95QNe0B4e02E1K.4Ws4Dqcj_i--4i-82iKysi--ciK.Ni-27i--Ni-i8i-2pi--fi-z7iK.pi--Xi-i8i-27; SCF=Aha4XxHMg9AQ8pCP6aqmXzBmnA6kTsunGvm4vTCYJxelLV9quW9Q5FqMLHPUxa03Lpv-piijUf106YnKdB5QthA."
#"SSOLoginState=1637015847; SUB=_2A25MlpF3DeRhGeFN71sS8SzFwjWIHXVseD8_rDV6PUJbktCOLVDxkW1NQAOoWn_ZS9a95VFuWnckhtXgLWHjA2v2; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFebFUdhj4ecuLMYZc.yuio5NHD95QNe0B4e02E1K.4Ws4Dqcj_i--4i-82iKysi--ciK.Ni-27i--Ni-i8i-2pi--fi-z7iK.pi--Xi-i8i-27; _T_WM=21d48925b8312c9b531054204ea35983; SCF=Aha4XxHMg9AQ8pCP6aqmXzBmnA6kTsunGvm4vTCYJxelLV9quW9Q5FqMLHPUxa03Lpv-piijUf106YnKdB5QthA."
#"_T_WM=21d48925b8312c9b531054204ea35983; SUB=_2A25MH62hDeRhGeFN71sS8SzFwjWIHXVv4zPprDV6PUJbktB-LWvDkW1NQAOoWmh4VoDCoPnucODU2A7J1yIs8xmR; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFebFUdhj4ecuLMYZc.yuio5NHD95QNe0B4e02E1K.4Ws4Dqcj_i--4i-82iKysi--ciK.Ni-27i--Ni-i8i-2pi--fi-z7iK.pi--Xi-i8i-27; SCF=Aha4XxHMg9AQ8pCP6aqmXzBmnA6kTsunGvm4vTCYJxelLV9quW9Q5FqMLHPUxa03Lpv-piijUf106YnKdB5QthA."
#" _T_WM=d5300f6f3ad491560416e9f074471fc4; SUB=_2A25MH62hDeRhGeFN71sS8SzFwjWIHXVv4zPprDV6PUJbktB-LWvDkW1NQAOoWmh4VoDCoPnucODU2A7J1yIs8xmR; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFebFUdhj4ecuLMYZc.yuio5NHD95QNe0B4e02E1K.4Ws4Dqcj_i--4i-82iKysi--ciK.Ni-27i--Ni-i8i-2pi--fi-z7iK.pi--Xi-i8i-27; SCF=Aha4XxHMg9AQ8pCP6aqmXzBmnA6kTsunGvm4vTCYJxelLV9quW9Q5FqMLHPUxa03Lpv-piijUf106YnKdB5QthA."
#"_T_WM=ffd86b775690f6937a49ccead078b0d2; SCF=AtoELGQ3lZ0Lbib6mi1TgsaEm9--Iee8UUtht0oMX-Eo4FrWD9eFP5Lj0mKXzQzi5vvMkJKum6-jToRrYn6N3io.; SUB=_2A25MbASQDeRhGedP7VYY-CjEzT-IHXVvrqzYrDV6PUJbktAKLXnakW1NX0HEZ2UTBu73i93r9x0V3fanfgXmgMAe; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5k5xJReM75SqTjq-AHoJug5NHD95QpeKqX1Knc1hq0Ws4Dqcj.i--fiK.NiK.pi--4i-2EiKLhi--Xi-i8i-8si--fi-88i-z7; SSOLoginState=1634235584"
#"_T_WM=d5300f6f3ad491560416e9f074471fc4; SUB=_2A25MH62hDeRhGeFN71sS8SzFwjWIHXVv4zPprDV6PUJbktB-LWvDkW1NQAOoWmh4VoDCoPnucODU2A7J1yIs8xmR; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFebFUdhj4ecuLMYZc.yuio5NHD95QNe0B4e02E1K.4Ws4Dqcj_i--4i-82iKysi--ciK.Ni-27i--Ni-i8i-2pi--fi-z7iK.pi--Xi-i8i-27; SCF=Aha4XxHMg9AQ8pCP6aqmXzBmnA6kTsunGvm4vTCYJxelLV9quW9Q5FqMLHPUxa03Lpv-piijUf106YnKdB5QthA."
#"_T_WM=d5300f6f3ad491560416e9f074471fc4; SSOLoginState=1629216242; SUB=_2A25MH62hDeRhGeFN71sS8SzFwjWIHXVv4zPprDV6PUJbktB-LWvDkW1NQAOoWmh4VoDCoPnucODU2A7J1yIs8xmR; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFebFUdhj4ecuLMYZc.yuio5NHD95QNe0B4e02E1K.4Ws4Dqcj_i--4i-82iKysi--ciK.Ni-27i--Ni-i8i-2pi--fi-z7iK.pi--Xi-i8i-27; SCF=Aha4XxHMg9AQ8pCP6aqmXzBmnA6kTsunGvm4vTCYJxelLV9quW9Q5FqMLHPUxa03Lpv-piijUf106YnKdB5QthA." 
#"SSOLoginState=1629216242; SUB=_2A25MH62hDeRhGeFN71sS8SzFwjWIHXVv4zPprDV6PUJbktB-LWvDkW1NQAOoWmh4VoDCoPnucODU2A7J1yIs8xmR; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFebFUdhj4ecuLMYZc.yuio5NHD95QNe0B4e02E1K.4Ws4Dqcj_i--4i-82iKysi--ciK.Ni-27i--Ni-i8i-2pi--fi-z7iK.pi--Xi-i8i-27; _T_WM=1e0484d815eea099efb0ebb89281fe76; SCF=Aha4XxHMg9AQ8pCP6aqmXzBmnA6kTsunGvm4vTCYJxelLV9quW9Q5FqMLHPUxa03Lpv-piijUf106YnKdB5QthA."
#"SSOLoginState=1629216242; SUB=_2A25MH62hDeRhGeFN71sS8SzFwjWIHXVv4zPprDV6PUJbktB-LWvDkW1NQAOoWmh4VoDCoPnucODU2A7J1yIs8xmR; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFebFUdhj4ecuLMYZc.yuio5NHD95QNe0B4e02E1K.4Ws4Dqcj_i--4i-82iKysi--ciK.Ni-27i--Ni-i8i-2pi--fi-z7iK.pi--Xi-i8i-27; _T_WM=1e0484d815eea099efb0ebb89281fe76; SCF=Aha4XxHMg9AQ8pCP6aqmXzBmnA6kTsunGvm4vTCYJxelLV9quW9Q5FqMLHPUxa03Lpv-piijUf106YnKdB5QthA."
#" _T_WM=1e0484d815eea099efb0ebb89281fe76; SCF=Aha4XxHMg9AQ8pCP6aqmXzBmnA6kTsunGvm4vTCYJxelLV9quW9Q5FqMLHPUxa03Lpv-piijUf106YnKdB5QthA.; SSOLoginState=1627897633; SUB=_2A25MA89xDeRhGeFN71sS8SzFwjWIHXVvD9E5rDV6PUJbktCOLRjskW1NQAOoWgPm3__D35Qc6vnOTgQ9Q72jCtpi; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFebFUdhj4ecuLMYZc.yuio5NHD95QNe0B4e02E1K.4Ws4Dqcj_i--4i-82iKysi--ciK.Ni-27i--Ni-i8i-2pi--fi-z7iK.pi--Xi-i8i-27; ALF=1630489279"
#"M_WEIBOCN_PARAMS=luicode%3D20000174; _T_WM=1e0484d815eea099efb0ebb89281fe76; SCF=Aha4XxHMg9AQ8pCP6aqmXzBmnA6kTsunGvm4vTCYJxelLV9quW9Q5FqMLHPUxa03Lpv-piijUf106YnKdB5QthA.; SSOLoginState=1627897633; SUB=_2A25MA89xDeRhGeFN71sS8SzFwjWIHXVvD9E5rDV6PUJbktCOLRjskW1NQAOoWgPm3__D35Qc6vnOTgQ9Q72jCtpi; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFebFUdhj4ecuLMYZc.yuio5NHD95QNe0B4e02E1K.4Ws4Dqcj_i--4i-82iKysi--ciK.Ni-27i--Ni-i8i-2pi--fi-z7iK.pi--Xi-i8i-27; ALF=1630489279"
# "_T_WM=20275767258; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFebFUdhj4ecuLMYZc.yuio5NHD95QNe0B4e02E1K.4Ws4Dqcj_i--4i-82iKysi--ciK.Ni-27i--Ni-i8i-2pi--fi-z7iK.pi--Xi-i8i-27; SCF=AgbDFxhQEEGFVTUwnhqpc9Q-tSqinhWHs850o7JgLTBkB_7MfrOD0_rFfo4sqlFYzCdtrPLt1vQgANvJJR0hmqc.; SUB=_2A25y0nUCDeRhGeFN71sS8SzFwjWIHXVuPRtKrDV6PUJbktANLVHSkW1NQAOoWpaPC1jemsrAt2Ea-RYRhaSwfVv8; SSOLoginState=1607861586"
#"_T_WM=7b9145612605f10755dec998c03c4377; ALF=1605624566; SCF=AgbDFxhQEEGFVTUwnhqpc9Q-tSqinhWHs850o7JgLTBkCH1uaH2vxHTl-suSjYoGYYR-DoADC6V-lD3KNXaszp4.; SUB=_2A25yiNvzDeRhGedP7VYY-CjEzT-IHXVucuW7rDV6PUJbktAKLRb3kW1NX0HEZ05A7KVo8P_bY9k7CWtmFEg3dCE4; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5k5xJReM75SqTjq-AHoJug5NHD95QpeKqX1Knc1hq0Ws4Dqcjbi--NiKyhi-8Fi--fiKnfi-8hi--Xi-zRi-iF-c8bMJLVqBtt; SUHB=079yb-W6s5RZiP; SSOLoginState=1603054499"

#"_T_WM=7b9145612605f10755dec998c03c4377; SCF=AgbDFxhQEEGFVTUwnhqpc9Q-tSqinhWHs850o7JgLTBkYHrh10kRlgiqi2iZO7G7Sg7L8sHhlWrV10QenI9ty_c.; SUB=_2A25yiCWmDeRhGedP7VYY-CjEzT-IHXVuc0vurDV6PUJbktANLVfkkW1NX0HEZ6GVXPvZtyjbA1G36a2DkqQqIERA; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5k5xJReM75SqTjq-AHoJug5JpX5K-hUgL.Fo2pSoB41hqRSoe2dJLoIEzLxKML12eLB-zLxK-L1h-LB-eLxKBLBonLB.iKqgiEIg4y; SUHB=0P1dxjbb6Q7TXI; SSOLoginState=1603032566; ALF=1605624566"

cook_mobile = {"Cookie": today_cookie_mobile}

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"

#"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"

header = { 'User-Agent' : user_agent}

# https://weibo.cn/repost/JbCmgg3ev?uid=2009113272&rl=1

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
    #form_action = form_action_url
    #url = comment_page + form_action  #string可以相加
    
    time.sleep(random.uniform(0.5, 3.5)) #randint
    
    html = requests.get(Mobile_url, cookies=cook_mobile, headers = header).content  #
    soup = BeautifulSoup(html, "lxml") #html.parser
    form = soup.find("form", attrs={"action": "/repost/" + form_action})
    
    if form is None: 
        
        url_list = [Mobile_url]
        
    else:
        #a = form.find('a').get('href')
        #b = a[0:len(a)-1] #页面的第一部分
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
        #for i in all_url[20:]:
        for i in all_url:
            time.sleep(random.uniform(0.5, 3.5)) #randint (3,8)

            if all_url.index(i) > 0 and all_url.index(i) % 30 == 0:
                
                time.sleep(100) 
            
            html = requests.get(i, cookies=cook_mobile, headers = header).content
            
            soup = BeautifulSoup(html, "lxml")
            r = soup.findAll('div', attrs={"class": "c"}) ##???
            for j in r[4:]: #4, should be 4; 3 这里应该是3;
                
                if j.find_all('a',href=re.compile("/u")) != []:
                    #item = j.find_all('a',href=re.compile("/u")) # it is a list, length is 1.
                    #userid = item[0].get("href").split("/")[2]
                    ########## Wrong！！！！！不是userid!!!!!!!!!!错了！！！！！！
                    userid = re.compile(".*/(\d+)").match(str(j.find_all('a')[0])).group(1)
                    #username = j.text.split('\xa0')[0].split(':')[0]
                    rep_username = j.find("a").text
                    repost_content = j.text.split('\xa0')[0] #.split(':')[1] 
                    #numlikes = j.text.split("\xa0")[-3]
                    if len(j.text.split('\xa0')) != 1:
                        numlikes = j.text.split('\xa0')[1]
                        repost_time = j.text.split('\xa0')[2]
                        from_device = j.text.split('\xa0')[3]
                        line = origin_username + "\t" + origin_content + "\t"+ origin_time +"\t" + rep_username + "\t" + userid + "\t" + repost_content + "\t" + numlikes + "\t" + repost_time + "\t" + from_device + "\n"
                        #line = userid + "\t" + username + "\t" + repost_content + "\t" + numlikes + "\t" + repost_time + "\t" + origin + "\n"
                        print(line.replace("\n", ""))
                        #weiboRepost.write(line)    
            
                if j.find_all('a',href=re.compile("/u")) == [] and j.text.split('\xa0')[0] !="" : #type(re.compile(".*/(\w*\d*)").match(str(j.find_all('a')[0]))) == re.Match and 
                    
                    userid = re.compile(".*/(\w*\d*)").match(str(j.find_all('a')[0].get("href"))).group(1)
                    rep_username = j.text.split('\xa0')[0].split(':')[0]
                    if len(j.text.split('\xa0')) != 1:
                        repost_content = j.text.split('\xa0')[0] #.split(':')[1]
                        numlikes = j.text.split('\xa0')[1]
                        repost_time = j.text.split('\xa0')[2]
                        from_device = j.text.split('\xa0')[-1]
                        line = origin_username + "\t" + origin_content + "\t"+ origin_time +"\t" + rep_username + "\t" + userid + "\t" + repost_content + "\t" + numlikes + "\t" + repost_time + "\t" + from_device + "\n"
                        print(line.replace("\n", ""))
                        #weiboRepost.write(line)                            
                
                print(line.replace("\n", ""))
                #if href.find("javascript:void(0)") != -1:
                    #line = str(index) + "\t" + title + "\t" + hot + "\t" + date +"\t"
                #写入文件
                weiboRepost.write(line)    
                
                 #考虑个性域名，字母在前，数字在后, 数字也可能不出现。   
                 
        weiboRepost.close()
        
    #except socket.timeout:
    except Exception:
        print("Exceptions")
    except urllib.error.URLError:
        print('The handshake operation timed out')
    #except http.client.RemoteDisconnected:
    #    print("Remote end closed connection without response")   
    #except http.client.IncompleteRead:
    #    print("IncompleteRead")
    except NameError:
        print("Name Timeout is not defined")
    #except error.URLError as err: 
    #    print("Error description:",err.reason)
    #except error.HTTPError as err:
    #    print("Error description:", err.reason)
    except ConnectionError:
        print("Error description: Socket error timed out.")  

###########################################################################################
#group1_cluster3
# 三浦春马10年前写给自己的信 11, not completed, 19th link
# 31省区市新增确诊16例 13, not, 74th link

#group3_cluster3
# 金鹰奖宣传片: 14
# 奶奶陪渐冻症孙女参加中考: 23
# 上海遛狗 30
# 秦昊东升旅行社导游 35 
# 特朗普自夸疫情发布会收视率超高 44 maybe not complete 
# 安徽巢湖中庙寺被淹 54 not completed
# '受过军训的饺子' 58
# 路小北没有救回哥哥 66 not completed 
# 录3年求婚视频男主回应 78 not completed, 23th link
# 周杰伦直播 87 start from 98th link
        
        

#for keyword in groups_clusters[14:100]:   # try just one element in the list #social_hashtags:

df_up_hashtag = ['法国室内公共场所强制佩戴口罩',
 '汽车日租价降幅达50%',
 '南特大教堂火灾或系人为',
 '排球少年完结',
 '有剧情的红绿灯',
 '广发证券保荐资格被暂停',
 '航拍恩施堰塞湖',
 '浪漫轨迹',
 '澳军准航母在南海与中国海军对峙',
 '大连全市现场招聘活动暂停',  #broke from 7th 
 '电排站回应采购360吨黄豆防汛',
 '王者世冠小组赛收官',
 '71岁老人5次高考终圆梦',
 '大连志愿者防护服拧出汗水',
 '瑞幸称被立案调查不会影响门店运营',
 '疫情中处在十字路口的旅游业',
 '杨英格回应退赛',
 '王者世冠应援歌曲',
 '新疆新增22例本土病例',
 '大连向足协申诉',
 '严浩翔翻唱安静',
 '北京重启消费季',
 '博茨瓦纳北部出现约350头非洲象尸体',
 '偶像梦幻祭', #broke from 38th 源数据有问题，已改正 
 '四川乐山洪峰过境',
 '第一创业', # too old in history, discard  
 '马刺无缘季后赛',
 '失去家的玩具们',
 '西班牙人续约武磊',
 '国内油价上调',
 '7月稀土出口下降近70%',
 '全国各地点亮地标为科比庆生',
 '自己身上的神奇点',
 '2020世界城市名册',
 '七夕蜜桃约会妆',
 '深圳特区40年',
 '六部门发文治理未成年人网络环境',
 '给闺蜜安利爱豆的样子',
 '巴托梅乌',
 '孟子坤世界末日',
 'FPX拿到赛点',
 '东京街头的繁华',
 '合肥冰雹',
 '滴水成画',
 '忍不住代入孙弈秋',
 '青岛凤凰音乐节', ##2019年的不要
 '任嘉伦薇娅直播',
 '股票新基金募资降3成',
 'LCK冒泡赛',
 '中超外援倒钩进球',
 '法国黄马甲示威游行在疫情中卷土重来',
 '吴彤时代少年团合影',
 '空军空降兵最新宣传片',
 '10位铁骑队员3分钟徒手推走抛锚车',
 '兵哥哥真人版演示手枪如何工作',
 '车艺照大赛',
 '军训照挑战',
 '我与冲浪只差个自拍杆',
 '电子竞技莫得感情',
 '白昊天反击江子算',
 '趣头条整改',
 '25省份上半年GDP出炉',
 '湖人战胜魔术',
 '宋祖儿喊话跟拍',
 '张雨绮撞衫Jennie',
 '意大利海上救援犬组织30年救起上千人',
 '掘金vs快船',
 '孟美岐跳霸王别姬'] 

############---------------------
group2_cluster1_lower = ['趣头条道歉',
 '乌鲁木齐地铁1号线停运',
 '315曝光趣头条虚假广告',
 '山东即墨查处问题海参',
 '金盆洗手之后的吴邪',
 '世界死亡病例超58万',
 '新疆新增本土病例1例',
 '上海全覆盖检查汉堡王',
 '香港经深港口岸入境须持核酸证明',
 '中国驻洛杉矶总领馆提醒当心山谷热',
 '美国凤凰城地区3中国公民患山谷热',
 '10岁男孩用零花钱给抗洪战士买糖',
 '山东连夜派出调查组赶赴即墨',
 '新疆昌吉公交暂停营运',
 '江湖预告',
 '长征五号火箭垂直转运至发射区',
 '长江2020年第2号洪水',
 '2020港姐15强诞生',
 '扎克伯格连线福奇',
 '美国新冠感染病例超355万',
 '宁静对郑希怡说我不希望失去你',
 '乘风破浪的姐姐三公分组',
 '消防员拿第一获准外出后的步伐',
 '韩国棋手AI作弊被判监禁',
 '新疆专升本考试延期举行',
 '乌鲁木齐机场航班大量取消',
 '国务院联防联控机制联络组离鄂返京',
 '申长友', #no such
 '李宇春自评级X',
 '49名退役军人一天内赶回家乡抗洪',
 '电影院复映片单',
 '一中学生连获三年全国青创赛奖项',
 '日本6月外国游客仅约2600名',
 '舞蹈生迷惑行为图鉴', #no such 
 '西班牙将扑杀10万只养殖貂',
 '中国全球化品牌50强榜单',
 '巴菲特4个月从苹果赚400亿美元',
 '兽药店库房查出土霉素原粉',
 '当两个孤独的人相遇',
 '岳云鹏沙溢蹭饭版无价之姐',
 '台军直升机坠毁画面',
 'Haro的盲僧',
 '北京7月21日进入主汛期',
 '下周北方将进入主汛期',
 '青岛即墨区自然资源局副局长被查',
 '校方回应中学生连获三年青创赛奖',
 '淮河发生2020年第1号洪水',
 '乌鲁木齐已启动疫情应急响应预案',
 '江西鄱阳中洲圩决口合龙',
 '美国加州幼儿园已报告近1000例确诊']


group2_cluster2_up = ['北京将稳妥有序推进电影院恢复开放',
 '安徽32条河湖超警戒水位',
 '暮白首大结局',
 '莫高窟单日游客最大限量调整为50%',
 '国防科大版无价之姐',
 '影院重启首日大学生连看四场',
 '全国电子烟市场首张罚单',
 '官方回应西安足球场禁止踢球',
 '北京电影院开启预售',
 '中国全网5G用户破亿',
 '福奇为美职棒新赛季开球',
 '深圳暖夜灯柱',
 '福布斯全球品牌价值100强',
 'Somi舞台',
 '乐队的夏天可太帅了',
 '吴前好厉害',
 '香港新增确诊80例',
 '水上列车驶过天空之镜',
 '浙江玉环全面排查阳台违规改造',
 '辽宁队淘汰新疆队',
 '韩国试射新型弹道导弹',
 '微软',
 '用玩具还原大话西游经典场景',
 '璇玑花式哄司凤',
 '唱过夏天', #26th broke
 'Otto解说',
 '北京电影院上座率上限调至50%',
 '缓解头痛的小方法',
 '时刻保持微笑的方法',
 '中国参加武器贸易条约缔约国大会',
 '被孙雯雯气死',
 '新西兰流浪猫与总理竞争年度人物',
 '当代爱情图鉴',
 '七夕蛤蟆',
 '居民回应豪华中学部分设施被拆',
 '山东荣成休渔期非法捕捞调查',
 '原路返回的可爱小鹿',
 '风月不相关将拍剧',
 '白色月光大结局',
 '2020高考暖心结局',
 '韦神解说',
 'S10资格赛',
 '中国96B坦克与俄T72坦克同场竞速',
 '亚马逊无人机获批',
 '深圳进入强制垃圾分类时代',
 '火箭雷霆抢七',
 '信条解析',
 '易建联寄语年轻球员',
 '孙弈秋有骨气',
 '中国每日航班量恢复到疫情前九成',
 '76岁大爷勇救200斤溺水小伙',
 '张伯礼获奖后第一天',
 '日本女足运动员加盟男队',
 '兰芊翊背锅',
 '猫先拿回来 手机可以慢慢等',
 '湖南援鄂医生送儿子武大报到',
 '寝室环境大赛',
 '美印将签关键军事协议共享信息',
 '郝帅撒娇',
 '美国西部山火持续肆虐',
 '全国多地景区门票降价',
 '统计局回应房地产市场回暖',
 '15种语言版你曾是少年',
 '第11号台风红霞',
 '泰国将提供270天旅游签证']


group3_cluster2_up = ['3岁女童凌晨独自上街小伙一路护送',
 '三十而已和二十不惑串场',
 '三十而已的男性角色',
 '中国女排版无价之姐',
 '优马铁子',
 '信条女主190',
 '健身教练的视角',
 '关晓彤四分之三减龄妆',
 '准研究生虐狗事件狗主人不接受道歉',
 '剑仙回归',
 '剑网3十一周年',
 '北京允许举办500人以下体育赛事活动',
 '北大回应留守女生报考考古专业',
 '口罩的防晒效果有多好',
 '吉野家将关闭含中国市场内150家门店',
 '唐国强老师演过的角色',
 '唯一的好男人是许子言',
 '大连女子隆胸去世医方承担完全责任',
 '姜贞羽恋情',
 '孙子跪地给七旬奶奶拍写真',
 '宁静李斯丹妮抢王霏霏',
 '张玉环案或申请约700万国家赔偿',
 '张艺兴 嘲笑我可以不要嘲笑努力',
 '把男朋友叫做普通朋友',
 '抹茶杏仁豆腐奶冻',
 '教育类硕士毕业生免试认定教师资格',
 '昊辰卷土重来',
 '杭州失踪女子居住小区居民献花祭奠',
 '林有有段位',
 '武汉东湖之眼摩天轮',
 '武汉菜市场卖野生青蛙',
 '父亲为弥补儿子亲手改造房间',
 '白桃乌龙青森冰沙',
 '羊城十二时辰',
 '羊能长得多潦草',
 '肖战自拍',
 '肯塔基州两支游行队伍现场对峙',
 '阚清子说朱一龙神秘',
 '阻止性侵被咬耳男子称不后悔',
 '阿里巴巴注册新公司京西']

group2_cluster3_up = ['1元抗癌厨房墙上留下不少电话号码',
 '3岁女孩被爸妈喂到70斤当吃播赚钱',
 '7岁女童商场偷拿玩具亲妈报警',
 '7省市将有大到暴雨',
 'AI技术复原91年前黑白视频颜色',
 'Angelababy回复章子怡',
 'TFBOYS演唱会单人机位',
 'iPhone12 Pro玻璃后壳曝光',
 '一只装满水的气球扎破瞬间',
 '乐山大佛脚趾露出',
 '乘风破浪的姐姐复活换位战',
 '乘风破浪的铁三角',
 '入狱4年手机被经办民警私用',
 '凌霄和李尖尖的CP名',
 '刘心悠 我喜欢谣言',
 '厦门两名高级警长同日殉职',
 '吴镇宇念王一博粉丝祝福语',
 '喂鲤鱼当消遣的黑天鹅',
 '四川宜宾通报路面塌陷',
 '多本爆特朗普黑料新书销量猛增',
 '女子被家暴高速收费站求助获救',
 '孔雀溜进图书馆',
 '学历鄙视链真存在吗',
 '宁静爸爸好年轻',
 '张朝阳称自己每天只睡4个小时',
 '张雨绮舞蹈进步好多',
 '张馨予呼吁不要对女演员胖瘦太苛刻',
 '当你发现队友在谈恋爱',
 '快乐源泉蔡国庆',
 '想象中给骑车的男友打伞',
 '我国新一轮降雨将启程',
 '我有一个梦想演讲57周年美国民众游行',
 '新疆宣布全面恢复正常生产生活秩序',
 '新疆新增17例本土病例',
 '日系初恋心动妆',
 '明年将禁用不可降解塑料袋',
 '景区上演现实版鱼跃龙门',
 '杜华 我自己打了自己的脸',
 '森碟腿部线条',
 '水果姐产后身材',
 '江西入室杀两人嫌犯又杀一人',
 '湖人时隔十年再进西决',
 '特朗普成为美国共和党总统候选人',
 '特朗普承认曾淡化新冠疫情严重性',
 '特朗普计划在白宫为弟弟举行葬礼',
 '猛龙战胜凯尔特人',
 '瑞幸咖啡单店现金流已转正',
 '璇玑切大号',
 '男子5000米世界纪录告破',
 '男子口罩内藏作弊器考科目一',
 '白天开饭店晚上挖地道盗文物',
 '硝酸铵是什么',
 '童瑶气质',
 '紫禁城600年一见如故',
 '罗冠军称梁颖方愿意公开道歉',
 '美国3000多专家联名挺福奇',
 '美国新冠肺炎确诊超491万例',
 '美国现十年来最大破产潮',
 '药水哥打拳',
 '谢霆锋谈年轻艺人排场大',
 '钟晓芹钟晓阳好甜',
 '钟晓阳暖男',
 '陈养鱼许放炮梁海王',
 '韩国植物园立安倍下跪谢罪雕像',
 '顾佳被骗',
 '香港教育局称教科书不应出现违法内容',
 '骑手摔残废了手机还在自动接单']

group1_cluster1_up = ['万只白鹭田野中齐飞',
 '全球单日新增新冠肺炎近30万例',
 '大波浪改编爱情买卖',
 '民警创作歌曲揭10种校园诈骗',
 '第12个全民健身日',
 '詹姆斯大帽威少',
 '雨后彩虹照']

group1_cluster2_up = ['30吨橘子散落高速没人哄抢',
 '70岁宝藏奶奶靠时装火出圈',
 'LGD状态',
 '上海大学开学礼物送干湿垃圾桶',
 '上海整治养犬行为违规者当场罚款',
 '仪陇通报400字官方回复错4字',
 '哪一刻决定开始养猫',
 '四行仓库客流量猛增两倍',
 '大连人vs恒大',
 '日本铲屎官记录自家猫咪叫声',
 '杭州失踪女子尸体在小区化粪池找到',
 '胡明轩三分球']

group1_cluster3_up = ['李遐怡新歌MV', '路小北和许蔚摊牌']

group2_cluster1_up = ['14款游戏APP存在隐私问题',
 '2020未来科学大奖获奖人揭晓',
 '9月1日起成都天然水域全面禁捕10年',
 'CLC新歌MV',
 'S10抽签仪式嘉宾',
 '一颗高楼大小行星将飞过地球',
 '下半年最想看到的电影',
 '中国方便面海外买家翻倍',
 '云南今年来野生菌中毒已致12死',
 '井底蛙顺着绳子奋力往岸上爬',
 '八月星空',
 '再无法超越的经典角色',
 '分享欲有多重要',
 '刘雨昕金丝眼镜', #53 broke
 '北京学校食堂不得制售冷食生食',
 '北京环球影城明年5月开园',
 '区块链金融顶层设计出台', 
 '卫健委明确抑郁症防治四类重点人群',
 '印度连续两日新增确诊破9.5万例',
 '去新疆旅游无需核酸检测及隔离',
 '同济大学军训教官跳女团舞',
 '吹玻璃师傅工作的样子',
 '大连10岁女童被害案法院判赔128万',
 '女艺人能有多敢说',
 '宁静看张雨绮出神忘选手机',
 '小鸟遇人僵直脖子如标本',
 '山西襄汾坍塌饭店老板被刑拘',
 '山顶小学摇滚乐队将开演唱会',
 '巴特勒40分',
 '张玉环前妻称他还欠我一个抱',
 '彭于晏像拉黄包车的车夫',
 '德云社小剧场将恢复演出',
 '德国小镇麦田怪圈',
 '成都300年桂花巷内桂花树全被砍',
 '救人医学生回应获奖1万元',
 '无价之邪',
 '杨幂瑞丽25周年封面',
 '核电站海底种珊瑚',
 '桂花椰汁西米糕',
 '武汉天空像羊群奔跑的云团',
 '武汉百万大学生返校',
 '民间大神打脸现场',
 '湖人球员众生相',
 '独居老人家中摔倒4天靠敲盆获救',
 '王源MV创意',
 '王菲K歌直播',
 '瑞士小镇下起巧克力雨',
 '硬糖少女首张EP',
 '罗云熙仲夏光影大片',
 '美国一夏令营发生集体感染',
 '美国俄勒冈州染成红色',
 '胡一天黄子韬 蜡笔小新',
 '菅义伟正式就任日本首相',
 '詹姆斯季后赛胜场数历史第一',
 '豆腐脑店老板作诗贴满墙',
 '赵丽颖哭的镜头',
 '还没从琉璃走出来',
 '这蜡烛吹得挺突然的',
 '逃离家暴有多难',
 '金晨郁可唯表情包',
 '陈木胜追思会',
 '隐秘的角落 切片式混剪',
 '零食托',
 '霍格沃茨学院妆',
 '青春芒果夜阵容', #青春芒果节官微 broke
 '韩国近七成80岁以下老人想工作',
 '香港新增新冠肺炎确诊113例',
 '黄子韬加盟说唱新世代']

group1_cluster1_down = ['写信力挺援港医护的港警收到回复了',
 '创业板注册制首批企业8月24日上市',
 '制造业PMI连续5个月在临界点以上',
 '北京企业乱倒建筑垃圾最高罚100万',
 '多肉乌龙青提沙',
 '女性科技人力资源比例进一步提升',
 '安徽解除紧急防汛期',
 '少儿读物类图书均价上涨超2成',
 '线下独处线上热闹成常态',
 '西藏加林山岩画上的动物世界',
 '连狗子都会玩滑板了',
 '首批火星地形地貌中文推荐译名']


group1_cluster2_down = ['00后内向男孩成国内首位手语翻译',
 '为战疫功勋护航21车队形是最高规格',
 '抚顺3.0级地震',
 '杭州金边云',
 '现在军训的才艺技能有多丰富',
 '约基奇三双创历史',
 '纳达尔退出2020年美网',
 '蓝色格纹穿搭',
 '西亚卡姆脚踢对手',
 '遵义欧亚医院总经理获刑20年',
 '重启特化']

group1_cluster3_down = ['KPL韩信星元皮肤',
 'SpaceX首批星际飞船乘客',
 '亲历者讲述国航航班突降千米',
 '大坂直美罢赛',
 '孤day打歌蛤蟆',
 '当给宠物加上特效',
 '影子银行规模三年缩减16万亿',
 '日本新内阁名单公布',
 '毛阿敏毛不易神仙合唱',
 '滞留乌市人员核酸检测合格后可离开',
 '用狗狗最爱的词语讲故事',
 '给李现P衣服',
 '美46万人庆摩托车节26万人确诊',
 '鄱阳县境内水位呈下降趋势',
 '长城上眺望北京CBD',
 '黎巴嫩司法部长辞职']

group2_cluster2_down = ['TFBOYS合唱Heart',
 '九旬大爷勇救落水男童',
 '北部湾大量珊瑚白化面临死亡',
 '台风过境吉林屋顶被掀树被刮倒',
 '嗨学网退费难',
 '四川强降雨结束',
 '国家卫健委18人专家团队抵达大连',
 '国庆酒店机票价格创5年新低',
 '安徽淮河王家坝关闸',
 '工信部要求严查SDK违规收集用户信息',
 '房地产的广告有多奇葩',
 '把悬崖村搬下悬崖',
 '林俊杰孙燕姿新歌MV',
 '武磊西乙首球',
 '江水已从乐山大佛脚趾退去',
 '现存中华老字号近一半持续亏损',
 '美国至少24州报告高校新冠病例',
 '雅润等5款消毒湿巾虚标酒精浓度']


group3_cluster3_down = ['1200万台第三方产品支持鸿蒙',
 '2岁女童10分钟横渡沾天湖',
 'KPL阿古朵首秀',
 'Mlxg手气',
 '三星电子关闭在华最后一家电脑厂',
 '上万颗钉子做成的立体山水画',
 '中国新冠疫苗在阿联酋获紧急批准',
 '乌克兰前总理季莫申科感染新冠肺炎',
 '周峻纬单场21分',
 '张雨绮 抱你到天亮mua',
 '恋爱脑的反常规操作',
 '杨超越工作室公告',
 '段振宇救姜小果',
 '特朗普考虑大选后撤换国防部长',
 '王一博霸总式选人',
 '王岳伦表白李湘王诗龄',
 '看到情侣的我',
 '综艺里最热闹的场面',
 '这年头水居然会敷面膜',
 '迪士尼在逃生物',
 '钟汉良小宝 什么偶像剧情节',
 '高福接种实验型新冠病毒疫苗']

group3_cluster2_down = ['DNA检测通告吓出高空抛物肇事者',
 'S7冒泡赛兮夜用卡萨丁淘汰iG',
 'iPhone11首次在印度生产',
 '中国代表在联大严厉驳斥美方无端指责',
 '刘永坦捐出最高科技奖800万奖金',
 '加满一箱油将多花3.5元',
 '南开录取通知书送两粒莲花种子',
 '吴尊友称未来出现疫情是一种常态',
 '大连地铁回应老人无健康码乘车受阻',
 '安倍晋三正式宣布辞职',
 '家中起火姐姐带9岁弟弟教科书式避险',
 '当老师让小朋友带一种蔬菜',
 '招生办通报专升本考试疑似泄题事件',
 '日方回应韩国立安倍下跪谢罪雕像',
 '时代少年团微电影',
 '易烊千玺大妈同款拍照姿势',
 '田雨白玉兰最佳男配角',
 '秦霄贤大波浪舞台好炸',
 '美国没资格要求安理会恢复对伊制裁',
 '美国西部97处大规模山火在燃烧',
 '考生伪造清华录取通知书',
 '薇娅李子柒当选全国青联委员',
 '贱内的意思',
 '青簪行预告是原声',
 '黄子韬爸爸去世']

group2_cluster1_down = ['150米盲道被改成十八弯',
 '2020亚洲小姐竞选面试',
 '2020年标准地图发布',
 '31省区市新增确诊14例',
 '347国道发生大面积山体垮塌',
 '8月有5场天象奇观',
 'DWG获得LCK夏季赛冠军',
 'Haro的盲僧',
 'S10抽签仪式时间',
 'THE9首支MV',
 '一旦接受了这个设定后',
 '世卫称全球需要多种类型疫苗',
 '丝滑可可糯米糍',
 '为什么火箭能飞太空飞机却不行',
 '乌童改造玲珑',
 '乌鲁木齐开展全民免费核酸检测',
 '乔丹支持NBA重启',
 '乘风破浪的姐姐三公分组',
 '云南新增境外航空输入病例1例',
 '人类早期驯服四肢的过程',
 '伦敦运河边的芭蕾舞者',
 '何洛洛呼吁粉丝在机场保持秩序',
 '全球二季度最赚钱100家企业',
 '准格尔首试免费接种宫颈癌疫苗',
 '出海观鲸偶遇海豚群狂奔',
 '别用衣架晾口罩',
 '北京警方起底美容贷',
 '北京高校承担学生返校核酸检测费用',
 '十几岁和现在恋爱的区别',
 '南京八卦洲首批人员撤离',
 '参与玉树救援的功勋犬天宝去世',
 '台风美莎克3日中午前后移入吉林',  
 '商务部回应美方再次升级对华为打压',
 '喉舌齿唇的发音部位',
 '在劫难逃刺激',
 '大连中风险封闭社区菜粮供应充足',
 '天津儿童免费乘车身高标准提至1米3',
 '央视记者实地探访乌鲁木齐社区',
 '女生中奖1吨娃哈哈送小朋友',
 '奶奶写的少女日记',
 '如何优雅的表达不满',
 '如何调整你的电脑桌椅',
 '学校复学成美国下一阶段疫情防控挑战',
 '宁吉喆说下半年最大挑战是稳就业',
 '宁静组拉横幅拉票',
 '安徽全椒县滁河实施爆破泄洪',
 '山东龙口一幼儿园校车与大货车相撞',
 '山西一施工罐车往河中倒水泥',
 '师德表现将作为教师职称评审首要条件',
 '广东47岁民警突发疾病倒在工作岗位',
 '广州暂停进口疫区冷冻肉制品和水产品',
 '库兹马三分绝杀',
 '张文宏称正在研究新冠特效药',
 '张萌不好意思找王一博合影',
 '张雨绮山东话rap',
 '徐艺洋 过程比结果重要',
 '微博将整治大胃王吃播内容',
 '德阳安医生自杀案今日开庭',
 '成都2名男子路中积水游泳比赛',
 '我国拟修法明确禁止倒挂国旗',
 '我的青春疼痛',
 '数辆过路车25秒静待老人过马路',
 '方硕最佳第六人',
 '曹操墓出土文物已修复900余件',
 '最喜欢的手机设计',
 '朱朝阳为严良庆生',
 '李斯丹妮中二vlog',
 '杨易脑王之王',
 '林郑月娥率队接受新冠病毒检测',
 '校方回应学生雨夜追星',
 '梦露 伊丽莎白泰勒',
 '汪苏泷线上演唱会', #45 link not finished
 '淮河发生2020年第1号洪水',
 '深航东航相关安全事件调查结果',
 '焦雅辉说希望理解医护不止在今天',
 '父亲回应家属被男子持铁锹暴打',
 '独行侠快船冲突',
 '王一博镜子蹲',
 '王丽坤手劲好大',
 '瑞丽已完成核酸检测全部为阴性',
 '福奇警告称美国疫情正向中西部蔓延',
 '福建下海救人的第三匹马已痊愈',
 '福建漳州龙海一厂房被吹倒',
 '科沃尔恶意犯规',
 '纽约周末发生多起枪击案',
 '网络游戏实名认证系统',
 '美国300家必胜客计划永久关闭',
 '美国扩大召回75款洗手液',
 '美国波特兰示威者推倒法院围栏',
 '老师授课的职业绝活',
 '考试成绩理想是什么体验', 
 '耳朵的工作量太大了', 
 '芝加哥所有桥梁升起',
 '花木兰放弃北美院线发行',
 '苹果秘密收购以色列相机公司',
 '菠萝芥末油条虾',
 '蒂姆状态',
 '西安业主自管小区一年盈利83万',
 '西班牙将扑杀10万只养殖貂',
 '西电拟清退33名失联超期博士生',
 '课间操跳得像康复训练',
 '贵州吉他村一年产800万把',
 '赵继伟高难度三分',
 '路人看到王俊凯的表情',  
 '跳河救人被冲走司机遗体找到',
 '迪丽热巴裤装造型', #here <--
 '重庆磁器口景区关闭',
 '雪顶气泡葡萄冰',
 '香港设计师绘画赠内地支援队',
 '马主人回应下海救人两匹马去世',
 '骗取贷款嫌疑人李冠君被通缉',
 '高考报考避坑口诀',
 '鹿晗连续6天拍打戏中暑',
 '黄晓明夏日午后大片',
 '黄景瑜喝酒对瓶吹',
 '黄金薯片爆浆拉丝芝士球',
 '黄鹤楼免票首日客流量涨3倍'] 

'''percentage of stepwise 
average of born in rome/sleeping beauty
(1) how long it takes 
(2)the way it reaches the HSL 
(3) contextual, what is about,
related to each other, make relationship between these aspects  
hope to understand the mechanism, depending on....  find relation and quantify 

maybe try different intervals and see how the statistics changes, trial and error 

show typical examples, make averages, how many steps, link to the nature of hashtag/when arrive 

tell problems/limitations, % percent of the data was corrupted 

leave out the statistics, but describe ... within 5 minutes? artificial
the list is manipulated, not folloiwng automated algorithm

method and data : describe the problems 
'''

for keyword in group2_cluster1_down[72:]:   # try just one element in the list #social_hashtags:
    os.chdir(cwd + "/" + type_group_cluster)  #working directory 很重要！！！
    if keyword + "keywordpost.txt" in  os.listdir():	
        df = pd.read_csv(keyword + "keywordpost.txt", sep = "\t")
        filtered_df = df[df['转发数'].notnull()] 
        print(len(filtered_df))
        filtered_new = filtered_df.drop_duplicates()
        print(len(filtered_new))
        # 再爬一遍不包含keyword的吧，因为存在展开全文这个东西。。。
        #filtered_new = filtered_df[~filtered_df["发布内容"].str.contains(keyword)]
        #filtered_new = filtered_df[filtered_df['发布内容'].str.contains(keyword, na=False)]
        # Filter out the rows that doesn't include the hashtag !!!!!!!!!!
        keyword_url_list = list(filtered_new["手机版链接"]) 

        print(keyword, len(keyword_url_list))

	##### make new dir to store reposts and change to new dir 

        dir = cwd + "/" + type_group_cluster + "/" + keyword ##!!!!!!!

        if not os.path.exists(dir):
            os.mkdir(keyword) 

        os.chdir(cwd +  "/" + type_group_cluster + "/" + keyword)

	## start crawling reposts in the new dir 
        for i in range(len(keyword_url_list)): ##Notice the beginning number !!!!!!!!!! #应该53！
            print("This is the {}th mobile repost link".format(i+1)) 
            GetRepost(getUrlList(keyword_url_list[i])) 
            print("The {}th mobile repost link is done.".format(i+1))

        print("The whole crawling is done." + keyword)

##########-------------------------------------------------##################








