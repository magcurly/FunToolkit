args<-commandArgs(T)
library("taxonomizr")
#read.accession2taxid(list.files('/hwfssz1/ST_META/PN/zhujiahui/bacteria-gene/script/nt','accession2taxid.gz$'),'accessionTaxa.sql')
taxaNodes<-read.nodes('/hwfssz1/ST_META/PN/zhujiahui/bacteria-gene/script/03.taxo/nt/nodes.dmp')
taxaNames<-read.names('/hwfssz1/ST_META/PN/zhujiahui/bacteria-gene/script/03.taxo/nt/names.dmp')

#blast <- read.table(args[1],header=F,check.names=F)
#blast <- files(args[1],'r')
library("hash")
h=hash()
h2=hash()
#t=list()
processFile = function(filepath) {
  con = file(filepath, "r")
  
  while ( TRUE ) {
    line = readLines(con, n = 1)
    if ( length(line) == 0 ) {
      break
    }
    k <- unlist(strsplit(line,"\t"))
		if(as.numeric(k[4])<=200){next}
    if (has.key(k[1],h)){
		if(k[2]==h[[k[1]]]){
			h2[[k[1]]] <- rbind(h2[[k[1]]],data.frame(as.numeric(k[7:8])))
			}
        next
    }
    .set(h,keys=k[1],values=k[2])
    .set(h2,keys=k[1],values=data.frame(as.numeric(k[7:8])))
  }

  close(con)
}

processFile(args[1])

p <- data.frame(values(h))
t <- as.character(p[,1])
n <- rownames(p)
taxaID <- accessionToTaxa(t,"/hwfssz1/ST_META/PN/zhujiahui/bacteria-gene/script/03.taxo/nt/accessionTaxa.sql")
taxa <- getTaxonomy(taxaID,taxaNodes,taxaNames)
acc2taxa <- data.frame(n,t,taxaID,taxa)
#h2 = hash(as.character(n),t)
#h3 = hash(as.character(n),acc2taxa$species)
colnames(acc2taxa)[1:3] <- c("Scaffold","Accession ID","Tax ID")
##acc <- as.character(blast[,2])
##taxaID <- accessionToTaxa(acc,"accessionTaxa.sql")
##taxa <- getTaxonomy(taxaID,taxaNodes,taxaNames)
##rows <- rownames(taxa)
##acc2taxa <- data.frame(blast[,1],rows,taxa)
##rownames(acc2taxa)[1:2] <- c("Scaffold","Taxa ID")

write.table(acc2taxa,args[2],quote=F,row.names=F)
count=data.frame()
index=keys(h2)
for(i in index){
	arr <- h2[[i]][order(h2[[i]][,1]),]
	len = arr[1,2]-arr[1,1]
	start=arr[1,1]
	end = arr[1,2]
	lengtha=length(arr[,1])
	for(j in 2:lengtha){
		if(arr[j,1] > end){
			len = len + (arr[j,2]-arr[j,1]+1)
			start = arr[j,1]
			end = arr[j,2]
		}else{
			if(arr[j,2] > end){
				len = len + (arr[j,2]-end)
				end = arr[j,2]
			}
		}
	}
	li=data.frame(i,h3[[i]],len)
	count <- rbind(count,li)
}
write.table(count,args[3],quote=F,row.names=F)
