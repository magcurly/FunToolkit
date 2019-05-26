print('The format of the bms file is printed as below\n\n')print('#SampleName\tInsertsize\tChip\tLane\tBarcode\tPath')print('Sample1\t230\tCL100000000\tL01\t501\t/zfssz1/xxxxx')



try:
	bms=open(sys.argv[1],'r')
except sys.argv[1] is None or sys.argv[1]=='help':
	usage()
	sys.exit(0)

#title=sys.argv[1]
#title=title.replace('.bms','.cfg')
#config=open(title,'w')
#for line in bms.readlines():if re.search('#',line): continueline=line.strip('\n')arr=line.split('\t')config.wirte(



