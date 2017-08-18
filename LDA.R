args <- commandArgs(T)
#data <- read.table("args[1]",header=T,check.names=F)
train_data <- read.table(args[1],header=T,check.names=F)
test_data <- read.table(args[2],header=T,check.names=F)
train_gr <- read.table(args[3],header=T,check.names=F)
train_data <- data.frame(t(train_data),train_gr)
train_data$gr <- as.character(train_data$gr)
test_gr <- read.table(args[4],header=T,check.names=F)
test_data <- data.frame(t(test_data),test_gr)
test_data$gr <- as.character(test_data$gr)

#groups <- read.table("/hwfssz1/ST_META/PN/zhujiahui/meta-analysis/test-cOMG/soap/tax/bms",check.names=F)

#gr <- groups[,2];
#dat <- data.frame(t(data),gr)
#train_data <- dat[1:85,]
#train_data$gr <- as.character(train_data$gr)
#test_data <- dat[86:93,]
#test_data$gr <- as.character(test_data$gr)
sink(gsub(" ","",paste(args[5],".lda")))
library(MASS)
model <- lda(gr~.,train_data)
model_pre <- predict(model,test_data)
model_pre
table(test_data$gr,model_pre$class)
sink()
