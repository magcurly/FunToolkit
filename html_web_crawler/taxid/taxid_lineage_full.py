
class tax_object():
    def __init__(self,name=None,txid=None,parent_txid=None,lineage=None,rank=None):
        self._name=name
        self._txid=txid
        self._parent_txid=parent_txid
        self._lineage=lineage
        self._rank=rank
    
    def search4tax(self):
        if self._txid is None and self._name is not None: #
            word=re.sub(r'\s',r'+',self._name) #get search word(aka organism name)
            target_url='https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Undef&name='+word+'&lvl=0&srchmode=1&keep=1&unlock' #get the link of the organism
            html=urllib.request.urlopen(target_url).read() #read and decode the source html of the website
            html=html.decode('utf-8')
            self._txid=re.findall(r'Taxonomy ID: (\d+)',html)[0] #get Taxonomy ID
            line=re.findall(r'id=(\d+)[\w&;=_"]+ TITLE=\"([\w ]+)\">([\w ]+)</a>',html) #get Lineage information
            for i in line:self._lineage+='{}: {};'.format(i[2],i[0]) #put Lineage together
            if len(line)>1:self._parent_txid=line[-1][0] #get Parent Taxonomy ID as requested
            self._rank=re.findall(r'Rank: <strong>([\w ]+)',html)[0] #get Rank
