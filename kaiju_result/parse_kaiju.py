import sys,os,re

#def (parameter_list):
#    pass

file=open(sys.argv[1],'r')
#Output file
prefix=sys.argv[2]
kingdom=open(prefix+'_kingdom','w')
phylum=open(prefix+'_phylum','w')
class_tax=open(prefix+'_class','w')
order=open(prefix+'_order','w')
family=open(prefix+'_family','w')
genus=open(prefix+'_genus','w')
species=open(prefix+'_species','w')
#Parsing the kaiju result
for line in file:
    line=line.strip('\n')
    arr=line.split('\t')
    if arr[0]=='C':
        tax=arr[-1]
        tax=re.sub('NA','Unclassified',tax)
        taxon=tax.split('; ')
        if taxon[-1]=='': taxon.pop()
    elif arr[0]=='U':
        tax='Unclassified'
        taxon=[tax]*7
    seqID=arr[1]
    kingdom.write(seqID+'\t'+taxon[0]+'\n')
    phylum.write(seqID+'\t'+taxon[1]+'\n')
    class_tax.write(seqID+'\t'+taxon[2]+'\n')
    order.write(seqID+'\t'+taxon[3]+'\n')
    family.write(seqID+'\t'+taxon[4]+'\n')
    genus.write(seqID+'\t'+taxon[5]+'\n')
    species.write(seqID+'\t'+taxon[6]+'\n' )
    
file.close()
kingdom.close()
phylum.close()
class_tax.close()
order.close()
family.close()
genus.close()
species.close()
