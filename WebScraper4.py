import requests
from bs4 import BeautifulSoup

url = "http://podnikam.webnoviny.sk/wp/wp-admin/admin.php?page=im_invoice_proforma_detail&id=1385"
r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

print(soup)




