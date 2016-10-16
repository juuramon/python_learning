# Trying to get to the webpage and scrape the data. Not able to due to the
# login needed! (trying to login in login.py)
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

r = Request('http://podnikam.webnoviny.sk/wp/wp-admin/admin.php?page=im_invoice_proforma_detail&id=1385',
            headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(r).read()
soup = BeautifulSoup(webpage, "html.parser")

print(soup)
