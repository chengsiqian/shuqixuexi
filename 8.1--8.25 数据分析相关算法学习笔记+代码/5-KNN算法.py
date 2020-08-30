#计算距离函数。
#type = c("O", "I", "F", "M", "2")
distance<-function(train_data,obse,type)
{
	r<-nrow(train_data)
	near_distance<-matrix(nrow=r,ncol=1)
	for(i in 1:r){
		near_distance[i]<-norm(cbind(train_data[i,]-obse),type)		
	}
	return (near_distance)
}

#计算与所有的训练集之间的距离关系
knn<-function(train_data,obse,type,calcols,classcol,idcol)
{
	d<-distance(train_data[,calcols],obse,type)
	return (data.frame(train_data[,idcol],train_data[,classcol],d))
}
#用knn来预测点属于的类别
#train_data  训练集matrix格式
#obse	     要预测对象
#type        计算距离采用的范数类型
#calcols     那些列参与计算距离
#classcol    类别标志类
#idcol       唯一标识每个训练对象的列
#k           k邻近里面的k值
knn_classi<-function(train_data,obse,type,calcols,classcol,idcol,k)
{
		all_near<-knn(train_data,obse,type,calcols,classcol,idcol)
		all_near<-all_near[order(all_near[,3]),]
		r<-nrow(all_near)
		cla<-unique(all_near[,2])
		probs<-matrix(cla,ncol=2,nrow=length(cla),byrow=FALSE)
		k_nearest<-all_near[1:k,]
		freqs<-as.data.frame(table(k_nearest[,2]))
		freqs[,2]<-freqs[,2]/k
		#probs[,2]=probs[,2]/k
		colnames(freqs)<-c("class","probs")
		freqs<-freqs[order(freqs[,2],decreasing = TRUE),]
		return (freqs[1,])
}