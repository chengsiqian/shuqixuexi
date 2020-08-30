import pandas as pd
data=pd.read_csv('./titanic_data.csv')
data.drop('PassengerId',axis=1,inplace=True)
data.loc[data['Sex']=='male','Sex']=1#用数值1来代替MALE
data.loc[data['Sex']=='female','Sex']=0
data.fillna(data['Age'].mean(),inplace=True)#用均值来填充缺失值
data
#************数据预处理****************
#************模型构建与预测************
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
DecisionTreeClassifier(max_depth=5,random_state=8)
Dtc.fit(data.iloc[:,1:],data['Survived'])#模型训练
pre=Dtc.predict(data.iloc[:,1:])#模型预测
pre==data['Survived']#比较模型预测值与样本实际值是否一致
classification_report(data['Survived'],pre)#模型分类报告
#************决策树可视化************
dot_data=export_graphviz(Dtc,feature_names=['Pclass','Sex','Age'],class_names='Survived')
graph=graphviz.Source(dot_data)
graph