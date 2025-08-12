import sys
o = ''
for x in open(sys.argv[1]).read()[::-1].split('\n'):
    for s, m, l, n in zip('IXCM', 'VLD.', 'XCM.', x):
        n = int(n)
        f = n % 5
        o += s * f * (f < 4) + (m if n < 9 else l) * (n > 3) + s * (f == 4)
    o += '\n'
print(o[-2:1:-1])
