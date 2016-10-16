import requests

with requests.Session() as c:
	url = 'http://podnikam.webnoviny.sk/wp/wp-admin/admin.php?page=im_invoice_proforma_detail&id=1385'
	c.get(url)
	

	
