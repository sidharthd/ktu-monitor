from bs4 import BeautifulSoup as bs
import requests
from time import sleep

def search(last_notification):
	url = "https://ktu.edu.in/eu/core/announcements.htm"
	r=requests.get(url)

	html=r.text
	soup=bs(html,"html.parser")

	rows = soup.find(class_="ktu-news").find_all("tr")

	notifications = []

	for row in rows:
		notification = row.find_all("td")[1].find("b").text
		if notification != last_notification:
			notifications.append(notification)
		else:
			break

	return notifications