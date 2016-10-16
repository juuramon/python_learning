import urllib.request

with urllib.request.urlopen('http://podnikam.webnoviny.sk') as response:
	html = response.read()
	print(html)


#HTTP 403, kedze vie, ze som robot, cize toto solution IS NOT WORKING!