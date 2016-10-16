import requests
import re 
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

#url = "http://podnikam.webnoviny.sk/wp/wp-admin/admin.php?page=im_invoice_proforma_detail&id=1385"
#r = requests.get(url)
r = Request('http://podnikam.webnoviny.sk/wp/wp-admin/admin.php?page=im_invoice_proforma_detail&id=1385', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(r).read()

soup = BeautifulSoup(webpage, "html.parser")

print(soup)


#Pekne naformatovane, ale neviem sa dostat dalej

