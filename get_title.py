import urllib.request
import bs4

url ="http://www.isi.edu/technology_groups/internet_and_networked_systems/publications"
response = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(response.read())

print("---------- main ----------")
span_a = []
span = soup.find_all("span",class_="pub_title")
for x in span:
    span_a.append(x.find_all("a"))

for a in span_a[0:30]:
    for x in a:
        print("\n{}".format(x.get_text()))
