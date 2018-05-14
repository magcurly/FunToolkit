args <- commandArgs(T)
library("ade4")
library("RColorBrewer")
data <- read.table(args[1],header=T,check.names=F)
data <- as.matrix(data)
rs <- rowSums(data)
data <- data[rs!=0,]
cn <- colnames(data)
cn <- gsub("X","",cn)
colnames(data) <- cn
data <- sweep(data,2,apply(data,2,sum),"/")
data <- sqrt(data)
data.dudi <- dudi.pca(t(data),scale = F, scannf = F,nf = ncol(data))
ratio <- inertia.dudi(data.dudi)

pca1 <- as.numeric(sprintf("%0.2f",(ratio$TOT)[1,3]))
pca2 <- as.numeric(sprintf("%0.2f",((ratio$TOT)[2,3]-(ratio$TOT)[1,3])))

xmax <- max(data.dudi$li[,1])
xmin <- min(data.dudi$li[,1])
ymax <- max(data.dudi$li[,2])
ymin <- min(data.dudi$li[,2])

#gsub("^\\s+|\\s+$", "", args[2])
#outdir=gsub(" ","", paste(args[2],"a"))
#print(outdir)
write.table(data.dudi$c1,file=gsub(" ","",paste(args[3],"/PCA_",args[4],"_col_normes_scores.txt")), sep="  ", quote=F)
write.table(data.dudi$l1,file=gsub(" ","",paste(args[3],"/PCA_",args[4],"_row_normes_scores.txt")), sep="  ", quote=F)
write.table(data.dudi$co,file=gsub(" ","",paste(args[3],"/PCA_",args[4],"_coorinates.txt")), sep=" ", quote=F)
write.table(data.dudi$li,file=gsub(" ","",paste(args[3],"/PCA_",args[4],"_princomp.txt")), sep="   ", quote=F)

library(ggplot2)
library(grid)

dat = data.frame(data.dudi$li[,1:2])
#groups = c("IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","IBD","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","Healthy","UC","UC","UC","UC","UC","UC","UC","UC")
gr <- read.table(args[2],check.names=F)
groups <- gr[,2]

pdf(gsub(" ","",paste(args[3],"/PCA_",args[4],".pdf")), 8, 7)
groups2<-as.factor(groups)
adjst1<- (max(dat[,1])-min(dat[,1]))*0.1
adjst2<- (max(dat[,2])-min(dat[,2]))*0.1
par(mai=c(1,1,0.5,2),bty="n")
p = c(17,17,20,20,20,20)

#p
col_pool <- brewer.pal(nlevels(groups2),"Set1")
#col_pool
plot(dat,pch=p[as.numeric(groups2)],cex=1,col=col_pool[as.numeric(groups2)],xlim=c(min(dat[,1])-adjst1,max(dat[,1])+adjst1), ylim=c(min(dat[,2])-adjst2,max(dat[,2])+adjst2),main="PCA based on species profile",xlab=paste("PC1","(",pca1,"%",")",sep=""),ylab=paste("PC2","(",pca2,"%",")",sep=""),bty="o")
#text(dat[,1],dat[,2],row.names(dat),pos=3,cex=0.6,col=col_pool)

grid(col="grey")
abline(h=0)
abline(v=0)
#lines(c((dat["CL100018628_L02_32",1]+dat["CL100018628_L02_34",1])/2,(dat["CL100018628_L02_35",1]+dat["CL100018628_L02_36",1])/2),c((dat["CL100018628_L02_32",2]+dat["CL100018628_L02_34",2])/2,(dat["CL100018628_L02_35",2]+dat["CL100018628_L02_36",2])/2),lty=3,lwd=1)
arrows((dat["CL100018628_L02_37",1]+dat["CL100018628_L02_38",1])/2,(dat["CL100018628_L02_37",2]+dat["CL100018628_L02_38",2])/2,(dat["CL100018628_L02_39",1]+dat["CL100018628_L02_40",1])/2,(dat["CL100018628_L02_39",2]+dat["CL100018628_L02_40",2])/2,length=0.05,lty=5,lwd=1)
arrows((dat["CL100018628_L02_39",1]+dat["CL100018628_L02_40",1])/2,(dat["CL100018628_L02_39",2]+dat["CL100018628_L02_40",2])/2,(dat["CL100018628_L02_32",1]+dat["CL100018628_L02_34",1])/2,(dat["CL100018628_L02_32",2]+dat["CL100018628_L02_34",2])/2,length=0.05,lty=5,lwd=1)
arrows((dat["CL100018628_L02_39",1]+dat["CL100018628_L02_40",1])/2,(dat["CL100018628_L02_39",2]+dat["CL100018628_L02_40",2])/2,(dat["CL100018628_L02_35",1]+dat["CL100018628_L02_36",1])/2,(dat["CL100018628_L02_35",2]+dat["CL100018628_L02_36",2])/2,length=0.05,lty=5,lwd=1)
text((dat["CL100018628_L02_37",1]+dat["CL100018628_L02_38",1])/2,(dat["CL100018628_L02_37",2]+dat["CL100018628_L02_38",2])/2,"UC_1106",pos=1,cex=0.6,col="black")
text((dat["CL100018628_L02_39",1]+dat["CL100018628_L02_40",1])/2,(dat["CL100018628_L02_39",2]+dat["CL100018628_L02_40",2])/2,"UC_1114",pos=1,cex=0.6,col="black")
text((dat["CL100018628_L02_32",1]+dat["CL100018628_L02_34",1])/2,(dat["CL100018628_L02_32",2]+dat["CL100018628_L02_34",2])/2,"UC_0119",pos=1,cex=0.6,col="black")
text((dat["CL100018628_L02_35",1]+dat["CL100018628_L02_36",1])/2,(dat["CL100018628_L02_35",2]+dat["CL100018628_L02_36",2])/2,"UC_0119B",pos=1,cex=0.6,col="black")
legend(par("usr")[2],par("usr")[4],cex=1,x.intersp=0.4,pt.cex=1,unique(groups),pch=p,col=col_pool,text.font=2,ncol=1,xpd=TRUE,bty="o")

#s.class(dfxy = dat, fac = groups2, col=col_pool, xax = 1, yax = 2 ,add.plot = TRUE )
dev.off()
