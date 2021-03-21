# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 15:55:24 2018

@author: User
"""

import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog as sd
from bs4 import BeautifulSoup
import requests
import time
import sys


def get_resourses(url):
    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
             "AppleWebKit/537.36 (KHTML, like Gecko)"
             "Chrome/63.0.3239.132 Safari/537.36"}
    return requests.get(url,headers=headers,cookies={"over18":"1"})


def parse_html(r):
    if r.status_code==requests.codes.ok:
        r.encoding="utf8"
        soup=BeautifulSoup(r.text,"html.parser")
    else:
        print("HTTP 請求錯誤...")
        soup=None
    return soup

def scrapping_ettoday():
    URL="https://www.ettoday.net/news/news-list.htm"    
    S=parse_html(get_resourses(URL))
    print("Homepage of ETtoday")
    print("\n")
    s1=S.find_all("div",class_="part_list_2")
    for line in s1:
        s2=line.find_all("h3")
        for j in s2:
            j1=j.find_all('a')
            for i in j1:
                print(i.text)
                print("https://www.ettoday.net"+i.get("href"))                
            print('\n')
            
def scrapping_yahoonews():
    URL="https://tw.news.yahoo.com/"
    S=parse_html(get_resourses(URL))
    print("Homepage of Yahoo News")
    print("\n")
    s=S.find_all("li",class_="Pos(r) Lh(1.5) H(24px) Mb(8px)")
    for line in s:
        s2=line.find_all("a",class_="D(ib) Ov(h) Whs(nw) C($c-fuji-grey-l) C($c-fuji-blue-1-c):h Td(n) Fz(16px) Tov(e) Fw(700)")
        for i in s2:
            print(i.text)
            print("https://tw.news.yahoo.com"+i.get("href"))        
        print('\n')
        
    

def scrapping_linetoday():
    URL="https://today.line.me/tw/pc"
    S=parse_html(get_resourses(URL))
    print("Homepage of Linetoday")
    print("\n")
    s=S.find_all("p",class_="content")
    for line in s:
        print(line.text)
        print('\n')

def search_date():
    now=time.time()
    while True:    
        try:
            n=input("Enter The Date(year-month-day): ")
            Input=time.mktime(time.strptime(n,"%Y-%m-%d"))
            while(now<Input):
                print("There is no news of that day. Please enter the date before today.")
                n=input("Enter The Date(year-month-day): ")
                Input=time.mktime(time.strptime(n,"%Y-%m-%d"))
        except ValueError:
            print("Wrong format. Please enter again.")
            continue
        else:
            break
    
    URL="https://www.ettoday.net/news/news-list-"+n+"-0.htm"
    S=parse_html(get_resourses(URL))
    print('\n')
    s1=S.find_all("div",class_="part_list_2")
    for line in s1:
        s2=line.find_all("h3")
        for j in s2:
            j1=j.find_all('a')
            for i in j1:
                print(i.text)
                print("https://www.ettoday.net"+i.get("href")) 
            print('\n')


def top_ranking():
    li=[]
    li2=[]
    n=0
    URL="https://today.line.me/TW/pc/popular/100259"
    S=parse_html(get_resourses(URL))
    s2=S.find_all("div",class_="icon like")
    for line in s2:
        like=line.find_all("span",class_="count")
        for i in like:
            li.append(i.text)
    s3=S.find_all("div",class_="icon reply")
    for line in s3:
        like=line.find_all("span",class_="count")
        for i in like:
            li2.append(i.text)
    s1=S.find_all("div",class_="txt")
    for line in s1:
        s=line.find_all("p",class_="content")
        for i in s:
            print(str(i.text))
            print('like: '+ str(li[n])+ ' reply: '+str(li2[n]))
            n+=1
        print("\n")
def sorting():
    n=input("Choose One Category to Enter"+"\n"+"(politics/finance/entertainment/sports/society/world/lifestyle/health/technology): ")
    while(n!="politics" and n!="finance" and n!="entertainment" and n!="sports" and n!="society" and n!="world" and n!="lifestyle" and n!="health" and n!="technology"):
        print("Wrong input. Please enter again.")
        n=input("Choose One Category to Enter"+"\n"+"(politics/finance/entertainment/sports/society/world/lifestyle/health/technology): ")
    URL="https://tw.news.yahoo.com/"+n
    S=parse_html(get_resourses(URL))
    print('\n')
    a=S.find_all("ul",class_="H(100%) D(ib) Mstart(24px) W(32.7%)")
    for s1 in a:
        s=s1.find_all("li",class_="Pos(r) Lh(1.5) H(24px) Mb(8px)")
        for line in s:
            s2=line.find_all("a",class_="D(ib) Ov(h) Whs(nw) C($c-fuji-grey-l) C($c-fuji-blue-1-c):h Td(n) Fz(16px) Tov(e) Fw(700)")
            for i in s2:
                    print(i.text)
                    print("https://tw.news.yahoo.com"+i.get("href"))
            print('\n')
            
def do_askstring():
    while True:
        try:
            str_input=sd.askstring("Ask City", "City Name:")
            city=str_input
            url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9f7db10cac1a0f4d7dcbbd59eecf0344"
            json_data=requests.get(url).json()
            print(city)
            print("location coordinate......")
            formatted_data1 = json_data['coord']
            print("longitude: "+ str(formatted_data1['lon']))
            print("latitude: "+ str(formatted_data1['lat']))
            formatted_data2 = json_data['main']
            print("\n" + "weather description......")
            print("temperature: "+ str(formatted_data2['temp'])+"°F")
            print("pressure: " + str(formatted_data2['pressure']))
            print("humidity: "+ str(formatted_data2['humidity']))
            print("temperature_MIN: "+ str(formatted_data2['temp_min'])+"°F")    
            print("temperature_MAX: "+ str(formatted_data2['temp_max'])+"°F")   
            formatted_data3 = json_data['weather'][0]['description']      
            print("condition: "+ formatted_data3)
            break
        except KeyError:
            print("City name error!!\n")
        except TypeError:
            break
        
def weather():
    root=tk.Tk()
    root.title("Weather")
    root.geometry("300x30")
    ttk.Button(root, text="City", command=do_askstring).pack()
    root.mainloop()

def stock():
    API_KEY1 = 'GPRQCL0QCG4UHRIY'
    r1 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=' + API_KEY1)
    if (r1.status_code == 200):
        #print r.json()
        result1 = r1.json()
        data1 = result1['Realtime Currency Exchange Rate']
        print ("From_Currency Name: " + data1['2. From_Currency Name'])
        print ("To_Currency Name: " + data1['4. To_Currency Name'])
        print ("Exchange Rate: " +  data1['5. Exchange Rate'])
        print ("Last Refreshed: " + data1['6. Last Refreshed'])
        print ("Time Zone: " + data1['7. Time Zone'])
        
    API_KEY2 = 'GPRQCL0QCG4UHRIY'
    r2 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=' + API_KEY2)
    if (r2.status_code == 200):
        #print r.json()
        result2 = r2.json()
        print()
        data2 = result2['Realtime Currency Exchange Rate']
        print ("From_Currency Name: " + data2['2. From_Currency Name'])
        print ("To_Currency Name: " + data2['4. To_Currency Name'])
        print ("Exchange Rate: " +  data2['5. Exchange Rate'])
        print ("Last Refreshed: " + data2['6. Last Refreshed'])
        print ("Time Zone: " + data2['7. Time Zone'])
        print("\n")
        print("\n")

while True:
    while True:
        try:
            n=int(input('0:Stop 1:ETtoday_homepage 2:Yahoonews_homepage 3:Linetoday_homepage'+"\n"+'4:Date searching 5.Top ranking 6.News sorting 7.Weather 8.Stock'+"\n"+'Ans: '))
            while(n<0 or n>8):
                print('Wrong number. Please enter again.')
                n=int(input('0:Stop 1:ETtoday_homepage 2:Yahoonews_homepage 3:Linetoday_homepage'+"\n"+'4:Date searching 5.Top ranking 6.News sorting 7.Weather 8.Stock'+"\n"+'Ans: '))
        except ValueError:
            print('Please enter a number.')
            continue
        else:
            break
        
    if n==0:
        sys.exit(0)
    elif n==1:
        print('Loading.....')
        print('\n')
        scrapping_ettoday()
    elif n==2:
        print('Loading.....')
        print('\n')
        scrapping_yahoonews()
    elif n==3:
        print('Loading.....')
        print('\n')
        scrapping_linetoday()
    elif n==4:
        search_date()
    elif n==5:
        print('Loading.....')
        print('\n')
        top_ranking()
    elif n==6:
        sorting()
    elif n==7:
        weather()
    elif n==8:
        print('Loading.....')
        print('\n')
        stock()

