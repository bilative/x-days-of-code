import requests
from bs4 import BeautifulSoup
import re
import time
import pandas as pd
import numpy as np

#This one is needed on every steps
def get_soup(BASE_PATH):
    page = requests.get(BASE_PATH)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

#This one is to take the urls of each phones
def visit_every_cat_page(page_url_wo_num, last_num):
    phone_url = []
    phone_name = []
    for page_num in range(1, last_num+1):
        phones_hole_page = page_url_wo_num + f'{page_num}'

        for i in range(1):
            soup = get_soup(phones_hole_page + f"?page={i}")

            for i in soup.find_all('a', href=True, attrs={'class':'picture'}):
                phone_url.append('https:' + i['href'])
                phone_name.append(i['title'])
            time.sleep(1)
    return phone_url

urls = visit_every_cat_page(page_url_wo_num, last_num)

print(len(urls))
#There are about 450 different phone page/url 

#This one to take every attributes and their values as dataframe
def take_infos_as_df(urls):
    df = pd.DataFrame()
    for i in urls:
        soup = get_soup(i)
        names = []
        values = []
        for i, j in zip(soup.find_all('td', attrs={'class' : "gg-d gg-t ddr spec-title"}), soup.find_all('td',attrs={'class':'gg-w gg-d ddr gg-m productFeaturesitemList'})):
            names.append(i.text)
            values.append(j.text.replace('\n', '').replace(' ', ''))
        if len(names)<1:
            df1 = pd.DataFrame(columns= names)
            df1.loc[0,:] = values
            df = df1
        # I took data row by row in every step, and concat them in same dataframe
            # This condition and the task make it possible
        if len(names)>0:
            df1 = pd.DataFrame(columns= names)
            df1.loc[0,:] = values
            df = pd.concat([df, df1])
        # I describe this below!!!!
        time.sleep(2)
    df.reset_index(drop = True, inplace = True)
    return df

df = take_infos_as_df(urls)

df.to_csv('phone_infos.csv', index=False)

# There is time.sleep(2) in a line. This is importtant for the host of the website. We are automating collecting data process, this could done so fast. But this mostly cause overload on the website we connect. So their traffic could effect bad from our process. They are doing their job, we dont wanna make their job hard for them. So we wait 2second for every step. Yea process took about 20 minute for me.
# This is so important!!
