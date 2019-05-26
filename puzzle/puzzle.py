import re
ref1="ATTCTTTAGCACCGACTATTCAGAAGACTTTGTTACATTACACCATAACGCATTAGACTTGCAGCAACGAATCGATTATCAACATTACACATC"

ref2="ZEBRA DNA SEQ BY BGIRESEARCH AND CNGB"
test="ATTCTTACCCTTTAATAAGATAAATTACAAATACTTTTTAATCGA"
lib={}
for i in range(0,len(ref1),3):
    if ref1[i:i+3]in lib.keys():
        lib[ref1[i:i+3]]+=1
    else:
        lib[ref1[i:i+3]]=1
print(lib)
for i in range(0,len(test),3):
    if test[i:i+3] in lib.keys():
        print(test[i:i+3],"\t",'yes')
    else:
        print(test[i:i+3],'\t','no')
print(len(ref1))
print(len(ref2))
print(len(test))