
import requests

divar=requests.get('https://divar.ir/s/tehran')

from bs4 import BeautifulSoup

divar_soup= BeautifulSoup(divar.text ,'html.parser')
val=divar_soup.find_all('div',attrs={'class':'post-card-item kt-col-6 kt-col-xxl-4'})

for item in val:
    price = item.find('div', class_ = 'kt-post-card__description')
    if str(price) !='None' and price.text=='توافقی':
            print(item.text)