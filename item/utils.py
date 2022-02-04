from bs4 import BeautifulSoup
import requests

def get_item_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    title=soup.find('span',class_="B_NuCI").getText()
    price=soup.find('div',class_="_30jeq3 _16Jk6d").getText()
    img_div=soup.find('div',class_="CXW8mj _3nMexc")
    des_div=soup.find('div',class_="_1mXcCf RmoJUa")
    imgurl=img_div.find('img').get('src')
    des=des_div.find('p').getText()
    rate=int(price[1:].replace(',',''))
    itemdata={"title":title,
    "price":rate,
    "imgurl":imgurl,
    "des":des
    }
    print(itemdata)
    return itemdata

