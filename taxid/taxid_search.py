import sys,os
import urllib.request
import re
#from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys

url = "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi"
#driver = webdriver.PhantomJS(executable_path='/mnt/f/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

tax_file = open('./CGR.infomation.tsv','r')

tax={}
tax_line={}
for line in tax_file:
    line=line.strip('( )*\n')
    arr=line.split('\t')
    if arr[4] not in tax:
        tax[arr[4]]=1
    tax_line[arr[0]]=line
tax_file.close()

for i in tax:
    word=re.sub(r'\s',r'+',i)
    target_url=url+'?mode=Undef&name='+word+'&lvl=0&srchmode=1&keep=1&unlock'
    #print(target_url)
    html=urllib.request.urlopen(target_url).read()
    html=html.decode('utf-8')
    m=re.findall(r'Taxonomy ID: (\d+)',html)
    tax[i]=m[0]
    #print(m[0])

taxid_add=open('./CGR.infomation_taxid.tsv','w')
for j in tax_line:
    arr=tax_line[j].split('\t')
    if arr[4] in tax:
        taxid_add.write(tax_line[j]+'\t'+tax[arr[4]]+'\n')
    
taxid_add.close()
os.system('wc -l ./CGR.infomation_taxid.tsv')
    
    




    
