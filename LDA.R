args <- commandArgs(T)
train_data <- read.table(args[1],header=T,check.names=F)
test_data <- read.table(args[2],header=T,check.names=F)
train_gr <- read.table(args[3],header=T,check.names=F)
train_data <- data.frame(t(train_data),train_gr)
train_data$gr <- as.character(train_data$gr)
test_gr <- read.table(args[4],header=T,check.names=F)
test_data <- data.frame(t(test_data),test_gr)
test_data$gr <- as.character(test_data$gr)

sink(gsub(" ","",paste(args[5],".lda")))
library(MASS)
model <- lda(gr~.,train_data)
model_pre <- predict(model,test_data)
model_pre
table(test_data$gr,model_pre$class)
sink()

#This is a R script to do the LDA test. Please prepare your R with package "MASS".
#I use read.table and header=T here.Please make sure your first line of your group info file is "(Tab)gr" and your first column is your samples' name. 
#Besides, in order to co-work with the perl script in this project, please make sure your data set file start with "(Tab)Sample1(Tab)Sample2..." and your first column is your variables' name.
#Hope you find it super useful!
#If you have better idea, please add a comment.
