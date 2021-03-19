# 抓取ptt電影版資料
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
# 建立request物件，並附加request headers資訊
request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"})
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')
#解析原始碼，取得文章標題
import bs4
root = bs4.BeautifulSoup(data, "html.parser") #利用beautifulsoup4解析html
titles = root.find_all("div", class_="title") #尋找所有class="title" 的div標籤
for title in titles:
    if title.a != None: #如果包含a標籤，印出來
        print(title.a.string)












