import sys,os
import urllib.request
import re
import taxid_lineage_full as t
#from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys

url = "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi"
#driver = webdriver.PhantomJS(executable_path='/mnt/f/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
if len(sys.argv)<3:
    try:
        sys.exit(0)
    except:
        print('python '+sys.argv[0]+' [input] [output]')

tax_file = open(sys.argv[1],'r')

tax={}
tax_line={}
for line in tax_file:
    line=line.strip('( )*\n')
    arr=line.split('\t')
    if arr[4] not in tax:
        tax[arr[4]]=1
#        tax[arr[4]]=t.tax_object(arr[4])
 #       tax[arr[4]].assign4tax()
    tax_line[arr[0]]=line
tax_file.close()
for i in tax:
    info={}
    word=re.sub(r'\s',r'+',i)
    target_url=url+'?mode=Undef&name='+word+'&lvl=0&srchmode=1&keep=1&unlock'
    #print(target_url)
    html=urllib.request.urlopen(target_url).read()
    html=html.decode('utf-8')
    m=re.findall(r'Taxonomy ID: (\d+)',html)
    info['taxid']=m[0]
    line=re.findall(r'id=(\d+)[\w&;=_"]+ TITLE=\"([\w ]+)\">([\w ]+)</a>',html)
    for i in line:
        if i[1] == 'genus':
            info['genus']='{}: {}'.format(i[2],i[0])
        elif i[1] == 'phylum':
            info['phylum']='{}: {}'.format(i[2],i[0])
    
    tax[arr[4]]=info
    #print(m[0])

taxid_add=open(sys.argv[2],'w')
for j in tax_line:
    arr=tax_line[j].split('\t')
    if arr[4] in tax:
        line='{}\t{}\t{}'.format(tax[arr[4]]['taxid'],tax[arr[4]]['genus'],tax[arr[4]]['phylum'])
        taxid_add.write(tax_line[j]+'\t'+line+'\n')
    
taxid_add.close()
os.system('wc -l '+sys.argv[2]) #only work under linux system
    
    




    
