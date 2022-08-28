# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:05:19 2022

@author: coolz
"""
import re
import json 
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Edge()
driver.get("https://pmkisan.gov.in/")
outputFile = open('pmkisan_scrape.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

years = [0,1,2,3]
period = [0,1,2]
outputWriter.writerow(['State','Total Payment Percentage','StateCode','Total Beneficiaries','Total Payment','Period','FinYr'])

def fun(data):
    soup = BeautifulSoup(data,features="lxml")
    results = soup.findAll('script', {'type':'text/javascript'})
    r = []

    for result in results :
        if 'var str= [' in result.text:
            x = re.findall(r'var str= (\[.*\])', result.text)
            if (len(x) > 0):
                r.append(x[0])
    data = r[0]
    
    p = re.compile('(?<!\\\\)\'')
    data = p.sub('\"', data)
    data = json.loads(data)
    for state in data:
        outputWriter.writerow([state['StateName'],state['Percent'],state['StateCode'],state['TotalData'],state['PaymentSuccessAndPending'],state['InstallmentNo'],state['FinYr']])
    
for y in years:
    for p in period:
        #print(y,p)
        yeardrop = Select(driver.find_element_by_id("ddlFinYr"))        
        yeardrop.select_by_index(y)
        if y == 3 and p >= 1:
            continue            
        perioddrop = Select(driver.find_element_by_id("ddlTrimester"))
        perioddrop.select_by_index(p)
        html = driver.page_source
        fun(html)
outputFile.close()