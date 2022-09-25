import numpy as np
from numpy import trapz
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
#1.3.1
#a=np.arange(64).reshape(8,8)
#for i in range(8):
#    for j in range(8):
#        a[i,j]=(i+j)%2
#print(a)

#1.3.2
#a=np.arange(25).reshape(5,5)
#for i in range(5):
#    for j in range(5):
#        a[i,j]=j
#print(a)

#1.3.3
#a=np.random.random((3,3,3))
#print(a)

#1.3.4
#n=input()
#n=int(n)
#a=np.arange(n*n).reshape(n,n)
#for i in range(n):
#    for j in range(n):
#        if(j==0)or(i==0)or(j==n-1)or(n-1==i):
#            a[i,j]=0
#        else:
#            a[i,j]=1
#print(a)

#1.3.5
#n=input()
#n=int(n)
#a=np.random.random((n))
#print(a)
#a=np.sort(a)
#a=np.flip(a)
#print(a)

#1.3.6
#n=input()
#n=int(n)
#a=np.arange(n*n).reshape(n,n)
#print(a.shape,a.size,a.ndim)

#2.3.1
#s1=pd.Series([2,2],["x","y"])
#s2=pd.Series([1,1],["x","y"])
#print(np.sqrt(np.power(s1["x"]-s2["x"], 2)+np.power(s1["y"]-s2["y"], 2)))

#2.3.2/2.3.3
#url='https://raw.githubusercontent.com/akmand/datasets/main/FMLPDA_Table4_3.csv'
#dataframe=pd.read_csv(url)
#dataframe.head(5)
#dataframe.tail(5)
#print(dataframe.shape)
#print(dataframe.describe())


#3.3.2
# df = pd.read_csv("https://raw.githubusercontent.com/akmand/datasets/master/iris.csv")
# sepal_length_cm = preprocessing.normalize([np.array(df["sepal_length_cm"])])
# print("\nsepal_length_cm с использованием минимаксного преобразования: \n", sepal_length_cm,"\n")
# sepal_width_cm = np.array(df["sepal_width_cm"])
# sepal_width_cm = (sepal_width_cm - sepal_width_cm.mean())/sepal_width_cm.std()
# print("sepal_width_cm  с задействованием z-масштабирования:\n",sepal_width_cm)
