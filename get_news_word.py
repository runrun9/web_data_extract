import urllib.request
import bs4
import re
import json

def getwords(html):
  # Remove all the HTML tags
  txt = re.compile(r'<[^>]+>').sub(' ',html)
  # Split words by all non-alpha characters
  words = re.compile(r'[^A-Z^a-z]+').split(txt)
  # Convert to lowercase
  return [word.lower() for word in words if word!='']

host_url = "http://www.isi.edu"
current_url = host_url

#news一覧ページへ移行
c = urllib.request.urlopen(current_url)
soup = bs4.BeautifulSoup(c.read(), "html5lib")
links = soup('a')

for link in links:
  if ('href' in dict(link.attrs)):
      url=link['href']
      if 'news' in getwords(url):
          if url[0:4] == "http" and getwords(url)[len(getwords(url)) - 1] == "news":
              current_url = url
              break
          if url[0] == "/" and getwords(url)[len(getwords(url)) - 1] == "news":
              current_url = host_url + url
              break
c.close()
print(current_url)


#news取得
c = urllib.request.urlopen(current_url)
soup = bs4.BeautifulSoup(c.read(), "html5lib")
links = soup('a')

news_links =[]
for link in links:
  if ('href' in dict(link.attrs)):
      url=link['href']
      if "news" in getwords(url) and "year" not in getwords(url) and len(getwords(url)) != 1:
          if url[0:4] == "http" and getwords(url)[len(getwords(url)) - 1] != "news":
              news_links.append(url)
          if url[0] == "/" and getwords(url)[len(getwords(url)) - 1] != "news":
              news_links.append(host_url + url)

c.close()
# print( len( news_links ) )

#wordcount
wc = {} # text word collection in Base URL with 'news' in  url
for news_url in news_links:
  c = urllib.request.urlopen(news_url)
  soup = bs4.BeautifulSoup(c.read(), "html5lib")
  words = getwords( soup.getText() )
  for w in words:
    if len(w) > 5: # Short word is not counted/stop words as well
      wc.setdefault(w,0)
      wc[w]+=1
  c.close()

sorted_wc = sorted(wc.items(),key=lambda x:x[1],reverse=True)
for x in sorted_wc[0:10]:
    print(x)

# out = open('news_wc.txt',"w")
# json.dump(wc,out)
# out.close()
