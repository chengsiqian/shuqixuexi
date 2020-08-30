#python实现K-Means
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
iris=load_iris()
model = KMeans(n_clusters=3).fit(iris.data)
model.labels_
#模型评估
from sklearn.metrics import jaccard_similarity_score
pre=model.labels_
pre==iris.target
jaccard_similarity_score(iris.target,pre)