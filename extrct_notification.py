from bs4 import BeautifulSoup as bs
import requests

def send_mail(notifications):
	for i in notifications:
		print i

last_notification = ""

r=requests.get("https://ktu.edu.in/eu/core/announcements.htm")
html=r.text
soup=bs(html,"html.parser")
tab=soup.table
rows = soup.find(class_="ktu-news").find_all("tr")

notifications = []
if __name__ == "__main__":
	for row in rows:
		notification = row.find_all("td")[1].find("b").text
		if notification != last_notification:
			notifications.append(notification)
		else:
			break

	if notifications:
		send_mail(notifications)

	for i in notifications:
		print(i)