args<-commandArgs(T)
library("taxonomizr") # This is an R library that is able to achieve taxonomic annotation to NCBI Blast results.
taxaNodes<-read.nodes('/Path/to/your/nodes.dmp')
taxaNames<-read.names('/Path/to/your/names.dmp')

library("hash") # Introduce hash into R Script
h=hash()
h2=hash()

processFile = function(filepath) {
  con = file(filepath, "r")
  
  while ( TRUE ) {
    line = readLines(con, n = 1)
    if ( length(line) == 0 ) {
      break
    }
    k <- unlist(strsplit(line,"\t"))
		if(as.numeric(k[4])<=200){next} #Filter results that the alignment length is less than 200 bps
    if (has.key(k[1],h)){
		if(k[2]==h[[k[1]]]){ 
			h2[[k[1]]] <- rbind(h2[[k[1]]],data.frame(as.numeric(k[7:8]))) #To calculate the coverage
			}
        next
    }
    .set(h,keys=k[1],values=k[2]) #To Choose the Best Hit
    .set(h2,keys=k[1],values=data.frame(as.numeric(k[7:8]))) #get the alignment region
  }

  close(con)
}

processFile(args[1])

p <- data.frame(values(h))

#To get the taxonomic annotation
t <- as.character(p[,1])
n <- rownames(p)
taxaID <- accessionToTaxa(t,"/path/to/your/accessionTaxa.sql")
taxa <- getTaxonomy(taxaID,taxaNodes,taxaNames)
acc2taxa <- data.frame(n,t,taxaID,taxa)
colnames(acc2taxa)[1:3] <- c("Scaffold","Accession ID","Tax ID")
write.table(acc2taxa,args[2],quote=F,row.names=F) 

#This is a part that is unfinished
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
