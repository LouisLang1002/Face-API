#coding=utf-8 
import urllib 
import urllib2
import json
#获取到网页内容的函数
def post(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    return response.read()
def main():
    pic_url="http://imgsrc.baidu.com/forum/pic/item/0df431adcbef760975bb9a3e2edda3cc7dd99eda.jpg"   #图片的地址
    url1="http://apicn.faceplusplus.com/v2/detection/detect?api_key=decd8b8ef8aa8a98c45aa9e7b6d9b8ba&api_secret=f2CPky4XtPDxfRvO9G06UowNHY0DtxvO&url="+pic_url  #获取到图片id的地址
    data=json.loads(post(url1)) #转换成JSON文件
    print data
    face_id=data['face'][0]['face_id']  #获取到face_id
    print face_id
    face_id=face_id.encode("utf-8") #编码，将UNICODE编码成str
    url2="http://apicn.faceplusplus.com/v2/detection/landmark?api_key=decd8b8ef8aa8a98c45aa9e7b6d9b8ba&api_secret=f2CPky4XtPDxfRvO9G06UowNHY0DtxvO&face_id="+face_id    #获取点的网址
    data2=json.loads(post(url2))    
    x=[]
    y=[]
    dict=data2['result'][0]['landmark'] #获取到含有点信息的dict
    for k,v in dict.iteritems():
        x.append(v['x'])    #添加到LIST
        y.append(v['y'])
    return x,y
if __name__ == '__main__':
    x=[]
    y=[]
    x,y=main()
    f = open('112.txt','w')
    for i in range(len(x)):
        # print x[i],y[i]
        #f.write("\r\n")
        f.write(str(x[i])+' '+str(y[i])+"\r\n")
    f.close()
