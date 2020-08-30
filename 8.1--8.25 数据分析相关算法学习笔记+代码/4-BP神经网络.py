import pandas as pd
import numpy as np
data_tr=pd.read_csv('./BPdata_tr.txt')
yita=0.05#学习速率
n=len(data_tr)
def sigmoid(x):#网络激活函数
    return 1/(1+np.exp(-x))
net_in=np.array([])#网络输入
out_in=np.array([0,0,0,0,-1])#输出层的输入
real=pd.read_csv('./BPdata_te.txt')
w_mid=np.zeros([3,4])#隐层神经元的权值&阈值
w_out=np.zeros([5])#输出层神经元的权值&阈值
delta_w_out=np.zeros([5])#输出层权值&阈值修正量
delta_w_mid=np.zeros([3,4])#中间层权值&阈值的修正量
for it in range(n):
    net_in=np.array([data_tr.iloc[it,0],data_tr.iloc[it,1],-1])#网络输入
    real=data_tr.iloc[it,2]
    for i in range(4):
        out_in[i]=sigmoid(sum(net_in*w_mid[:,i]))#从输入到隐层的传输过程
    res=sigmoid(sum(out_in*w_out))#模型预测值
    print(it,'个样本的模型输出',res,'real:',real)
    delta_w_out=yita*res*(1-res)*(real-res)*out_in#输出层权值的修正量
    delta_w_out[4] = -yita*res*(1-res)*(real-res)
    w_out=w_out+delta_w_out#更新
    for i in range(4):
        delta_w_mid[:,i]=yita*out_in[i]*(1-out_in[i])*w_out[i]*res*(1-res)*(real-res)*net_in#中间层神经元的权值修正量
        delta_w_mid[2,i]=yita*out_in[i]*(1-out_in[i])*w_out[i]*res*(1-res)*(real-res)#中间层神经元的阈值修正量
 #训练好后导入测试集进行测试
 data_te=pd.read_csv('./BPdata_te.txt')
 import matplotlib.pyplot as plt
error_te=[]
for it in range(len(data_te)):
    net_in=np.array([data_te.iloc[it,0],data_te.iloc[it,1],-1])#网络输入
    real=data_tr.iloc[it,2]
    for i in range(4):
        out_in[i]=sigmoid(sum(net_in*w_mid[:,i]))#从输入到隐层的传输过程
    res=sigmoid(sum(out_in*w_out))#模型预测值
    error=res-real
    error_te.append(abs(error))
plt.plot(error_te)
plt.show()

