url = '' #Insert URL of concert site (e.g. https://www.cityline.com.hk/Login.html?targetUrl=https%3A%2F%2Fcultural.cityline.com.hk%2Fen%2F2025%2Fphantom2025.html)
email = '' #Replace with your member email address
password '' #Replace with your member password

from bs4 import BeautifulSoup
with open(url) as fp:
  page = BeautifulSoup(fp)

page.find();


