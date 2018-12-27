import sys,os
import urllib.request
import re
import taxid_lineage_full as t

tax_file = open(sys.argv[1],'r')

tax={}
for line in tax_file:
    line=line.strip('( )*\n')
    arr=line.split('\t')
    if arr[5] not in tax:
        #print(arr[5])
        tax[arr[5]]=t.tax_object(arr[4],arr[5])
        tax[arr[5]].assign4tax()
        p_id=tax[arr[5]]._parent_txid
        p_name=tax[arr[5]]._parent_name
        while p_id not in tax:
            #print(p)
            tax[p_id]=t.tax_object(p_name,p_id)
            tax[p_id].assign4tax()
            #print(tax[p_id]._name)
            if tax[p_id]._rank == 'phylum':
                break
            p_name=tax[p_id]._parent_name
            p_id=tax[p_id]._parent_txid
            
tax_file.close()

#print(list(tax.keys()))

tax_table=open(sys.argv[2],'w')
tax_table.write('NCBI_ID'+'\t'+'Parent_NCBI_ID'+'\t'+'Organism_Name'+'\t'+'Level'+'\t'+'Lineage'+'\n')
for k in sorted(list(tax.keys())):
    tax_table.write(tax[k].printtax_tree()+'\n')

tax_table.close()