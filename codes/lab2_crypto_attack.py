print("="*70)
print("LAB 2: ATTACKING CLASSIC CRYPTO SYSTEMS")
print("="*70)

def caesar_decrypt(txt, shft):
    res = ""
    for c in txt:
        if c.isalpha():
            b = ord('A') if c.isupper() else ord('a')
            res += chr((ord(c) - b - shft) % 26 + b)
        else:
            res += c
    return res

def brute_caesar(ctxt):
    print("\nTrying all 26 shifts...")
    print("-"*50)
    for s in range(26):
        dec = caesar_decrypt(ctxt, s)
        print(f"Shift {s:2d}: {dec[:60]}...")
    print("-"*50)

print("\n")
print("#"*70)
print("CHECKPOINT 1: CAESAR CIPHER ATTACK (10 Marks)")
print("#"*70)

c1 = "odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo"
c2 = "JpcyvkVexzevvizexTfccvxvzjrkvtyeztrczejkzklkzfewftljvufehlrckpvexzevvizexvultrkzfekyiflxyjkifexkyvfipreugirtkztrccvriezex.Zkrzdjkfuvmvcfgjbzccvuuzjtzgczeijuereuzeuljkip-ivrupvexzevvij."

print("\n>>> Cipher 1:")
print(f"Ciphertext: {c1}")
brute_caesar(c1)

shift1 = 10
plain1 = caesar_decrypt(c1, shift1)
print(f"\nBest shift: {shift1}")
print(f"Plaintext: {plain1}")

print("\n\n>>> Cipher 2:")
print(f"Ciphertext: {c2}")
brute_caesar(c2)

shift2 = 17
plain2 = caesar_decrypt(c2, shift2)
print(f"\nBest shift: {shift2}")
print(f"Plaintext: {plain2}")

print("\n\n" + "="*70)
print("CHECKPOINT 1 - FINAL RESULTS")
print("="*70)
print(f"\nCipher 1 Decrypted (shift={shift1}):")
print(f"  {plain1}")
print(f"\nCipher 2 Decrypted (shift={shift2}):")
print(f"  {plain2}")


print("\n\n")
print("#"*70)
print("CHECKPOINT 2: PLAYFAIR CIPHER ATTACK (10 Marks)")
print("#"*70)

def build_matrix(kword):
    kword = kword.upper().replace('J', 'I')
    letters = []
    for c in kword:
        if c not in letters and c.isalpha():
            letters.append(c)
    
    alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for c in alpha:
        if c not in letters:
            letters.append(c)
    
    mat = []
    for i in range(5):
        mat.append(letters[i*5:(i+1)*5])
    return mat

def get_pos(mat, ch):
    ch = ch.upper()
    if ch == 'J':
        ch = 'I'
    for row in range(5):
        for col in range(5):
            if mat[row][col] == ch:
                return row, col
    return None, None

def print_matrix(mat):
    print("\nPlayfair Key Matrix:")
    print("+" + "-"*11 + "+")
    for row in mat:
        print("| " + " ".join(row) + " |")
    print("+" + "-"*11 + "+")

def decrypt_playfair(ctxt, kword):
    mat = build_matrix(kword)
    print_matrix(mat)
    
    clean = ""
    for c in ctxt.upper():
        if c.isalpha():
            clean += 'I' if c == 'J' else c
    
    digraphs = []
    i = 0
    while i < len(clean):
        if i + 1 < len(clean):
            digraphs.append(clean[i] + clean[i+1])
        else:
            digraphs.append(clean[i] + 'X')
        i += 2
    
    ptxt = ""
    for dg in digraphs:
        r1, c1 = get_pos(mat, dg[0])
        r2, c2 = get_pos(mat, dg[1])
        
        if r1 == r2:
            ptxt += mat[r1][(c1 - 1) % 5]
            ptxt += mat[r2][(c2 - 1) % 5]
        elif c1 == c2:
            ptxt += mat[(r1 - 1) % 5][c1]
            ptxt += mat[(r2 - 1) % 5][c2]
        else:
            ptxt += mat[r1][c2]
            ptxt += mat[r2][c1]
    
    return ptxt

keyword = "cryptography"
ciphertext = "fqdagvbydhqldrvckppfmkqzmksyfhqdqndlmglyglcxrktmtnrknlwlowpbgckxfeoyrdqzltfwmdofcbmkpedclkbyhogmoyginblfikwflyfhquudqzmkqzzbcgmafmryptpkalrkpoqflxkmgiqctybcdrcralikefssyfhqdwngcngpkaleyglbyybtdmgqz"

print(f"\nKey: {keyword}")
print(f"\nCiphertext:\n{ciphertext}")

decrypted = decrypt_playfair(ciphertext, keyword)

final_text = ""
for c in decrypted:
    final_text += c

print("\n" + "="*70)
print("CHECKPOINT 2 - FINAL RESULTS")
print("="*70)

print(f"\nRaw Decrypted Text:")
for i in range(0, len(decrypted), 60):
    print(f"  {decrypted[i:i+60]}")

cleaned = decrypted.replace('X', ' ')
print(f"\nReadable Text (X replaced with space):")
for i in range(0, len(cleaned), 60):
    print(f"  {cleaned[i:i+60]}")

print("\n\n" + "="*70)
print("APPROACH EXPLANATION")
print("="*70)

print("""
CAESAR CIPHER ATTACK APPROACH:
------------------------------
1. Caesar cipher shifts each letter by a fixed amount (0-25)
2. Only 26 possible keys exist, so brute force is practical
3. Try all shifts and look for readable English text
4. Cipher 1: shift of 10 reveals 'ethereum is the best smart contract...'
5. Cipher 2: shift of 17 reveals 'Sylhet Engineering College...'

PLAYFAIR CIPHER ATTACK APPROACH:
--------------------------------
1. The key 'cryptography' is given, so we build the 5x5 matrix
2. Remove duplicate letters from key, then fill rest with alphabet
3. I and J are treated as same letter (standard Playfair rule)
4. For decryption, reverse the three rules:
   - Same row: shift LEFT (instead of right)
   - Same column: shift UP (instead of down)  
   - Rectangle: swap corners (same as encryption)
5. Process ciphertext in pairs (digraphs)
6. Remove filler X characters to get final plaintext
""")

print("="*70)
print("END OF LAB 2")
print("="*70)
