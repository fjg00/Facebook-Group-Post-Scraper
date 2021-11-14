from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup 

import argparse
import time
import json

import os
import time
from selenium.webdriver.chrome.options import Options

def addvalues(dictionary, key, L):
    """Append multiple values to a key in the given dictionary"""
    if key not in dictionary:
        dictionary[key] = list()
    dictionary[key].extend(L)
    return dictionary


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-notifications')

driver = webdriver.Chrome('INSERT CHROME DRIVER DIRECTORY HERE', options=chrome_options) #USER INPUT
driver.get('https://www.facebook.com/')

email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name = 'email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name = 'pass']")))


email.clear()
password.clear()

email.send_keys("INSERT EMAIL HERE") #USER INPUT
password.send_keys("INSERT PASSWOR HERE") #USER INPUT


login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type = 'submit']"))).click()


#maximize window
driver.maximize_window()

n_scrolls = 5

x = "INSERT SEARCH PROMPT HERE" #USER INPUT

x = x.replace(" ","%20")

driver.get('INSERT GROUP URL HERE'+x) #USER INPUT

text = ""
comments = ""
z = 1

for i in range(1,n_scrolls):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(5)
    
    
    anchor = driver.find_elements_by_tag_name('a')
    anchor = [a.get_attribute('href') for a in anchor]
    anchor = [a for a in anchor if (str(a).startswith('https://www.facebook.com/groups/INSERTGROUPNUMBER/posts/') and 'comment' not in str(a))] #USER INPUT
    
 
WrapperDict = list() 
    
for a in anchor:
        driver.get(a)
        time.sleep(1)
        
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        
        actualPosts =  soup.find_all( 'div' , class_ = "kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q") #posts
        actualPosts = actualPosts +  soup.find_all( 'div' , class_ = "o9v6fnle cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q") #new
        actualPosts = actualPosts + soup.find_all( 'div' , class_ = "kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql") #both
                
        w = 1
        
        BranchDict = dict()
        BranchDict["tag"] = 1
        BranchDict["patterns"] = 1
        BranchDict["responses"] = list()
        L = list()
        
        for post in actualPosts:
            s = post.get_text()
            if (s == "INSERT GROUP DESCRIPTION HERE"): #USER INPUT
                time.sleep(1)
            elif len(s.split()) < 4:
                time.sleep(1)
            else:
                if w == 1: #post
                    text= text + post.get_text() 
                    BranchDict["tag"] = x + str(z) 
                    BranchDict["patterns"] = text
                    w = w + 1
                elif w > 1 : #comments
                    comments = post.get_text()
                    L.append(comments)
                    comments = ""
        z = z + 1
        addvalues(BranchDict, "responses", L)
        WrapperDict.append(BranchDict)
        text = ""
        
x = '/.' + x + '.json'    
 
with open(x,'w', encoding='utf-8') as file:
            file.write(json.dumps(WrapperDict, indent = 4, ensure_ascii=False).encode('utf-8').decode())
            
                
