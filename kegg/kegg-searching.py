import sys,os
import urllib.request
import re

kegg="https://www.kegg.jp"
search_url=kegg+"/dbget-bin/www_bfind_sub?mode=bfind&max_hit=1000&locale=en&serv=kegg&dbkey=mgenes&keywords=baiG&page=1"
search_html=urllib.request.urlopen(search_url).read()
search_html=search_html.decode('utf-8')
kegg_seq=re.findall(r'(\w+:\d+)</a><br><div style="margin-left:2em"> ([\w]+; [\w\s]+)',search_html)
dict_kegg={}
for item in kegg_seq:
    dict_kegg[item[0]]=item[0]+";"+item[1]

ls=list(dict_kegg.keys())
#searching for sequence
url=kegg+"/dbget-bin/www_bget?"

download_fasta=open('baiG.fasta','w')
for accession in ls:
    target_url=url+accession
    html=urllib.request.urlopen(target_url).read()
    html=html.decode('utf-8')
    num=re.findall(r'(\d+ aa)',html)
    download_fasta.write('>'+dict_kegg[accession]+";"+num[0]+'\n')
    m=re.findall(r'\n([A-Z]+)(<br>|</td></tr>)',html)
    seq=''
    for j in m:
        seq+=j[0]
    download_fasta.write(seq+'\n')

download_fasta.close()