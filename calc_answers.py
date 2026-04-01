import string

def vig_encrypt(pt,key):
    a=string.ascii_uppercase
    res=[]
    ki=0
    for ch in pt.upper():
        if ch in a:
            p=a.index(ch); k=a.index(key[ki%len(key)].upper());
            res.append(a[(p+k)%26]); ki+=1
        else:
            res.append(ch)
    return ''.join(res)

print('VIG', vig_encrypt('SECURITY','KEY'))

# Playfair

def build_matrix(key):
    key=key.upper().replace('J','I')
    seen=[]
    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.append(ch)
    for ch in string.ascii_uppercase:
        if ch=='J':
            continue
        if ch not in seen:
            seen.append(ch)
    matrix=[seen[i:i+5] for i in range(0,25,5)]
    pos={matrix[r][c]:(r,c) for r in range(5) for c in range(5)}
    return matrix,pos

def digraphs(text):
    t=''.join(ch for ch in text.upper() if ch.isalpha()).replace('J','I')
    out=[]; i=0
    while i<len(t):
        a=t[i]
        if i+1>=len(t):
            b='X'; i+=1
        else:
            b=t[i+1]
            if a==b:
                b='X'; i+=1
            else:
                i+=2
        out.append(a+b)
    return out

def playfair_encrypt(text,key):
    matrix,pos=build_matrix(key)
    d=digraphs(text)
    enc=[]
    for pair in d:
        a,b=pair
        ra,ca=pos[a]; rb,cb=pos[b]
        if ra==rb:
            enc.append(matrix[ra][(ca+1)%5]+matrix[rb][(cb+1)%5])
        elif ca==cb:
            enc.append(matrix[(ra+1)%5][ca]+matrix[(rb+1)%5][cb])
        else:
            enc.append(matrix[ra][cb]+matrix[rb][ca])
    return matrix,d,enc,''.join(enc)

m,d,e,c=playfair_encrypt('HIDE MONEY','MONARCHY')
print('MATRIX')
for row in m:
    print(' '.join(row))
print('DIGRAPHS',d)
print('ENC_PAIRS',e)
print('CIPHER',c)
