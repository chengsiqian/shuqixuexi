from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
boston=load_boston()#实例化
x=boston.data[:,5:6]
clf.fit(boston.data[:,5:6],boston.target)
clf.coef_
y_pre=clf.predict(boston.data[:,5:6])
plt.scatter(x,boston.target)
plt.plot(x,y_pre,c='r')
plt.show()