import re
import urllib.request

def search4tax(type,word):
    info={}
    if type == 'id':
        t_id=word
        target_url='https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id='+t_id+'&lvl=3&p=mapview&p=has_linkout&p=blast_url&p=genome_blast&lin=f&keep=1&srchmode=5&unlock'
    elif type == 'name':
        t_name=re.sub(r'\s',r'+',word)
        target_url='https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Undef&name='+t_name+'&lvl=0&srchmode=1&keep=1&unlock'
    else:
        return None
    html=urllib.request.urlopen(target_url).read() #read and decode the source html of the website
    html=html.decode('utf-8')
    info['name']=re.findall(r'<h2>(.+)</h2>',html)[0]
    info['taxid']=re.findall(r'Taxonomy ID: (\d+)',html)[0]
    info['lineage']=''
    line=re.findall(r'id=(\d+)[\w&;=_"]+ TITLE=\"([\w ]+)\">([\w ]+)</a>',html)
    for i in line:
        info['lineage']+='{}: {};'.format(i[2],i[0]) #put Lineage together
    if len(line)>=1:
        info['parent_id']=line[-1][0]
    info['rank']=re.findall(r'Rank: <strong>([\w ]+)',html)[0]#get Rank
    return info

class tax_object():
    def __init__(self,name=None,txid=None,parent_txid=None,lineage='',rank=None):
        self._name=name
        self._txid=txid
        self._parent_txid=parent_txid
        self._lineage=lineage
        self._rank=rank

    def check4tax(self):
        if self._name is not None:
            info=search4tax('name',self._name)
        else:
            return False
        
        if self._txid != info['taxid'] or self._lineage != info['lineage'] or self._parent_txid != info[''] or self._rank != info['rank']:
            return False
        else: 
            return info

    def assign4tax(self):
        if self._name is None and self._name is None:
            return False
        elif self._txid is None or self._name is None: 
            if self._name is not None:
                info=search4tax('name',self._name)
                self._txid=info['taxid']
            elif self._txid is not None:
                info=search4tax('id',self._txid)
                self._name=info['name']
        else:
            info = check4tax(self)
            if info is False:
                print('This organism needs to be check -- '+self._name+'\n')
                return False
        
        self._lineage=info['lineage']
        self._parent_txid=info['parent_id']
        self._rank=info['rank']
    
    def printtax(self):
        return self._name+'\t'+self._txid+'\t'+self._parent_txid+'\t'+self._lineage+'\t'+self._rank
