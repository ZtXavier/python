import re      #正则表达式
import urllib.request,urllib.error      #获取网络数据    
from bs4 import BeautifulSoup       #用来网页解析
import xlwt                                  #保存在excel中

# from test01 import saveData      
#用到的正则表达式有 * . ?
findlink = re.compile(r'<a href="(.*?)">')  #这里面i是用?的第二种模式为懒惰模式(尽可能少的匹配)
findlmgSrc = re.compile(r'<img.*src="(.*?)"',re.S)
findtitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findjudge = re.compile(r'<span>(\d*)人评价</span>')
findinq = re.compile(r'<span class="inq">(.*?)</span>')
findbd = re.compile(r'<p class="">(.*?)</p>',re.S)

def main():
    # 爬取的网页连接地址
    weburl = "https://movie.douban.com/top250?start="
    # 传入网页地址
    datares = getData(weburl)
    savepath = "豆瓣电影评价表top250.xls"
    # 保存数据
    saveData(datares,savepath)        
        
        
def getData(weburl):
    datalist = []    #用列表来存信息
    for i in range(0,10):
        url = weburl + str(i * 25)
        html = askurl(url)
        # 数据解析
        soup = BeautifulSoup(html,"html.parser")   #这里第二个参数是该函数库依赖的解析器
        for item in soup.find_all('div',class_="item"):   #这里的含义是寻找符合的标签
            resdata = []
            item = str(item)
            # 以下是将通过正则表达式来找到匹配的数据
            # 电影链接
            link = re.findall(findlink,item)[0]      
            resdata.append(link)
            # 图片链接
            imgsrc = re.findall(findlmgSrc,item)[0]
            resdata.append(imgsrc)
            # 标题
            title = re.findall(findtitle,item)
            if len(title) == 2:
                resdata.append(title[0])
                title1 = title[1].replace("/","")
                resdata.append(title1)
            else:
                resdata.append(title[0])
                resdata.append(" ")
            # 评分
            rating = re.findall(findRating,item)[0]
            resdata.append(rating)
            # 评价人数
            judgenum = re.findall(findjudge,item)[0]
            resdata.append(judgenum)
            # 电影评语
            inq = re.findall(findinq,item)
            resdata.append(inq)
            # 电影导演等信息
            bd = re.findall(findbd,item)[0]
            bd = re.sub(r'<br/>(\s*)?',"",bd)      # 用正则来过滤掉不需要的部分
            bd = re.sub("/","",bd)
            resdata.append(bd)
            datalist.append(resdata)
    return datalist
        
def askurl(url):
    #模拟浏览器头部信息
    head = {
         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    
    req = urllib.request.Request(url,headers = head)
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as err:
        # 这里用于判断目标字符串是否拥有需要的类型
        # code:返回状态码404表示不存在，500表示服务器错误
        # reason:返回错误原因 
        if hasattr(err,"code"):
            print(err.code)
        if hasattr(err,"reason"):
            print(err.reason)
    return html



def saveData(datalist,savepath):
    # 先创建一个对象
    store = xlwt.Workbook(encoding = "utf-8",style_compression=0)
    # 然后创建一个表格来分别对应存储信息
    exe = store.add_sheet('豆瓣电影评价表top250',cell_overwrite_ok=True)
    dictdb = ("电影链接","图片链接","中文名","外国名","评分","评价人数","电影评语","电影相关信息")
    for i in range(0,8):
        exe.write(0,i,dictdb[i])
    for i in range(0,250):
        data = datalist[i]
        for j in range(0,8):
            exe.write(i+1,j,data[j])
    store.save(savepath)
    
    
    
if __name__ == "__main__":
    main()
    print("爬取完毕")