import sys
with open(sys.argv[1]) as f:
    filebytes = f.read().encode()
    fileint = int.from_bytes(filebytes, 'big')
    print(f"exec(int( '{str(bin(fileint))[2:].replace('0', ' ').replace('1', '\t')}'.translate({{32:48,9:49}}),2).to_bytes(length={len(filebytes)}).decode())", end='')
