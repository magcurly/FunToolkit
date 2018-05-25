#Build a SQL database before performing the annotation
library("taxonomizr")
read.accession2taxid(list.files('/hwfssz1/ST_META/PN/zhujiahui/bacteria-gene/script/nt','accession2taxid.gz$'),'accessionTaxa.sql')
