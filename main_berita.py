import pandas as pd
import requests
import tkinter.messagebox
from bs4 import BeautifulSoup

url = 'https://hot.detik.com/?_ga=2.37249897.898864883.1674733433-1583770152.1673329588'
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')
additional_set = {
  'DOWNLOAD_DELAY' : 2,
  'RANDOMIZE_DOWNLOAD_DELAY' : False,
}
def sleep(additional_set):
  pass

container = soup.find_all('h3',{'class':'media__title'})

Headline = []
Waktu = []
alamat_url = []
url = []

for i in container:
  try:
    url.append(i.find('a').get('href'))
  except:
    url.append('')

for i in url:
  response = requests.get(i)
  soup = BeautifulSoup(response.content,'html.parser')
  pass

  try:
    Headline.append(soup.find('h1',{'class':'detail__title'}).get_text().replace('\n        ',''))
  except:
    Headline.append('')

  try:
    Waktu.append(soup.find('div',{'class':'detail__date'}).get_text())
  except:
    Waktu.append('')
      
  try:
    alamat_url.append(soup.find('link',{'rel':'amphtml'}).get('href'))
  except:
    alamat_url.append('')
    

df = pd.DataFrame({
    "Headline":Headline,
    "Waktu" :Waktu,
    "Alamat_url" :alamat_url
})

df.to_csv('hasil.csv',index=False)

tkinter.messagebox.showinfo(title='Hi there', message='finish scrapping,please check ur folder path')
