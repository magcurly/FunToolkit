import os,sys,re

def parse_lineage(seq2tax_file):
    seq2tax={}
    for line in open(seq2tax_file.'r').readlines():
        line=line.strip()
        arr=line.split('\t')
        arr[-1]=arr[-1][:-1]
        lineage=arr[-1].split(';')
        for i in range(0,len(lineage)):lineage[i]=lineage[i].strip()
        seq2tax[arr[1]]=lineage
    return seq2tax

def parse_len(len_file):
    gid2seq={}
    for line in open(len_file,'r').readlines():
        line=line.strip()
        arr=line.split('\t')
        gid2seq[arr[0]]=arr[1]
    return gid2seq

def main():
    taxon_lineage=sys.argv[1]
    len_file
    seq2tax=parse_lineage(taxon_lineage)
    gid2seq=parse_len(len_file)
    for key in gid2seq:
        if seq2tax[gid2seq[key]]:
            
