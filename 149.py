import sys
for x in open(sys.argv[1]):
	o=''
	for s,m,l,n in zip('IXCM','VLD.','XCM.',x[:-1][::-1]):
		n=int(n)+1
		f=n%5-1
		if n>9:
			m=l
		o+=s*f+m*(n>4)+s*(-f)
	print(o[::-1])
