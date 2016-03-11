#coding=utf-8 
import urllib,os
import urllib2
import json
import facepp
#获取到网页内容的函数
API_KEY ='decd8b8ef8aa8a98c45aa9e7b6d9b8ba'
API_SECRET ='f2CPky4XtPDxfRvO9G06UowNHY0DtxvO'
api = facepp.API(API_KEY, API_SECRET)
def post(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    return response.read()
#文件目录中请勿出现中文字符，图片名默认为1.jpg,2.jpg....i.jpg
def main(filename):
    file = os.getcwd()+"\\pic\\"+filename
    print file
    data2 = api.detection.detect(img =facepp.File(file))
    face_id=data2['face'][0]['face_id']
    face_id=face_id.encode("utf-8")
    url2="http://apicn.faceplusplus.com/v2/detection/landmark?api_key=%s&api_secret=%s&face_id=%s"%(API_KEY,API_SECRET,face_id)    #获取点的网址
    data2=json.loads(post(url2))    
    x=[]
    y=[]
    dict=data2['result'][0]['landmark'] #获取到含有点信息的dict
    for k,v in dict.iteritems():
        x.append(v['x'])    #添加到LIST
        y.append(v['y'])
    return x,y
if __name__ == '__main__':
    piclist = os.listdir("%s\\pic"%os.getcwd())
    for each in piclist:
        #print each.split(".")[0] 
        x=[]
        y=[]
        x,y=main(each)
        f = open('%s.txt'%each.split(".")[0],'w')
        for i in range(len(x)):
            # print x[i],y[i]
            #f.write("\r\n")
            #输出文件为txt格式，默认名字为1.txt,2.txt.....i.txt等
            f.write(str(x[i])+' '+str(y[i])+"\r\n")
        f.close()
