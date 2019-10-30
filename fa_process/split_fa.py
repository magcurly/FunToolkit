import re,os,sys
import argparse
from Bio import SeqIO



def split_fa(filename,num,prefix):
    seq_list=list(SeqIO.parse(filename,"fasta"))
    total_num=len(seq_list)
    each_num=total_num/num
    if each_num != int(each_num):
        each_num=int(each_num)+1
    count=0
    file_num=0
    fa_list=[]
    sub_seq=[]
    for seq_r in seq_list:
        sub_seq.append(seq_r)
        count+=1
        if count >each_num:
            file_num+=1
            fa_file=prefix+"_"+file_num+".fa"
            fa_list.append(fa_file)
            SeqIO.write(sub_seq,fa_file,"fasta")
            count=0            
            sub_seq=[]
    
    return fa_list
    

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--fa_file','-f',help="Input Fasta File for Slicing")
    parser.add_argument('--prefix'，'-p',help='Output Prefix (output directory inclued)')
    parser.add_argument('--number','-n',help='Identify How many files to be split')
    args=parser.parse_args()
    fa_file_list=split_fa(args.fa_file,args.number,args.prefix)
    fa_list_file=args.prefix+"_fa.list"
    with open(fa_list_file,'w') as handle:
        handle.write('\n'.join(fa_file_list))

main()