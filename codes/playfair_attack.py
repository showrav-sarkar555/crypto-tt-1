def mk_mat(kw):
    kw = kw.upper().replace('J', 'I')
    s = []
    for ch in kw:
        if ch not in s and ch.isalpha():
            s.append(ch)
    
    alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for ch in alpha:
        if ch not in s:
            s.append(ch)
    
    mat = []
    for i in range(5):
        mat.append(s[i*5:(i+1)*5])
    return mat

def get_pos(mat, ch):
    ch = ch.upper()
    if ch == 'J':
        ch = 'I'
    for r in range(5):
        for c in range(5):
            if mat[r][c] == ch:
                return r, c
    return None, None

def decrypt(ct, kw):
    mat = mk_mat(kw)
    
    clean = ""
    for ch in ct.upper():
        if ch.isalpha():
            if ch == 'J':
                clean += 'I'
            else:
                clean += ch
    
    prs = []
    for i in range(0, len(clean), 2):
        if i + 1 < len(clean):
            prs.append(clean[i] + clean[i+1])
        else:
            prs.append(clean[i] + 'X')
    
    pt = ""
    
    for pr in prs:
        r1, c1 = get_pos(mat, pr[0])
        r2, c2 = get_pos(mat, pr[1])
        
        if r1 == r2:
            pt += mat[r1][(c1 - 1) % 5]
            pt += mat[r2][(c2 - 1) % 5]
        elif c1 == c2:
            pt += mat[(r1 - 1) % 5][c1]
            pt += mat[(r2 - 1) % 5][c2]
        else:
            pt += mat[r1][c2]
            pt += mat[r2][c1]
    
    return pt

key = "cryptography"
cipher = "fqdagvbydhqldrvckppfmkqzmksyfhqdqndlmglyglcxrktmtnrknlwlowpbgckxfeoyrdqzltfwmdofcbmkpedclkbyhogmoyginblfikwflyfhquudqzmkqzzbcgmafmryptpkalrkpoqflxkmgiqctybcdrcralikefssyfhqdwngcngpkaleyglbyybtdmgqz"

print("Key:", key)
print("\nCiphertext:", cipher)

result = decrypt(cipher, key)
print("\nDecrypted:", result)
