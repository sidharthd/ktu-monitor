from bs4 import BeautifulSoup as bs
import requests
r=requests.get("https://ktu.edu.in/eu/core/announcements.htm")
html=r.text
soup=bs(html)
tab=soup.table
for bold_text in tab.find_all_next("b"):
	print bold_text.text
	
