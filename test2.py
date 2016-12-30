# -*- coding: utf-8 -*-
import numpy
import math
import scipy
import scipy.io as sio
import numpy as np

'''#读数据
print "Start"
mat = sio.loadmat('C:\Users\Smilleen\Desktop\RICK\Monday1.mat')
#print mat
data =mat['monday1']
#print data
monday = data[0]
#print monday
print "Done"
#测试数据
test=monday[0:2]
#print type(test)
print "ok"'''
#距离函数
def dist(p,q):
	a=np.square(p[0]-q[0])
	b=np.square(p[1]-q[1])
	d=math.sqrt(a+b)
	return d
#夹角函数
def ftheta(p,q):
	cos_angle=(q[1]-p[1])/dist(p,q)
	angle=np.arccos(cos_angle)
	return angle
	
L=[[[1,1],[2,2],[3,2]],[[0,0],[1,0],[1,1],[2,2]]]
for tra in L:
	for i in range(len(tra)-1):
		tra[i].append(ftheta(tra[i],tra[i+1]))
print L

p=[116.1157379150391503906,39.854122161865234]
q=[116.11576843261719,39.85401153564453]
print dist(p,q)
print ftheta(p,q)