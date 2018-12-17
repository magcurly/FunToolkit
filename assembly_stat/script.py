import shutil
import os
import sys

def script(rmhost_list,sample_list,pro):
    workdir=os.getcwd()
    ls=open(rmhost_list).readlines()
    bms=open(sample_list,'r')
    process=pro.split(',')
    sample={}
    for line in bms.readline():
        line=line.strip('\n')
        arr=line.split('\t')
        sample[arr[1]]=arr[0]
    bms.close()

    if 'idba' in process:
        idba_file=os.path.join(workdir,'idba.ass.sh')
        idba_ass=open(idba_file,'w')
        idba_ud=shutil.which('idba_ud')
        fq2fa=shutil.which('fq2fa')
    if 'bwa' in process:
        bwa_path=os.path.join(workdir,'bwa.sh')
        bwa_file=open(bwa_file,'w')
        bwa=shutil.whhich('bwa')
    if 'orf' in process:
        orf_path=os.path.join(workdir,'orf.sh')
        orf
    for i in range(0,len(ls),2):
        line1=ls[i]
        line2=ls[i+1]
        if 'idba' in process:
            script='if [ -f '+line1+' ];then'+'\n\tzcat '+line1+'>'+
            

