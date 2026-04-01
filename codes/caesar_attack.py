def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted = chr((ord(char) - base - shift) % 26 + base)
            result += decrypted
        else:
            result += char
    return result

def break_caesar(ciphertext):
    print("="*60)
    print("CAESAR CIPHER ATTACK")
    print("="*60)
    print(f"\nCiphertext: {ciphertext}\n")
    print("-"*60)
    
    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift:2d}: {decrypted}")
    
    print("-"*60)

cipher1 = "odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo"
cipher2 = "JpcyvkVexzevvizexTfccvxvzjrkvtyeztrczejkzklkzfewftljvufehlrckpvexzevvizexvultrkzfekyiflxyjkifexkyvfipreugirtkztrccvriezex.Zkrzdjkfuvmvcfgjbzccvuuzjtzgczeijuereuzeuljkip-ivrupvexzevvij."

print("\n" + "#"*60)
print("CHECKPOINT 1: BREAKING CAESAR CIPHER")
print("#"*60)

print("\n\n>>> CIPHER 1 <<<")
break_caesar(cipher1)

print("\n\n>>> CIPHER 2 <<<")
break_caesar(cipher2)

print("\n" + "="*60)
print("ANALYSIS OF RESULTS")
print("="*60)

shift1 = 10
shift2 = 17

print(f"\nCipher 1 - Best shift found: {shift1}")
print(f"Decrypted: {caesar_decrypt(cipher1, shift1)}")

print(f"\nCipher 2 - Best shift found: {shift2}")
print(f"Decrypted: {caesar_decrypt(cipher2, shift2)}")
