# Just using a different solution hoping for different outcome.
# Still not able to scrapte the desired data as I`m not logged in.
#(login.py in progress)

import requests
from bs4 import BeautifulSoup

#urlInvoice = "http://podnikam.webnoviny.sk/wp/wp-admin/admin.php?page=im_invoice_proforma_detail&id=1385"
url = "http://podnikam.webnoviny.sk"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")



print(soup)
