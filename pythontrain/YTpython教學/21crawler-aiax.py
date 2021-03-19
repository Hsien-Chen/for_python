# 抓取medium.com資料
import urllib.request as req
url = "https://medium.com/_/api/home-feed"
# 建立request物件，並附加request headers資訊
request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"})
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')
#解析json格式，取得文章標題
import json
data = data.replace("])}while(1);</x>","")
data = json.loads(data)
# print(data)
# 取得json資料中的文章標題
posts = data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])


