#網路爬蟲in nknu class
import urllib.request as req
import bs4


url = "https://w3.nknu.edu.tw/zh/"

request = req.Request(url, headers={  #在爬蟲時有一件事很重要，那就是大多數網站是開給人類使用的，而不是機器
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
})

with req.urlopen(request) as reponse:
  data = reponse.read().decode("utf-8") 

root = bs4.BeautifulSoup(data, "html.parser") #data是要抓的內容，html.parser是抓取的工具
print(root,end="\n---------------------------------\n")
print(root.title,end="\n---------------------------------\n")
print(root.a,end="\n---------------------------------\n")
print(root.a.parent.name,end="\n---------------------------------\n")