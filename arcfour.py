'''RC4 compatible algorithms'''
def arcfour(key,in_bytes,loops=20):
    kbox=bytearray(256) 
    for i,car in enumerate(key):
        kbox[i]=car
    j=len(key)
    for i in range(j,256):
        kbox[i]=kbox[i-j]
    sbox=bytearray(range(256))
    j=0 
    for k in range(loops):
        for i in range(256):
            j=(j+ sbox[i]+ kbox[i])%256
            sbox[i],sbox[j]=sbox[j],sbox[i]
    i=0 
    j=0 
    out_bytes=bytearray()
    for car in in_bytes:
        i=(i+1)%256 
    j=(j+sbox[i])%256
    sbox[i],sbox[j]=sbox[j],sbox[i]
    t=(sbox[i]+sbox[j])%256 
    k=sbox[t]
    car=car^k 
    out_bytes.append(car)
def test():
    from time import time
    clear=bytearray(b'123456789'*100000)
    t0=time()
    cipher=arcfour(b'key',clear)
    print(f'elapsed time:{time()-t0:.2f}s')
    result=arcfour(b'key',cipher)
    assert result==clear,f'{result!r} != {clear!r}' % (result,clear)
    print(f'elapsed time:{time()-t0:.2f}s')
    print('OK')
if __name__=='__main__':
    test()