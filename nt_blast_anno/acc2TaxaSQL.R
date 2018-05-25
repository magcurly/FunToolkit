#Build an ass2tax SQL database before performing the annotation
library("taxonomizr")
read.accession2taxid(list.files('/Path/to/','accession2taxid.gz$'),'/path/to/your/accessionTaxa.sql')

#The directory must contain 4 files to build the sql database as following: 
#nucl_est.accession2taxid.gz
#nucl_gb.accession2taxid.gz
#nucl_gss.accession2taxid.gz
#nucl_wgs.accession2taxid.gz
