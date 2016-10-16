from urllib.request import Request, urlopen
import re

#regex = '<title>(.+?)</title>'
#pattern = re.compile(b'<title>(.+?)</title>')

req = Request('http://podnikam.webnoviny.sk/wp/wp-admin/admin.php?page=im_invoice_proforma_detail&id=1385', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
#title = re.findall(pattern, webpage)

print(webpage)


#dostanem sa na loginscreen a neviem co dalej
