// ConsoleApplication3.cpp : 定义控制台应用程序的入口点。

#include "stdafx.h"
#include <opencv2/opencv.hpp>
#include <iostream>
#include <fstream>
#include <istream>
using namespace std;
using namespace cv;
int _tmain(int argc, _TCHAR* argv[])
{
	char filename[100];
	char file_dst[100];
	char filename_txt[100];

	for(int i=1;i<=4;i++)
	{
	//读取照片,运行前请更改图片文件夹路径
  sprintf(filename,"C:/Users/Administrator/Desktop/Face++/pic/%d.jpg",i);
IplImage* src=cvLoadImage(filename,1);
IplImage* dst=cvCreateImage(cvGetSize(src),src->depth,src->nChannels);
cvCopy(src, dst, NULL);

	int wimag=dst->height;//高
	int himag=dst->width;
	//读取数据，运行前请更改文本数据文件路径
	 sprintf(filename_txt,"C:/Users/Administrator/Desktop/Face++/%d.txt",i);
	ifstream inpin(filename_txt);//加载名称
	float xdata,ydata;
	int x,y;
	int r=5;
	while(!inpin.eof())
	{
		inpin>>xdata;
		inpin>>ydata;
		y=wimag*ydata*0.01;
		x=himag*xdata*0.01;
		Point center=Point(x,y);
		cvCircle(dst,center,r,Scalar(0,0,255),-1);
	}
//输出处理后的照片，运行前请确定输出文件夹
	sprintf(file_dst,"D:\\%d.jpg",i);
     cvSaveImage(file_dst,dst);
	}
	waitKey(0);
	return 0;
}



