import sys,os,re,json
from treelib import Tree, Node

#catalog 2 tree
tax=['root']

tax_tree=Tree()
tax_tree.create_node('root','root')
filea = open(sys.argv[1],'r')
head=filea.readline()
for line in filea.readlines():
    line=line.strip()
    arr=line.split('\t')
    upper='root'
    for i in range(1,len(arr)):
        if arr[i] == "NA":continue
        if arr[i] not in tax:
            tax.append(arr[i])
            tax_tree.create_node(arr[i],arr[i],parent=upper,data=arr[i])
        upper=arr[i]

tax_tree.save2file(sys.argv[2])
#print(tax_tree.to_dict())

#def convert_dict_to_stdjson(tree_dict):
#    js='"name":root,"children":'
#    for key in tree_dict:
        
def to_dict(tree, nid=None, key=None, sort=True, reverse=False, with_data=False):
        """Transform the whole tree into a dict."""

        nid = tree.root if (nid is None) else nid
        ntag = tree[nid].tag
        tree_dict = {ntag: {"children": []}}
        json_dict={"name":ntag,"children":[]}
        if with_data:
            tree_dict[ntag]["data"] = tree[nid].data
            #json_dict["data"]=tree[nid].data

        if tree[nid].expanded:
            queue = [tree[i] for i in tree[nid].fpointer]
            key = (lambda x: x) if (key is None) else key
            if sort:
                queue.sort(key=key, reverse=reverse)

            for elem in queue:
                tree_dict[ntag]["children"].append(
                    to_dict(tree,elem.identifier, with_data=with_data, sort=sort, reverse=reverse))
                json_dict["children"].append(to_dict(tree,elem.identifier, with_data=with_data, sort=sort, reverse=reverse))
            if len(tree_dict[ntag]["children"]) == 0:
                tree_dict = tree[nid].tag if not with_data else \
                    {ntag: {"data": self[nid].data}}
            return json_dict   
    
def json_to_newick(json):
    def _parse_json(json_obj):
        try:
            newick = json_obj['name']
        except KeyError:
            newick = ''
        if 'branch_length' in json_obj:
            newick = newick + ':' + str(json_obj['branch_length'])
        if 'children' in json_obj:
            info = []
            if len(json_obj['children'])>0:
                for child in json_obj['children']:
                    info.append(_parse_json(child))
                info = ','.join(info)
                newick = '(' + info + ')' + newick
            else:
                newick=newick
        return newick
    newick = _parse_json(json) + ';'
    return newick

newick_f=open(sys.argv[3],'w')
newick_f.write(json_to_newick(to_dict(tax_tree)))
newick_f.close()

