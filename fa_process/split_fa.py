import re,os,sys
import argparse
from Bio import SeqIO



def split_fa_rn(filename,num,prefix): #split fa file based on sequence number
    seq_list=list(SeqIO.parse(filename,"fasta"))
    total_num=len(seq_list)
    ave_num=total_num/num
    if ave_num != int(ave_num):
        ave_num=int(ave_num)+1
    count=0
    file_num=0
    fa_list=[]
    sub_seq=[]
    for seq_r in seq_list:
        sub_seq.append(seq_r)
        count+=1
        if count >=ave_num:
            file_num+=1
            fa_file=prefix+"_"+file_num+".fa"
            fa_list.append(fa_file)
            SeqIO.write(sub_seq,fa_file,"fasta")
            count=0            
            sub_seq=[]
    if count !=0:
        file_num+=1
        fa_file=prefix+"_"+file_num+".fa"
        fa_list.append(fa_file)
        SeqIO.write(sub_seq,fa_file,"fasta")
    
    return fa_list

def split_fa_fs(filename,num,prefix): #split fa file based on file size
    seq_list=list(SeqIO.parse(filename,"fasta"))
    total_size=0
    for seq_rec in seq_list:
        total_size+=len(seq_rec.seq)
    ave_size=total_size/num
    if ave_size != int(ave_size):ave_size=int(ave_size)+1
    count=0
    file_num=0
    fa_list=[]
    sub_seq=[]
    for seq_r in seq_list:
        sub_seq.append(seq_r)
        count+=len(seq_r.seq)
        if count>=ave_size:
            file_num+=1
            fa_file=prefix+"_"+file_num+".fa"
            fa_list.append(fa_file)
            SeqIO.write(sub_seq,fa_file,"fasta")
            count=0            
            sub_seq=[]
    if count !=0:
        file_num+=1
        fa_file=prefix+"_"+file_num+".fa"
        fa_list.append(fa_file)
        SeqIO.write(sub_seq,fa_file,"fasta")
    return fa_list

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--fa_file','-f',help="Input Fasta File for Slicing")
    parser.add_argument('--prefix'，'-p',help='Output Prefix (output directory inclued)')
    parser.add_argument('--number','-n',help='Identify How many files to be split')
    parser.add_argument('--type','-t',default="file",help='Type of split, based on file size or seq number')
    args=parser.parse_args()
    if arg
    fa_file_list=split_fa(args.fa_file,args.number,args.prefix)
    fa_list_file=args.prefix+"_fa.list"
    with open(fa_list_file,'w') as handle:
        handle.write('\n'.join(fa_file_list))

main()