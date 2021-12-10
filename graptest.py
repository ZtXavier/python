import requests
 
# 中文网页：https://baike.so.com/doc/24386561-25208408.html
url1='https://baike.so.com/doc/24386561-25208408.html'
#添加请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
response_1=requests.get(url1, headers=headers)
 
response_1.encoding='utf-8'
#第一种：
# with open('steve_jobs2.html','w',encoding='utf-8') as f1:
#     f1.write(response_1.text)
#第二种：
f1=open('steve_jobs2.html','w',encoding='utf-8')
f1.write(response_1.text)
 
c=response_1.text
print(c)


#这里设置header就是为了避免被服务器认出来非人类操作