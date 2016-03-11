// ConsoleApplication3.cpp : �������̨Ӧ�ó������ڵ㡣

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
	//��ȡ��Ƭ,����ǰ�����ͼƬ�ļ���·��
  sprintf(filename,"C:/Users/Administrator/Desktop/Face++/pic/%d.jpg",i);
IplImage* src=cvLoadImage(filename,1);
IplImage* dst=cvCreateImage(cvGetSize(src),src->depth,src->nChannels);
cvCopy(src, dst, NULL);

	int wimag=dst->height;//��
	int himag=dst->width;
	//��ȡ���ݣ�����ǰ������ı������ļ�·��
	 sprintf(filename_txt,"C:/Users/Administrator/Desktop/Face++/%d.txt",i);
	ifstream inpin(filename_txt);//��������
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
//�����������Ƭ������ǰ��ȷ������ļ���
	sprintf(file_dst,"D:\\%d.jpg",i);
     cvSaveImage(file_dst,dst);
	}
	waitKey(0);
	return 0;
}



