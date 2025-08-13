import sys
for x in open(sys.argv[1]):
    o=''
    for s,m,l,n in zip('IXCM','VLD.','XCM.',x[:-1][::-1]):
        n=int(n)
        f=(n+1)%5-1
        o+=s*f+(m if n<9 else l)*(n>3)+s*(-f)
    print(o[::-1])
