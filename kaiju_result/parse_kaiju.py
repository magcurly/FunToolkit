import sys,os,re,argparse,shutil

def kaiju2seqtaxon(kaiju_output,taxon_level,outdir,prefix,node,name):
    taxon_names=shutil.which('addTaxonNames')
    outfile=outdir+'/'+prefix+'_kaiju_nameadded'
    tax_rank=','.join(taxon_level)
    cmd=taxon_names+' -r '+tax_rank+' -i '+kaiju_output+' -t '+node+' -n '+name+' -o '+outfile
    os.system(cmd)

    file=open(outfile,'r')
    output_file=[]
    for rank in taxon_level:
        rankfile=outdir+'/'+prefix+'_gene2'+rank+'.lst'
        r_o=open(rankfile,'w')
        output_file.append(r_o)
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
            taxon=[tax]*len(taxon_level)
        seqID=arr[1]
        for j in range(0,len(output_file)):
            string=seqID+'\t'+taxon[j]+'\n'
            output_file[j].write(string)
    file.close()
    for i in output_file:
        i.close()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-r','--levels',nargs='+',default=['phylum','genus','species'],help='Taxon level: phylum class order family genus species. Consistant with \'addTaxonNames\'. Default: -r phylum genus species')
    parser.add_argument('-o','--outdir',default='./',help='Output directory. Default: -o ./')
    parser.add_argument('-p','--prefix',default='kaiuju',help='Prefix of output file. Default: -p kaiju')
    parser.add_argument('-i','--input',help='Input file, Kaiju\'s Output')
    parser.add_argument('-t','--node',help='node.dmp file path')
    parser.add_argument('-n','--name',help='names.dmp file path')
    args=parser.parse_args()
    if args.input is None or args.node is None or args.name is None :
        parser.parse_args(['-h'])
        sys.exit(0)
    kaiju2seqtaxon(args.input,args.levels,args.outdir,args.prefix,args.node,args.name)
main()
