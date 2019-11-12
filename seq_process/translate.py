import re,os,sys,argparse
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import generic_dna
import gzip

def translate_dna(input_handle,output_handle,table_code):
    for seq_rec in SeqIO.parse(input_handle,'fasta'):
        info=seq_rec.description
        detail=re.search('# (\S+) # ID=\w+;partial=(\d+);start_type=(\w+)',info)
        protein=seq_rec.translate(table=11)
        pro_str=str(protein.seq)
        if detail.group(2)!='11': ##This filtered out all sequences with at least a start codon or a stop codon
            if detail.group(2)=='00' or detail.group(3) == "Edge": ##This filtered out all sequences with a stop codon
                pro_str=re.sub(r'\*$','',pro_str)  ##Remove the stop codon at the end of the amino acid sequence
        pro_str=re.sub(r'\*','X',pro_str) ##due to the translational readthrough, make uncertain aa to Xaa
        protein.seq=Seq(pro_str) ##Redefine the protein seq
        protein.description=info
        protein.id=seq_rec.id
        output_handle.write(protein.format('fasta'))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input','-i', help='fasta file with DNA needs to be translated')
    parser.add_argument('--output','-o',help='output amino acid sequences in fasta format')
    parser.add_argument('--table','-t',default=11,help='codon table, default is 11 ')
    args=parser.parse_args()
    if re.search(r'gz',args.input):
        input_handle=gzip.open(args.input,'rt')
    else:
        input_handle=open(args.input,'rt')
    output_handle=open(args.output,'w')
    translate_dna(input_handle,output_handle,args.table)
    input_handle.close()
    output_handle.close()

main()
    