import sys
for x in open(sys.argv[1]):
	o=''
	for s,m,l,n in zip('IXCM','VLD.','XCM.',x[:-1][::-1]):
		n=int(n)+1
		f=n%5-1
		o+=s*f+(l if n>9 else m)*(n>4)+s*(-f)
	print(o[::-1])
