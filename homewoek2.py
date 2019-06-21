import http.cookiejar,urllib.request
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
cookie = http.cookiejar.CookieJar()
cookie = http.cookiejar.MozillaCookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
url=('http:www.17k.com/chapter/2933095/36699279.html')
request = urllib.request.Request(url,headers=headers)
response = opener.open(request)

for item in cookie:
    print(item.name,item.value)

#储存
filename = 'one.txt'
cookie.save(filename=filename,ignore_discard=True,ignore_expires=True)

cookie = http.cookiejar.MozillaCookieJar()
cookie.load('one.txt')
print(cookie)